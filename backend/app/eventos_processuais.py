

EVENTOS_POR_AREA = {
    "criminal": [
        {
            "id": "vitima_identificada",
            "label": "Vítima já está identificada?",
            "tipo": "boolean"
        },
        {
            "id": "fatos_documentados",
            "label": "Fatos criminosos já estão documentados (B.O., provas)?",
            "tipo": "boolean"
        },
        {
            "id": "processo_instaurado",
            "label": "Inquérito policial ou processo criminal já instaurado?",
            "tipo": "boolean"
        },
        {
            "id": "denuncia_recebida",
            "label": "Denúncia já foi recebida pelo juiz?",
            "tipo": "boolean"
        },
        {
            "id": "citacao_realizada",
            "label": "Réu já foi citado?",
            "tipo": "boolean"
        },
        {
            "id": "resposta_acusacao_apresentada",
            "label": "Resposta à acusação já foi apresentada?",
            "tipo": "boolean"
        },
        {
            "id": "audiencia_instrucao_realizada",
            "label": "Audiência de instrução já foi realizada?",
            "tipo": "boolean"
        },
        {
            "id": "sentenca_proferida",
            "label": "Sentença já foi proferida?",
            "tipo": "boolean"
        },
        {
            "id": "decisao_interlocutoria_existe",
            "label": "Existe decisão interlocutória para recorrer?",
            "tipo": "boolean"
        },
        {
            "id": "preso_provisoriamente",
            "label": "O réu está preso provisoriamente?",
            "tipo": "boolean"
        },
        {
            "id": "prisao_ilegal_existe",
            "label": "Há prisão ou constrangimento ilegal em curso?",
            "tipo": "boolean"
        }
    ],
    
    "trabalhista": [
        {
            "id": "vinculo_empregaticio_existe",
            "label": "Existe ou existiu vínculo empregatício?",
            "tipo": "boolean"
        },
        {
            "id": "verbas_nao_pagas",
            "label": "Existem verbas trabalhistas não pagas?",
            "tipo": "boolean"
        },
        {
            "id": "reclamacao_apresentada",
            "label": "Reclamação trabalhista já foi apresentada?",
            "tipo": "boolean"
        },
        {
            "id": "contestacao_apresentada",
            "label": "Contestação já foi apresentada pela reclamada?",
            "tipo": "boolean"
        },
        {
            "id": "audiencia_instrucao_realizada",
            "label": "Audiência de instrução já foi realizada?",
            "tipo": "boolean"
        },
        {
            "id": "sentenca_proferida",
            "label": "Sentença de 1º grau já foi proferida?",
            "tipo": "boolean"
        },
        {
            "id": "recurso_ordinario_interposto",
            "label": "Recurso ordinário já foi interposto?",
            "tipo": "boolean"
        },
        {
            "id": "acordao_trt_proferido",
            "label": "Acórdão do TRT já foi proferido?",
            "tipo": "boolean"
        }
    ],
    
    "civil": [
        {
            "id": "conflito_juridico_existe",
            "label": "Existe conflito/problema jurídico a resolver?",
            "tipo": "boolean"
        },
        {
            "id": "tentativa_extrajudicial",
            "label": "Já houve tentativa de resolução extrajudicial?",
            "tipo": "boolean"
        },
        {
            "id": "processo_existe",
            "label": "Já existe processo judicial em andamento?",
            "tipo": "boolean"
        },
        {
            "id": "citacao_realizada",
            "label": "Réu já foi citado?",
            "tipo": "boolean"
        },
        {
            "id": "contestacao_apresentada",
            "label": "Contestação já foi apresentada?",
            "tipo": "boolean"
        },
        {
            "id": "pericia_realizada",
            "label": "Perícia já foi realizada?",
            "tipo": "boolean"
        },
        {
            "id": "instrucao_probatoria_realizada",
            "label": "Instrução probatória já foi realizada?",
            "tipo": "boolean"
        },
        {
            "id": "sentenca_proferida",
            "label": "Sentença de 1º grau já foi proferida?",
            "tipo": "boolean"
        },
        {
            "id": "sentenca_transitada",
            "label": "Sentença já transitou em julgado?",
            "tipo": "boolean"
        },
        {
            "id": "decisao_interlocutoria_existe",
            "label": "Existe decisão interlocutória para agravar?",
            "tipo": "boolean"
        },
        {
            "id": "recurso_interposto",
            "label": "Recurso (apelação/agravo) já foi interposto?",
            "tipo": "boolean"
        },
        {
            "id": "acordao_tj_proferido",
            "label": "Acórdão do TJ já foi proferido?",
            "tipo": "boolean"
        },
        {
            "id": "execucao_iniciada",
            "label": "Fase de execução já foi iniciada?",
            "tipo": "boolean"
        },
        {
            "id": "bens_penhorados",
            "label": "Bens já foram penhorados?",
            "tipo": "boolean"
        },
        {
            "id": "decisao_monocratica_existe",
            "label": "Existe decisão monocrática para agravar internamente?",
            "tipo": "boolean"
        },
        {
            "id": "resp_negado_admissibilidade",
            "label": "Recurso Especial teve admissibilidade negada?",
            "tipo": "boolean"
        },
        {
            "id": "ato_autoridade_existe",
            "label": "Existe ato de autoridade violando direito líquido e certo?",
            "tipo": "boolean"
        }
    ],
    
    "previdenciario": [
        {
            "id": "tempo_contribuicao_suficiente",
            "label": "Tempo de contribuição ou carência já foi cumprido?",
            "tipo": "boolean"
        },
        {
            "id": "requerimento_administrativo_feito",
            "label": "Requerimento administrativo no INSS já foi feito?",
            "tipo": "boolean"
        },
        {
            "id": "beneficio_indeferido",
            "label": "Benefício foi indeferido administrativamente?",
            "tipo": "boolean"
        },
        {
            "id": "beneficio_concedido",
            "label": "Benefício já foi concedido?",
            "tipo": "boolean"
        },
        {
            "id": "beneficio_incorreto",
            "label": "Benefício foi concedido com valor/cálculo incorreto?",
            "tipo": "boolean"
        },
        {
            "id": "processo_judicial_existe",
            "label": "Já existe ação judicial em andamento?",
            "tipo": "boolean"
        },
        {
            "id": "sentenca_proferida",
            "label": "Sentença já foi proferida?",
            "tipo": "boolean"
        }
    ],
    
    "contratos": [
        {
            "id": "partes_definidas",
            "label": "As partes contratantes estão definidas?",
            "tipo": "boolean"
        },
        {
            "id": "objeto_contrato_definido",
            "label": "O objeto/finalidade do contrato está claro?",
            "tipo": "boolean"
        },
        {
            "id": "acordo_verbal_existe",
            "label": "Já existe acordo verbal entre as partes?",
            "tipo": "boolean"
        },
        {
            "id": "plataforma_digital_existe",
            "label": "Trata-se de plataforma digital/serviço online?",
            "tipo": "boolean"
        }
    ]
}


# ====================================================================
#            REGRAS DE DEPENDÊNCIA (BLOQUEIO DE PEÇAS)
#                    ✅ TODAS AS 46 PEÇAS
# ====================================================================

REGRAS_DEPENDENCIA = {
    # ==================== CRIMINAL (7 PEÇAS) ====================
    
    "queixa_crime": {
        "eventos_requeridos": ["vitima_identificada", "fatos_documentados"],
        "mensagem": "Para apresentar Queixa-Crime é necessário que a vítima esteja identificada e os fatos criminosos documentados.",
        "peças_iniciais": True  # Pode ser a primeira peça
    },
    
    "resposta_acusacao": {
        "eventos_requeridos": ["denuncia_recebida", "citacao_realizada"],
        "mensagem": "Para apresentar Resposta à Acusação é necessário que a denúncia já tenha sido recebida e o réu citado."
    },
    
    "habeas_corpus": {
        "eventos_requeridos": ["prisao_ilegal_existe"],
        "mensagem": "Habeas Corpus só cabe quando há prisão ou constrangimento ilegal.",
        "peças_iniciais": True  # Pode ser a primeira peça judicial
    },
    
    "alegacoes_finais_criminais": {
        "eventos_requeridos": ["audiencia_instrucao_realizada"],
        "mensagem": "Alegações finais só podem ser apresentadas após a audiência de instrução."
    },
    
    "apelacao_criminal": {
        "eventos_requeridos": ["sentenca_proferida"],
        "mensagem": "Apelação só pode ser interposta após a sentença ser proferida."
    },
    
    "recurso_sentido_estrito": {
        "eventos_requeridos": ["decisao_interlocutoria_existe"],
        "mensagem": "Recurso em Sentido Estrito só cabe contra decisões interlocutórias específicas (art. 581, CPP)."
    },
    
    "pedido_liberdade_provisoria": {
        "eventos_requeridos": ["preso_provisoriamente"],
        "mensagem": "Pedido de liberdade provisória só é cabível se o réu estiver preso provisoriamente."
    },
    
    # ==================== TRABALHISTA (6 PEÇAS) ====================
    
    "reclamacao_trabalhista": {
        "eventos_requeridos": ["vinculo_empregaticio_existe", "verbas_nao_pagas"],
        "mensagem": "Reclamação trabalhista requer vínculo empregatício e verbas não pagas.",
        "peças_iniciais": True
    },
    
    "contestacao_trabalhista": {
        "eventos_requeridos": ["reclamacao_apresentada"],
        "mensagem": "Contestação só pode ser apresentada após a reclamação trabalhista."
    },
    
    "impugnacao_contestacao_trabalhista": {
        "eventos_requeridos": ["contestacao_apresentada"],
        "mensagem": "Impugnação à contestação só pode ser feita após a contestação ser apresentada."
    },
    
    "recurso_ordinario_trabalhista": {
        "eventos_requeridos": ["sentenca_proferida"],
        "mensagem": "Recurso ordinário só pode ser interposto após a sentença."
    },
    
    "contrarrazoes_recurso_ordinario": {
        "eventos_requeridos": ["recurso_ordinario_interposto"],
        "mensagem": "Contrarrazões só podem ser apresentadas após o recurso ordinário ser interposto."
    },
    
    "recurso_revista": {
        "eventos_requeridos": ["acordao_trt_proferido"],
        "mensagem": "Recurso de Revista só cabe após o acórdão do TRT."
    },
    
    # ==================== CÍVEL (26 PEÇAS) ====================
    
    "peticao_inicial": {
        "eventos_requeridos": ["conflito_juridico_existe"],
        "mensagem": "Petição inicial inicia o processo judicial.",
        "peças_iniciais": True
    },
    
    "contestacao_civel": {
        "eventos_requeridos": ["processo_existe", "citacao_realizada"],
        "mensagem": "Contestação só pode ser apresentada após a citação do réu."
    },
    
    "impugnacao_contestacao": {
        "eventos_requeridos": ["contestacao_apresentada"],
        "mensagem": "Impugnação à contestação só pode ser feita após a contestação."
    },
    
    "alegacoes_finais_civel": {
        "eventos_requeridos": ["instrucao_probatoria_realizada"],
        "mensagem": "Alegações finais só podem ser apresentadas após a instrução probatória."
    },
    
    "apelacao_civel": {
        "eventos_requeridos": ["sentenca_proferida"],
        "mensagem": "Apelação só pode ser interposta após a sentença."
    },
    
    "contrarrazoes_apelacao": {
        "eventos_requeridos": ["recurso_interposto"],
        "mensagem": "Contrarrazões só podem ser apresentadas após a apelação ser interposta."
    },
    
    "contrarrazoes_recurso_inominado": {
        "eventos_requeridos": ["recurso_interposto"],
        "mensagem": "Contrarrazões ao recurso inominado só cabem após sua interposição."
    },
    
    "contrarrazoes_embargos_declaracao": {
        "eventos_requeridos": ["recurso_interposto"],
        "mensagem": "Contrarrazões aos embargos de declaração só cabem após sua oposição."
    },
    
    "agravo_instrumento": {
        "eventos_requeridos": ["decisao_interlocutoria_existe"],
        "mensagem": "Agravo de instrumento só cabe contra decisões interlocutórias."
    },
    
    "contraminuta_agravo": {
        "eventos_requeridos": ["recurso_interposto"],
        "mensagem": "Contraminuta só pode ser apresentada após a interposição do agravo."
    },
    
    "embargos_declaracao": {
        "eventos_requeridos": ["sentenca_proferida"],
        "mensagem": "Embargos de declaração cabem contra sentenças/acórdãos com omissão, contradição ou obscuridade."
    },
    
    "recurso_especial": {
        "eventos_requeridos": ["acordao_tj_proferido"],
        "mensagem": "Recurso Especial só cabe após o acórdão do Tribunal de Justiça."
    },
    
    "mandado_seguranca": {
        "eventos_requeridos": ["ato_autoridade_existe"],
        "mensagem": "Mandado de Segurança cabe contra ato de autoridade que viola direito líquido e certo.",
        "peças_iniciais": True
    },
    
    "recurso_inominado": {
        "eventos_requeridos": ["sentenca_proferida"],
        "mensagem": "Recurso inominado cabe contra sentenças de Juizados Especiais."
    },
    
    "cumprimento_sentenca": {
        "eventos_requeridos": ["sentenca_transitada"],
        "mensagem": "Cumprimento de sentença só pode ser iniciado após o trânsito em julgado."
    },
    
    "impugnacao_cumprimento": {
        "eventos_requeridos": ["execucao_iniciada"],
        "mensagem": "Impugnação ao cumprimento de sentença só cabe após o início da execução."
    },
    
    "embargos_execucao": {
        "eventos_requeridos": ["execucao_iniciada"],
        "mensagem": "Embargos à execução só podem ser opostos após o início da execução."
    },
    
    "manifestacao_processual": {
        "eventos_requeridos": ["processo_existe"],
        "mensagem": "Manifestação processual requer processo em andamento."
    },
    
    "impugnacao_embargos": {
        "eventos_requeridos": ["recurso_interposto"],
        "mensagem": "Impugnação aos embargos à execução só cabe após sua oposição."
    },
    
    "impugnacao_laudo": {
        "eventos_requeridos": ["pericia_realizada"],
        "mensagem": "Impugnação ao laudo só cabe após a perícia ser realizada."
    },
    
    "agravo_interno": {
        "eventos_requeridos": ["decisao_monocratica_existe"],
        "mensagem": "Agravo interno só cabe contra decisão monocrática de relator."
    },
    
    "excecao_pre_executividade": {
        "eventos_requeridos": ["execucao_iniciada"],
        "mensagem": "Exceção de pré-executividade cabe na fase de execução."
    },
    
    "agravo_recurso_especial": {
        "eventos_requeridos": ["resp_negado_admissibilidade"],
        "mensagem": "Agravo em Recurso Especial só cabe quando o REsp teve admissibilidade negada."
    },
    
    "contrarrazoes_recurso_especial": {
        "eventos_requeridos": ["recurso_interposto"],
        "mensagem": "Contrarrazões ao REsp só cabem após sua interposição."
    },
    
    "embargos_terceiro": {
        "eventos_requeridos": ["bens_penhorados"],
        "mensagem": "Embargos de terceiro só cabem quando há constrição de bens de terceiro."
    },
    
    "notificacao_extrajudicial": {
        "eventos_requeridos": ["conflito_juridico_existe"],
        "mensagem": "Notificação extrajudicial pode ser feita antes ou durante o processo.",
        "peças_iniciais": True  # Pode ser pré-processual
    },
    
    # ==================== PREVIDENCIÁRIO (5 PEÇAS) ====================
    
    "requerimento_beneficio_administrativo": {
        "eventos_requeridos": ["tempo_contribuicao_suficiente"],
        "mensagem": "Requerimento administrativo requer tempo de contribuição/carência.",
        "peças_iniciais": True
    },
    
    "recurso_previdenciario_administrativo": {
        "eventos_requeridos": ["beneficio_indeferido"],
        "mensagem": "Recurso administrativo só cabe após o indeferimento do benefício."
    },
    
    "revisao_beneficio_administrativo": {
        "eventos_requeridos": ["beneficio_concedido", "beneficio_incorreto"],
        "mensagem": "Revisão administrativa só cabe para benefícios já concedidos com erro."
    },
    
    "acao_concessao_beneficio": {
        "eventos_requeridos": ["beneficio_indeferido"],
        "mensagem": "Ação de concessão de benefício geralmente é proposta após indeferimento administrativo.",
        "peças_iniciais": True  # Em relação ao processo judicial
    },
    
    "acao_revisao_beneficio": {
        "eventos_requeridos": ["beneficio_concedido", "beneficio_incorreto"],
        "mensagem": "Ação de revisão só cabe para benefícios já concedidos com cálculo incorreto.",
        "peças_iniciais": True  # Em relação ao processo judicial
    },
    
    # ==================== CONTRATOS (2 PEÇAS) ====================
    
    "contrato": {
        "eventos_requeridos": ["partes_definidas", "objeto_contrato_definido"],
        "mensagem": "Contrato requer partes e objeto definidos.",
        "peças_iniciais": True  # Documento extrajudicial
    },
    
    "termos_uso": {
        "eventos_requeridos": ["plataforma_digital_existe"],
        "mensagem": "Termos de Uso são necessários para plataformas digitais/serviços online.",
        "peças_iniciais": True  # Documento extrajudicial
    }
}


# ====================================================================
#              FUNÇÃO DE VERIFICAÇÃO DE BLOQUEIO
# ====================================================================

def verificar_pode_gerar_peca(peca_id: str, eventos_informados: dict) -> dict:
    """
    Verifica se uma peça pode ser gerada baseado nos eventos informados
    
    Args:
        peca_id: ID da peça (ex: "resposta_acusacao")
        eventos_informados: Dict com eventos {evento_id: True/False}
    
    Returns:
        {
            "pode_gerar": bool,
            "bloqueada": bool,
            "motivo": str,
            "eventos_faltantes": list,
            "e_peca_inicial": bool
        }
    """
    
    # Se não há regra de dependência, pode gerar
    if peca_id not in REGRAS_DEPENDENCIA:
        return {
            "pode_gerar": True,
            "bloqueada": False,
            "motivo": "",
            "eventos_faltantes": [],
            "e_peca_inicial": False
        }
    
    regra = REGRAS_DEPENDENCIA[peca_id]
    eventos_requeridos = regra["eventos_requeridos"]
    e_peca_inicial = regra.get("peças_iniciais", False)
    
    # Verificar se todos os eventos requeridos estão TRUE
    eventos_faltantes = []
    for evento_id in eventos_requeridos:
        if not eventos_informados.get(evento_id, False):
            eventos_faltantes.append(evento_id)
    
    if eventos_faltantes:
        return {
            "pode_gerar": False,
            "bloqueada": True,
            "motivo": regra["mensagem"],
            "eventos_faltantes": eventos_faltantes,
            "e_peca_inicial": e_peca_inicial
        }
    
    return {
        "pode_gerar": True,
        "bloqueada": False,
        "motivo": "",
        "eventos_faltantes": [],
        "e_peca_inicial": e_peca_inicial
    }


# ====================================================================
#          FUNÇÃO PARA OBTER EVENTOS DE UMA ÁREA
# ====================================================================

def obter_eventos_area(area_id: str) -> list:
    """
    Retorna lista de eventos processuais para uma área específica
    
    Args:
        area_id: ID da área (ex: "criminal", "civil", "trabalhista")
    
    Returns:
        Lista de eventos com id, label e tipo
    """
    return EVENTOS_POR_AREA.get(area_id, [])


# ====================================================================
#        FUNÇÃO PARA LISTAR PEÇAS INICIAIS (SEM PROCESSO)
# ====================================================================

def obter_pecas_iniciais(area_id: str) -> list:
    """
    Retorna lista de IDs de peças que podem ser geradas sem processo existente
    
    Args:
        area_id: ID da área
    
    Returns:
        Lista de peca_ids que são iniciais
    """
    pecas_iniciais = []
    
    for peca_id, regra in REGRAS_DEPENDENCIA.items():
        if regra.get("peças_iniciais", False):
            pecas_iniciais.append(peca_id)
    
    return pecas_iniciais