from pydantic import BaseModel
from typing import Optional, Dict, Any

class DocumentRequest(BaseModel):
    area: str
    tipo_documento: str
    detalhes: Dict[str, Any]
    # Adicionamos este campo novo (Opcional para não quebrar outras rotas)
    dados_escritorio: Optional[Dict[str, Any]] = None

class DocumentResponse(BaseModel):
    sucesso: bool
    documento: str
    metadata: Optional[Dict[str, Any]] = None