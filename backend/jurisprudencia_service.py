import anthropic
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

# 🔥 PROMPT DESTRUIDOR - FORÇA IA A BUSCAR JURISPRUDÊNCIAS REAIS
PROMPT_JURISPRUDENCIA_REAL = """
🚨 ATENÇÃO: VOCÊ É UM ASSISTENTE JURÍDICO ESPECIALIZADO EM BUSCAR JURISPRUDÊNCIAS **REAIS E VERIFICÁVEIS**

⚖️ REGRAS ABSOLUTAS (QUEBRAR = ERRO GRAVE):

1. ✅ BUSQUE APENAS jurisprudências que EXISTEM nos tribunais brasileiros
2. ✅ USE web_search OBRIGATORIAMENTE para validar cada jurisprudência
3. ✅ NUNCA invente números de processos - eles devem ser REAIS
4. ✅ EXTRAIA ementas COMPLETAS (mínimo 150 palavras)
5. ✅ VALIDE se o tribunal existe (STF, STJ, TST, TRF, TRT, TJ-XX)
6. ✅ CONFIRME se o relator existe naquele tribunal
7. ✅ VERIFIQUE se a data é coerente (últimos 10 anos)

🔍 FONTES CONFIÁVEIS OBRIGATÓRIAS:
- jusbrasil.com.br
- stf.jus.br
- stj.jus.br
- tst.jus.br
- Sites oficiais dos TJs estaduais
- Consulta processual unificada (CNJ)

📋 FORMATO DE RESPOSTA (JSON OBRIGATÓRIO):
Retorne EXATAMENTE este formato:

{
  "jurisprudencias": [
    {
      "tribunal": "STJ",
      "numero_processo": "REsp 1.234.567/SP",
      "data_julgamento": "15/03/2023",
      "relator": "Ministro Paulo de Tarso Sanseverino",
      "orgao_julgador": "Terceira Turma",
      "ementa_completa": "[EMENTA COMPLETA COM MÍNIMO 150 PALAVRAS]",
      "fonte_verificacao": "https://www.stj.jus.br/...",
      "palavras_chave": ["responsabilidade civil", "dano moral"],
      "validado": true
    }
  ],
  "total_encontradas": 5,
  "criterios_busca": "dano moral atraso voo",
  "tribunais_consultados": ["STJ", "TJ-SP", "TRF-3"]
}

🎯 COMO BUSCAR (PASSO A PASSO):

1. ENTENDA O TEMA que o usuário pediu
2. BUSQUE no Google: "site:stj.jus.br [tema] ementa"
3. BUSQUE no Google: "site:jusbrasil.com.br [tema] jurisprudência"
4. BUSQUE no Google: "[tribunal] [tema] acórdão"
5. VALIDE cada resultado encontrado
6. EXTRAIA a ementa COMPLETA (não resuma!)
7. CONFIRME o número do processo
8. VERIFIQUE se o relator existe

⚠️ O QUE FAZER SE NÃO ENCONTRAR:
- NUNCA invente dados
- Retorne menos jurisprudências (mas todas REAIS)
- Amplie a busca para tribunais relacionados
- Busque jurisprudências similares verificáveis

🔥 QUALIDADE > QUANTIDADE:
- Prefira 3 jurisprudências REAIS do que 10 inventadas
- Ementas longas e completas são melhores que resumos
- Dados verificáveis > dados bonitos

💡 DICAS DE BUSCA AVANÇADA:
- Use operadores: site:stj.jus.br "dano moral" "atraso voo"
- Busque por número CNJ: NNNNNNN-DD.AAAA.J.TR.OOOO
- Valide relator no site do tribunal
- Confirme órgão julgador (turma, câmara)

🚨 ERROS QUE VOCÊ DEVE EVITAR:
❌ Inventar número de processo
❌ Criar relator fictício  
❌ Resumir ementa (ela deve ser COMPLETA)
❌ Não verificar fonte
❌ Tribunal inexistente
❌ Data impossível

✅ EXEMPLO DE BUSCA PERFEITA:

Tema: "rescisão contratual inadimplemento"

1. web_search: site:stj.jus.br rescisão contratual inadimplemento
2. web_search: site:tjsp.jus.br rescisão contratual 
3. web_search: jusbrasil rescisão contratual ementa completa

Resultado: 4 jurisprudências REAIS, ementas completas, dados validados.

🎯 AGORA EXECUTE:
"""

async def buscar_jurisprudencias_reais(tema: str, tipo_peca: str = "", area: str = "") -> dict:
    """
    🔥 BUSCA JURISPRUDÊNCIAS REAIS USANDO IA + WEB SEARCH
    
    Parâmetros:
    - tema: Tema da busca (ex: "dano moral atraso voo")
    - tipo_peca: Tipo da peça processual (opcional)
    - area: Área do direito (opcional)
    
    Retorna:
    - Dict com jurisprudências reais e verificadas
    """
    
    try:
        client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        # 🔥 CONTEXTO ADICIONAL PARA A IA
        contexto = f"""
TEMA DA BUSCA: {tema}
TIPO DE PEÇA: {tipo_peca or 'Não especificado'}
ÁREA DO DIREITO: {area or 'Não especificado'}

Com base nessas informações, busque jurisprudências que sejam:
- Relevantes para o tema
- Recentes (últimos 5 anos preferencialmente)
- De tribunais superiores (STF, STJ) ou tribunais estaduais relevantes
- Com ementas completas e detalhadas

IMPORTANTE: Use web_search para CADA jurisprudência que você for retornar!
Não retorne nada que você não tenha verificado através de busca na web.
        """
        
        print(f"🔍 Buscando jurisprudências reais sobre: {tema}")
        
        # 🔥 CHAMADA PARA A IA COM WEB SEARCH HABILITADO
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            system=PROMPT_JURISPRUDENCIA_REAL,
            tools=[
                {
                    "type": "web_search_20250305",
                    "name": "web_search"
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": contexto + "\n\nRETORNE APENAS O JSON. Não adicione texto antes ou depois."
                }
            ]
        )
        
        # 🔥 PROCESSAR RESPOSTA
        resposta_texto = ""
        for content in message.content:
            if content.type == "text":
                resposta_texto += content.text
        
        print(f"📄 Resposta da IA recebida")
        print(f"🔍 Preview: {resposta_texto[:500]}...")
        
        # 🔥 EXTRAIR JSON DA RESPOSTA
        # Remove markdown se houver
        resposta_limpa = resposta_texto.strip()
        
        # Tenta encontrar JSON na resposta
        json_match = re.search(r'\{[\s\S]*\}', resposta_limpa)
        if not json_match:
            print("⚠️ Não foi possível extrair JSON da resposta")
            return {
                "erro": "Formato de resposta inválido",
                "resposta_bruta": resposta_texto[:500]
            }
        
        json_str = json_match.group(0)
        resultado = json.loads(json_str)
        
        # 🔥 VALIDAÇÃO EXTRA
        if "jurisprudencias" not in resultado:
            return {
                "erro": "Nenhuma jurisprudência encontrada",
                "detalhes": "A IA não retornou jurisprudências válidas"
            }
        
        # 🔥 FILTRAR APENAS JURISPRUDÊNCIAS VALIDADAS
        jurisprudencias_validadas = [
            j for j in resultado["jurisprudencias"]
            if j.get("validado", False) and len(j.get("ementa_completa", "")) >= 150
        ]
        
        if len(jurisprudencias_validadas) == 0:
            return {
                "erro": "Nenhuma jurisprudência válida encontrada",
                "detalhes": "Todas as jurisprudências foram rejeitadas na validação"
            }
        
        print(f"✅ {len(jurisprudencias_validadas)} jurisprudências reais encontradas!")
        
        return {
            "sucesso": True,
            "jurisprudencias": jurisprudencias_validadas,
            "total": len(jurisprudencias_validadas),
            "tema_buscado": tema,
            "criterios": resultado.get("criterios_busca", tema),
            "tribunais_consultados": resultado.get("tribunais_consultados", [])
        }
        
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        return {
            "erro": "Erro ao processar resposta da IA",
            "detalhes": str(e)
        }
    
    except Exception as e:
        print(f"❌ Erro ao buscar jurisprudências: {e}")
        return {
            "erro": "Erro ao buscar jurisprudências",
            "detalhes": str(e)
        }


def formatar_jurisprudencia_abnt(jurisp: dict) -> str:
    """
    🔥 FORMATA JURISPRUDÊNCIA EM PADRÃO ABNT
    
    Retorna texto formatado pronto para inserir no documento
    """
    
    ementa = jurisp.get("ementa_completa", "")
    tribunal = jurisp.get("tribunal", "")
    numero = jurisp.get("numero_processo", "")
    relator = jurisp.get("relator", "")
    data = jurisp.get("data_julgamento", "")
    orgao = jurisp.get("orgao_julgador", "")
    
    # 🔥 FORMATAÇÃO ABNT PROFISSIONAL
    texto_formatado = f"""
═══════════════════════════════════════════════════════════════════

    {ementa}

    ({tribunal} - {numero}, Relator: {relator}, {orgao}, Data de Julgamento: {data})

═══════════════════════════════════════════════════════════════════
"""
    
    return texto_formatado


async def validar_jurisprudencia(jurisp: dict) -> bool:
    """
    🔥 VALIDAÇÃO EXTRA DE JURISPRUDÊNCIA
    
    Verifica se os dados fazem sentido
    """
    
    # Validações básicas
    campos_obrigatorios = ["tribunal", "numero_processo", "ementa_completa", "relator", "data_julgamento"]
    
    for campo in campos_obrigatorios:
        if not jurisp.get(campo):
            print(f"⚠️ Campo obrigatório ausente: {campo}")
            return False
    
    # Ementa deve ter pelo menos 150 caracteres
    if len(jurisp["ementa_completa"]) < 150:
        print(f"⚠️ Ementa muito curta: {len(jurisp['ementa_completa'])} caracteres")
        return False
    
    # Tribunal deve ser válido
    tribunais_validos = ["STF", "STJ", "TST", "TSE", "STM", "TRF", "TRT", "TJ"]
    tribunal_valido = any(t in jurisp["tribunal"].upper() for t in tribunais_validos)
    
    if not tribunal_valido:
        print(f"⚠️ Tribunal inválido: {jurisp['tribunal']}")
        return False
    
    # Número de processo deve ter formato válido
    # Formato CNJ: NNNNNNN-DD.AAAA.J.TR.OOOO
    numero = jurisp["numero_processo"]
    if not re.search(r'\d{7}[-.]?\d{2}[.]?\d{4}', numero):
        print(f"⚠️ Número de processo inválido: {numero}")
        return False
    
    print(f"✅ Jurisprudência validada: {jurisp['tribunal']} - {numero}")
    return True