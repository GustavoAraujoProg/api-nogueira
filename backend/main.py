import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq  # Importando a Groq

# Importações dos seus módulos locais
from routes import router
from pecas_juridicas import get_prompt_especializado

# Carrega variáveis de ambiente (.env)
load_dotenv()

# ============================================
# CONFIGURAÇÃO DA IA (GROQ)
# ============================================
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# ============================================
# INICIALIZAR O APP
# ============================================
app = FastAPI(
    title="Eduarda Nogueira API",
    description="API Jurídica Inteligente - Geração de Peças e Análise de Documentos",
    version="2.0.0"
)

# ============================================
# CONFIGURAR CORS
# ============================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# INCLUIR ROTAS (Do arquivo routes.py)
# ============================================
app.include_router(router)

# ============================================
# MODELO DE DADOS (REQUEST)
# ============================================
class TeseRequest(BaseModel):
    tipo_peca: str
    area: str = "civil"  # <--- CAMPO NOVO: Define a personalidade da IA
    fatos: str
    danos: str = ""
    campo_especifico: str = None

# ============================================
# ROTA INTELIGENTE: GERAR TESE
# ============================================
@app.post("/api/gerar-tese")
async def gerar_tese_endpoint(request: TeseRequest):
    try:
        # 1. Chama o Cérebro para criar o Prompt Especialista (Trabalhista, Criminal, etc)
        prompt_sistema = get_prompt_especializado(
            area=request.area,
            peca=request.tipo_peca,
            fatos=request.fatos,
            tese_usuario=request.danos
        )

        # 2. Define o Prompt do Usuário (O pedido direto)
        prompt_usuario = f"Escreva a fundamentação jurídica com base nestes fatos: {request.fatos}. Se houver campo específico ({request.campo_especifico}), foque nele."

        # 3. Chama a IA (Groq)
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            model="llama3-70b-8192", # Modelo super inteligente e rápido
            temperature=0.7,         # Criatividade equilibrada
            max_tokens=2048,         # Tamanho da resposta
        )

        # 4. Processa a resposta
        resposta_ia = chat_completion.choices[0].message.content

        # 5. Retorna o JSON formatado para o Frontend
        return {
            "tese": resposta_ia,
            "fatos_melhorados": request.fatos # Retorna os fatos (podemos melhorar isso no futuro)
        }

    except Exception as e:
        print(f"Erro na IA: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ============================================
# ROTA DE SAÚDE
# ============================================
@app.get("/")
async def root():
    return {
        "status": "online",
        "sistema": "Eduarda Nogueira Legal Intelligence",
        "inteligencia": "Ativada (Groq Llama 3)",
        "versao": "2.1.0"
    }