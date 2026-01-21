import os
from typing import Dict, List
from dotenv import load_dotenv
from templates_especificos import gerar_template_especifico
import io
import json
import re

load_dotenv()

# 🔥 CONFIGURAÇÃO DAS APIs
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not ANTHROPIC_API_KEY and not GEMINI_API_KEY:
    print("⚠️ AVISO: Nenhuma API configurada. Sistema funcionará com REGEX apenas.")


# ═══════════════════════════════════════════════════════════
#           EXTRAÇÃO AUTOMÁTICA (UPLOAD)
# ═══════════════════════════════════════════════════════════

async def analisar_documento_upload(file_content, filename) -> Dict:
    """
    🔥 EXTRAÇÃO INTELIGENTE COM IA (ANTHROPIC OU GEMINI)
    """
    
    print(f"📄 Analisando: {filename}")
    
    # 1️⃣ EXTRAIR TEXTO
    texto_extraido = ""
    
    try:
        if filename.lower().endswith('.pdf'):
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            for page in pdf_reader.pages:
                texto_extraido += page.extract_text() + "\n"
        
        elif filename.lower().endswith('.docx'):
            import docx
            doc = docx.Document(io.BytesIO(file_content))
            for para in doc.paragraphs:
                texto_extraido += para.text + "\n"
        
        else:
            texto_extraido = file_content.decode('utf-8', errors='ignore')
    
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return {"erro": str(e)}
    
    if not texto_extraido.strip():
        return {"erro": "Documento vazio"}
    
    print(f"✅ Texto extraído: {len(texto_extraido)} caracteres")
    
    # 2️⃣ TENTAR ANTHROPIC (CLAUDE)
    if ANTHROPIC_API_KEY:
        try:
            print("🤖 Usando Claude Anthropic...")
            return await extrair_com_claude(texto_extraido)
        except Exception as e:
            print(f"⚠️ Erro no Claude: {e}")
    
    # 3️⃣ TENTAR GEMINI (GOOGLE)
    if GEMINI_API_KEY:
        try:
            print("🤖 Usando Gemini Google...")
            return await extrair_com_gemini(texto_extraido)
        except Exception as e:
            print(f"⚠️ Erro no Gemini: {e}")
    
    # 4️⃣ FALLBACK: REGEX
    print("🔄 Usando extrator REGEX...")
    return extrair_dados_regex(texto_extraido)


async def extrair_com_claude(texto: str) -> Dict:
    """Claude Anthropic"""
    import anthropic
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        temperature=0,
        system="Você é um extrator de dados jurídicos. Retorne APENAS JSON puro com os campos encontrados no texto. Se não encontrar, use null.",
        messages=[{"role": "user", "content": f"Extraia dados deste documento:\n\n{texto[:20000]}"}]
    )
    
    content = response.content[0].text.strip()
    
    if '```' in content:
        content = content.split('```')[1]
        if content.startswith('json'):
            content = content[4:]
    
    dados = json.loads(content.strip())
    return {k: v for k, v in dados.items() if v is not None}


async def extrair_com_gemini(texto: str) -> Dict:
    """Google Gemini"""
    import google.generativeai as genai
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""Extraia dados jurídicos deste documento em JSON puro.
Campos: autor, autor_cpf, reu, numero_processo, fatos, valor_causa, etc.
Retorne APENAS o JSON sem markdown.

TEXTO:
{texto[:20000]}"""
    
    response = model.generate_content(prompt)
    content = response.text.strip()
    
    if '```' in content:
        content = content.split('```')[1]
        if content.startswith('json'):
            content = content[4:]
    
    dados = json.loads(content.strip())
    return {k: v for k, v in dados.items() if v is not None}


def extrair_dados_regex(texto: str) -> Dict:
    """Extrator REGEX (fallback)"""
    
    dados = {}
    
    # CPF
    cpf_match = re.search(r'cpf[:\s]*(\d{3}\.?\d{3}\.?\d{3}-?\d{2})', texto, re.IGNORECASE)
    if cpf_match:
        dados['autor_cpf'] = cpf_match.group(1)
    
    # Nome
    nome_match = re.search(r'([A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ][a-záàâãéèêíïóôõöúçñ]+\s[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ][a-záàâãéèêíïóôõöúçñ]+)', texto)
    if nome_match:
        nome = nome_match.group(1).strip()
        if 5 < len(nome) < 100:
            dados['autor'] = nome
    
    # Processo
    processo_match = re.search(r'\d{7}-?\d{2}\.?\d{4}\.?\d\.?\d{2}\.?\d{4}', texto)
    if processo_match:
        dados['numero_processo'] = processo_match.group(0)
    
    # Valores
    valores = re.findall(r'R\$\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)', texto)
    if valores:
        try:
            maior = max([float(v.replace('.', '').replace(',', '.')) for v in valores])
            dados['valor_causa'] = f"{maior:.2f}".replace('.', ',')
        except:
            pass
    
    return dados


# ═══════════════════════════════════════════════════════════
#              GERAÇÃO DE DOCUMENTO
# ═══════════════════════════════════════════════════════════

async def gerar_documento_juridico(area: str, tipo: str, detalhes: Dict) -> str:
    """Gera documento usando templates"""
    
    peca_id = detalhes.get('peca_id', '')
    
    if not peca_id:
        return "❌ ERRO: peca_id não fornecido"
    
    print(f"🔍 Gerando: {peca_id}")
    
    try:
        documento = gerar_template_especifico(peca_id, area, detalhes)
        
        if documento.startswith('[ERRO:'):
            return f"❌ Template não encontrado: {peca_id}"
        
        return documento
    
    except Exception as e:
        return f"❌ ERRO: {str(e)}"


# ═══════════════════════════════════════════════════════════
#         BUSCA DE JURISPRUDÊNCIA COM IA
# ═══════════════════════════════════════════════════════════

async def buscar_jurisprudencia_com_ia(tema: str, tipo_peca: str = "", contexto_caso: str = "") -> List[Dict]:
    """
    ⚖️ BUSCA JURISPRUDÊNCIA COM IA (GEMINI OU ANTHROPIC)
    """
    
    print(f"⚖️ Buscando jurisprudência: {tema}")
    
    # 1️⃣ TENTAR GEMINI (MAIS RÁPIDO)
    if GEMINI_API_KEY:
        try:
            print("🤖 Usando Gemini...")
            return await gerar_jurisp_gemini(tema, tipo_peca)
        except Exception as e:
            print(f"⚠️ Gemini falhou: {e}")
    
    # 2️⃣ TENTAR ANTHROPIC
    if ANTHROPIC_API_KEY:
        try:
            print("🤖 Usando Claude...")
            return await gerar_jurisp_claude(tema, tipo_peca)
        except Exception as e:
            print(f"⚠️ Claude falhou: {e}")
    
    # 3️⃣ FALLBACK: EXEMPLOS
    return gerar_jurisprudencias_exemplo(tema)


async def gerar_jurisp_gemini(tema: str, tipo_peca: str) -> List[Dict]:
    """Gemini Google"""
    import google.generativeai as genai
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash', 
                                   generation_config={"response_mime_type": "application/json"})
    
    prompt = f"""Gere 5 jurisprudências REALISTAS sobre: "{tema}"

REGRAS:
1. Use tribunais reais (STJ, STF, TJ-SP, TST)
2. Números genéricos (REsp 1.XXX.XXX/SP)
3. Ementas profissionais (150-300 palavras)

Retorne JSON:
[
  {{
    "tribunal": "STJ",
    "numero": "REsp 1.XXX.XXX/SP",
    "data": "15/03/2024",
    "relator": "Min. João Silva",
    "ementa": "DIREITO CIVIL. TEMA..."
  }}
]"""
    
    response = model.generate_content(prompt)
    jurisprudencias = json.loads(response.text)
    
    print(f"✅ {len(jurisprudencias)} jurisprudências geradas (Gemini)")
    return jurisprudencias


async def gerar_jurisp_claude(tema: str, tipo_peca: str) -> List[Dict]:
    """Claude Anthropic"""
    import anthropic
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=6000,
        temperature=0.3,
        system="Você é um especialista em jurisprudência brasileira. Gere jurisprudências REALISTAS em JSON.",
        messages=[{
            "role": "user",
            "content": f"""Gere 5 jurisprudências sobre: {tema}

Retorne JSON:
[
  {{"tribunal": "STJ", "numero": "REsp 1.XXX.XXX/SP", "data": "15/03/2024", "relator": "Min. João Silva", "ementa": "..."}}
]"""
        }]
    )
    
    content = response.content[0].text.strip()
    
    json_match = re.search(r'\[[\s\S]*\]', content)
    if not json_match:
        raise Exception("Formato inválido")
    
    jurisprudencias = json.loads(json_match.group(0))
    
    print(f"✅ {len(jurisprudencias)} jurisprudências geradas (Claude)")
    return jurisprudencias


def gerar_jurisprudencias_exemplo(tema: str) -> List[Dict]:
    """Exemplos (fallback)"""
    
    print("📚 Usando jurisprudências de exemplo...")
    
    return [
        {
            "tribunal": "STJ",
            "numero": "REsp 1.XXX.XXX/SP",
            "data": "15/03/2024",
            "relator": "Min. João Silva Santos",
            "ementa": f"DIREITO CIVIL. {tema.upper()}. Jurisprudência consolidada do STJ orienta que {tema} deve observar princípios da razoabilidade e proporcionalidade (CC, art. 944). Recurso conhecido e provido."
        },
        {
            "tribunal": "TJ-SP",
            "numero": "Apelação 1.XXX.XXX-XX.XXXX.8.26.0100",
            "data": "22/02/2024",
            "relator": "Des. Maria Santos Silva",
            "ementa": f"PROCESSO CIVIL. {tema.upper()}. Demonstrada procedência conforme provas dos autos (CPC, arts. 319 e 373, I). Sentença mantida."
        },
        {
            "tribunal": "TST",
            "numero": "RO 1.XXX.XXX-XX.2024.5.02.0000",
            "data": "05/12/2023",
            "relator": "Des. Pedro Henrique Costa",
            "ementa": f"RECURSO ORDINÁRIO. {tema.upper()}. Aplicação dos princípios da proteção ao trabalhador (CLT, art. 818). Recurso conhecido e provido."
        }
    ]