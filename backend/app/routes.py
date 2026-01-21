from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, Response
from pydantic import BaseModel
from typing import Dict, Optional
import io
import os
import json
import re
import anthropic
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

from pecas_juridicas import PROMPTS_POR_PECA
from docx_generator import gerar_docx_documento
from document_extractor import processar_upload_documento

load_dotenv()
router = APIRouter()

def obter_data_hoje():
    meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    hoje = datetime.now()
    return f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"

class DocumentRequest(BaseModel):
    area: str
    tipo_documento: str
    detalhes: Dict
    dados_escritorio: Optional[Dict] = None

class JurisprudenciaRequest(BaseModel):
    tema: str
    contexto: dict = {}

class TeseRequest(BaseModel):
    tipo_peca: str
    fatos: str
    danos: str = ""

# ============================================
# 🧠 CÉREBRO DE IA (GROQ 3.3 - RÁPIDO E GRATUITO)
# ============================================
def consultar_ia_groq(prompt, max_tokens=6000, temperatura=0.3):
    try:
        api_key = os.environ.get("GROQ_API_KEY")
        if api_key and "gsk_" in api_key:
            client = Groq(api_key=api_key)
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura, # Temperatura controlada
                max_tokens=max_tokens,
            )
            return completion.choices[0].message.content
    except Exception as e:
        print(f"⚠️ Erro Groq: {e}")
        return None

# ============================================
# 1. AGENTE "REVISOR JURÍDICO" (Melhora os Fatos)
# ============================================
def reescrever_fatos_ia(fatos_originais, tipo_peca):
    print("✍️ IA Melhorando a Redação dos Fatos...")
    
    prompt = f"""
    ATUE COMO UM ADVOGADO SÊNIOR E REVISOR DE PEÇAS.
    
    SUA TAREFA:
    Reescrever a narrativa dos fatos abaixo para uma {tipo_peca}.
    Transforme o texto original (que pode estar simples ou informal) em uma NARRATIVA JURÍDICA PROFISSIONAL, ELEGANTE E ROBUSTA.
    
    TEXTO ORIGINAL DO USUÁRIO:
    "{fatos_originais}"
    
    REGRAS RÍGIDAS (OBRIGATÓRIO):
    1. NÃO INVENTE FATOS: Mantenha estritamente a história, datas e valores fornecidos. Não crie testemunhas ou eventos que não existem.
    2. ESTILO: Use linguagem culta ("Nesse diapasão", "Cumpre salientar", "Imperioso destacar").
    3. FLUIDEZ: Conecte os parágrafos de forma lógica.
    4. ROBUSTEZ: Se o texto for curto, expanda a redação (encorpe o texto) explicando a gravidade da situação, mas sem mentir.
    
    SAÍDA:
    Apenas o texto reescrito dos fatos.
    """
    
    # Temperatura baixa (0.2) para garantir fidelidade aos fatos
    return consultar_ia_groq(prompt, temperatura=0.2) 

# ============================================
# 2. AGENTE "DOUTRINADOR" (Escreve o Direito)
# ============================================
def escrever_direito_ia(fatos, tipo_peca):
    print("⚖️ IA Escrevendo Fundamentação Jurídica...")
    prompt = f"""
    AJA COMO UM DOUTOR EM DIREITO E ESPECIALISTA EM PROCESSO CIVIL.
    TAREFA: Escrever o capítulo "DO DIREITO" para uma {tipo_peca}.
    
    BASE FÁTICA:
    "{fatos}"
    
    DIRETRIZES DE ESCRITA:
    - O texto deve ser EXTENSO, DENSO e TÉCNICO (Mínimo 4 páginas teóricas).
    - Citar Constituição Federal (Princípios), Código Civil/CPC/CDC/CLT conforme o caso.
    - INCLUIR DOUTRINA: Cite juristas clássicos (Maria Helena Diniz, Flávio Tartuce, etc).
    - INCLUIR JURISPRUDÊNCIA: Mencione o entendimento consolidado dos tribunais.
    - FORMATO: Use TÍTULOS EM CAIXA ALTA (Ex: "II.1 - DA RESPONSABILIDADE CIVIL").
    """
    return consultar_ia_groq(prompt, temperatura=0.4)

# =====================================================
# ROTAS API
# =====================================================

@router.post("/api/gerar-tese")
async def gerar_conteudo_completo(request: TeseRequest):
    # 1. Melhora a redação dos Fatos
    fatos_melhorados = reescrever_fatos_ia(request.fatos, request.tipo_peca)
    
    # Se der erro, mantém o original
    fatos_finais = fatos_melhorados if fatos_melhorados else request.fatos
    
    # 2. Escreve o Direito (Baseado nos fatos já melhorados)
    direito_gerado = escrever_direito_ia(fatos_finais, request.tipo_peca)
    
    if not direito_gerado:
        direito_gerado = "Erro ao gerar fundamentação jurídica."

    return {
        "fatos_originais": request.fatos,
        "fatos_melhorados": fatos_finais,
        "tese": direito_gerado
    }

@router.post("/api/gerar-docx")
async def gerar_docx_endpoint(request: DocumentRequest):
    try:
        conteudo = request.detalhes.get('conteudo_customizado', '')
        dados_doc = {"tipo": request.tipo_documento, "data": obter_data_hoje(), "area": request.area}
        docx = gerar_docx_documento(dados_doc, conteudo, request.dados_escritorio)
        return Response(content=docx, media_type="application/vnd.word", headers={"Content-Disposition": f'attachment; filename="{request.tipo_documento}.docx"'})
    except Exception as e: print(e); raise HTTPException(500, str(e))

@router.post("/api/extrair-documento")
async def extrair_documento_endpoint(arquivo: UploadFile = File(...), tipo_peca: str = "", campos: str = ""):
    try:
        content = await arquivo.read()
        return processar_upload_documento(content, arquivo.filename, tipo_peca, [c.strip() for c in campos.split(',')])
    except Exception as e: return {"sucesso": False, "erro": str(e)}

@router.post("/api/gerar-jurisprudencia")
async def gerar_jurisprudencia_endpoint(request: JurisprudenciaRequest):
    prompt = f'Retorne 3 ementas de jurisprudência REAIS sobre "{request.tema}" em formato JSON {{ "jurisprudencias": [ ... ] }}.'
    txt = consultar_ia_groq(prompt, max_tokens=2000)
    try:
        if txt:
            match = re.search(r'\{[\s\S]*\}', txt)
            if match: return json.loads(match.group(0))
    except: pass
    return {"jurisprudencias": []}

@router.get("/api/areas")
async def listar_areas():
    return {"areas": [{"id": k, "nome": v["nome"], "icon": v["icon"]} for k, v in PECAS_JURIDICAS.items()]}