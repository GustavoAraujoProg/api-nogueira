import PyPDF2
import re
import os
import json
from io import BytesIO
from docx import Document
from groq import Groq
from dotenv import load_dotenv
import unicodedata

load_dotenv()

# ============================================
# 1. FERRAMENTAS DE LIMPEZA
# ============================================
def limpar_texto_preservando_linhas(texto):
    if not texto: return ""
    # Normaliza mas MANTÉM os \n para detectar parágrafos
    return texto.replace('\r', '')

def limpar_json_da_ia(resposta_texto):
    try:
        inicio = resposta_texto.find('{')
        fim = resposta_texto.rfind('}') + 1
        if inicio != -1 and fim != -1:
            return json.loads(resposta_texto[inicio:fim])
        return None
    except: return None

# ============================================
# 2. LEITORES (PDF/DOCX)
# ============================================
def extrair_texto_pdf(arquivo_bytes):
    try:
        reader = PyPDF2.PdfReader(BytesIO(arquivo_bytes))
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() + "\n"
        return texto
    except: return ""

def extrair_texto_docx(arquivo_bytes):
    try:
        doc = Document(BytesIO(arquivo_bytes))
        # Pega o texto mantendo as quebras de parágrafo
        full_text = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(full_text)
    except: return ""

# ============================================
# 3. EXTRATOR "CIRÚRGICO" (FOCA NO TEXTO)
# ============================================
def extrair_fatos_na_marra(texto):
    """
    Tenta recortar exatamente o texto entre 'DOS FATOS' e 'DO DIREITO'.
    """
    texto_upper = texto.upper()
    
    # Marcadores comuns em Petições Iniciais
    marcos_inicio = ["I - DOS FATOS", "1. DOS FATOS", "DOS FATOS", "DA SÍNTESE", "BREVE SÍNTESE", "DO RESUMO"]
    marcos_fim = ["II - DO DIREITO", "2. DO DIREITO", "DO DIREITO", "DO MÉRITO", "DOS PEDIDOS", "III -"]
    
    idx_inicio = -1
    idx_fim = -1
    
    # 1. Acha o começo
    for m in marcos_inicio:
        pos = texto_upper.find(m)
        if pos != -1:
            idx_inicio = pos + len(m) # Pula o título
            break
            
    # 2. Acha o fim (só procura DEPOIS do início)
    if idx_inicio != -1:
        for m in marcos_fim:
            pos = texto_upper.find(m, idx_inicio)
            if pos != -1:
                idx_fim = pos
                break
                
        # Se achou início e fim, recorta o miolo
        if idx_fim != -1:
            return texto[idx_inicio:idx_fim].strip()
        
        # Se achou só o início, pega os próximos 4000 caracteres
        return texto[idx_inicio:idx_inicio+4000].strip()
    
    # 3. MODO DESESPERO: Não achou título "DOS FATOS"
    # Pega o texto bruto pulando o cabeçalho (aprox. 500 chars)
    print("⚠️ Títulos não encontrados. Pegando texto bruto.")
    return texto[500:5000].strip()

# ============================================
# 4. EXTRATOR DE METADADOS (REGEX/IA)
# ============================================
def extrair_metadados(texto):
    dados = {"numero_processo": "", "valor_causa": "", "autor": "", "reu": ""}
    
    # Processo (Regex)
    match_proc = re.search(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', texto)
    if match_proc: dados['numero_processo'] = match_proc.group(0)
    else:
        # Tenta achar número solto grande (ex: 0000000000000000)
        match_num = re.search(r'(?:Processo|Autos).*?(\d{13,25})', texto, re.IGNORECASE)
        if match_num: dados['numero_processo'] = match_num.group(1)

    # Valor (Regex)
    vals = re.findall(r'R\$\s?([\d\.]+[,]?\d*)', texto)
    if vals: dados['valor_causa'] = vals[-1]

    # Autor/Réu (IA é melhor pra isso, mas Regex quebra o galho)
    # Aqui a IA (Groq) seria útil só pra nomes, se quiser rapidez usamos Regex
    return dados

# ============================================
# 5. FUNÇÃO PRINCIPAL
# ============================================
def processar_upload_documento(arquivo_bytes, nome_arquivo, tipo_peca, campos_necessarios):
    try:
        # 1. Leitura
        ext = nome_arquivo.lower().split('.')[-1]
        texto = ""
        if ext == 'pdf': texto = extrair_texto_pdf(arquivo_bytes)
        elif ext in ['docx', 'doc']: texto = extrair_texto_docx(arquivo_bytes)
        else: texto = str(arquivo_bytes, 'utf-8', errors='ignore')

        if not texto or len(texto) < 50:
            return {"sucesso": False, "erro": "Documento vazio ou ilegível."}

        # 2. Extração
        # Pega os FATOS na marra (recorte de texto)
        fatos_extraidos = extrair_fatos_na_marra(texto)
        
        # Pega o resto via Regex simples
        metadados = extrair_metadados(texto)
        
        dados_finais = {
            "numero_processo": metadados["numero_processo"],
            "valor_causa": metadados["valor_causa"],
            "autor": metadados["autor"], # Pode vir vazio se regex falhar
            "reu": metadados["reu"]
        }

        # 3. Lógica de Mapeamento
        eh_contestacao = any(x in tipo_peca.lower() for x in ['contestacao', 'defesa', 'resposta'])
        
        if eh_contestacao:
            # Joga o texto recortado DIRETO na impugnação
            dados_finais["impugnacao_fatos"] = fatos_extraidos
            dados_finais["fatos"] = "" # Limpa para não confundir
        else:
            dados_finais["fatos"] = fatos_extraidos

        return {"sucesso": True, "dados": dados_finais}

    except Exception as e:
        print(f"Erro no processamento: {e}")
        return {"sucesso": False, "erro": str(e)}