from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Importações diretas (agora que os arquivos estão lado a lado, o Python acha nativamente)
from docx_generator import gerar_docx_documento
from document_extractor import processar_upload_documento
from routes import router

# Carrega variáveis de ambiente (.env)
load_dotenv()

# ============================================
# INICIALIZAR O APP
# ============================================
app = FastAPI(
    title="Eduarda Nogueira API",
    description="API Jurídica Inteligente - Geração de Peças e Análise de Documentos",
    version="2.0.0"
)

# ============================================
# CONFIGURAR CORS (Permitir Frontend React)
# ============================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, você pode restringir para o domínio do seu site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# INCLUIR ROTAS
# ============================================
app.include_router(router)

# ============================================
# ROTA DE SAÚDE (HEALTH CHECK)
# ============================================
@app.get("/")
async def root():
    return {
        "status": "online",
        "sistema": "Eduarda Nogueira Legal Intelligence",
        "mensagem": "API rodando perfeitamente!",
        "versao": "2.0.0"
    }