import sqlite3
from datetime import datetime
from typing import Dict, List, Optional
import json

DATABASE_PATH = "legal_intelligence.db"

def init_database():
    """
    Inicializa o banco de dados com as tabelas necessárias
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Tabela de documentos gerados
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area TEXT NOT NULL,
            tipo_peca TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            dados_formulario TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            preview TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("✅ Banco de dados inicializado!")


def salvar_documento(area: str, tipo_peca: str, conteudo: str, dados_formulario: Dict) -> int:
    """
    Salva um documento gerado no histórico
    
    Args:
        area: Área do direito (criminal, civil, etc)
        tipo_peca: Nome da peça (queixa_crime, contestacao_civel, etc)
        conteudo: Conteúdo do documento gerado
        dados_formulario: Dados do formulário preenchido
    
    Returns:
        ID do documento inserido
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Criar preview (primeiros 100 caracteres)
    preview = conteudo[:100] if len(conteudo) > 100 else conteudo
    
    cursor.execute("""
        INSERT INTO documentos (area, tipo_peca, conteudo, dados_formulario, preview)
        VALUES (?, ?, ?, ?, ?)
    """, (
        area,
        tipo_peca,
        conteudo,
        json.dumps(dados_formulario, ensure_ascii=False),
        preview
    ))
    
    documento_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    print(f"✅ Documento salvo com ID: {documento_id}")
    return documento_id


def obter_historico(limite: int = 50) -> List[Dict]:
    """
    Retorna lista de documentos do histórico
    
    Args:
        limite: Número máximo de documentos a retornar
    
    Returns:
        Lista de dicionários com os documentos
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            id,
            area,
            tipo_peca,
            preview,
            data_criacao
        FROM documentos
        ORDER BY data_criacao DESC
        LIMIT ?
    """, (limite,))
    
    rows = cursor.fetchall()
    conn.close()
    
    historico = []
    for row in rows:
        historico.append({
            "id": row["id"],
            "area": row["area"],
            "tipo_peca": row["tipo_peca"],
            "preview": row["preview"],
            "data_criacao": row["data_criacao"]
        })
    
    return historico


def obter_documento(documento_id: int) -> Optional[Dict]:
    """
    Retorna um documento específico pelo ID
    
    Args:
        documento_id: ID do documento
    
    Returns:
        Dicionário com os dados do documento ou None se não encontrado
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT *
        FROM documentos
        WHERE id = ?
    """, (documento_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return None
    
    return {
        "id": row["id"],
        "area": row["area"],
        "tipo_peca": row["tipo_peca"],
        "conteudo": row["conteudo"],
        "dados_formulario": json.loads(row["dados_formulario"]) if row["dados_formulario"] else {},
        "data_criacao": row["data_criacao"]
    }


def deletar_documento(documento_id: int) -> bool:
    """
    Deleta um documento do histórico
    
    Args:
        documento_id: ID do documento a deletar
    
    Returns:
        True se deletado com sucesso, False se não encontrado
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM documentos WHERE id = ?", (documento_id,))
    
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    
    if linhas_afetadas > 0:
        print(f"✅ Documento {documento_id} deletado!")
        return True
    else:
        print(f"❌ Documento {documento_id} não encontrado!")
        return False


def limpar_historico():
    """
    Limpa todo o histórico de documentos (usar com cuidado!)
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM documentos")
    
    conn.commit()
    conn.close()
    
    print("⚠️ Todo o histórico foi limpo!")


# Inicializar banco ao importar o módulo
init_database()