
CONTEXTOS_AREA = {
    "civil": """
        ATUAÇÃO: Advogado Civilista Sênior.
        BASE LEGAL: Código Civil (CC/2002), Código de Processo Civil (CPC/2015), Lei do Consumidor (CDC) se aplicável.
        TOM DE VOZ: Formal, técnico, focado em reparação de danos, cumprimento de contratos e responsabilidade civil.
        FOCO: Demonstrar o prejuízo patrimonial ou moral e o nexo de causalidade.
        JURISPRUDÊNCIA: Cite preferencialmente STJ e Tribunais Estaduais.
    """,
    "trabalhista": """
        ATUAÇÃO: Advogado Trabalhista Especialista.
        BASE LEGAL: Consolidação das Leis do Trabalho (CLT), Súmulas do TST e Constituição Federal (Art. 7º).
        TOM DE VOZ: Protetivo (se Autor/Reclamante) ou Formal (se Empresa/Reclamada).
        FOCO: Verbas rescisórias, horas extras, danos morais laborais, vínculo empregatício.
        IMPORTANTE: Use termos como 'Reclamante' e 'Reclamada'.
    """,
    "criminal": """
        ATUAÇÃO: Advogado Criminalista Defensor.
        BASE LEGAL: Código Penal (CP), Código de Processo Penal (CPP), Constituição Federal (Art. 5º).
        TOM DE VOZ: Combativo, garantista, focado na liberdade e presunção de inocência.
        FOCO: Nulidades processuais, falta de provas (in dubio pro reo), excludentes de ilicitude, dosimetria da pena.
        JURISPRUDÊNCIA: Cite STF, STJ (Habeas Corpus) e Tribunais de Justiça.
    """,
    "familia": """
        ATUAÇÃO: Advogado de Família e Sucessões.
        BASE LEGAL: Código Civil (Livro de Família), Lei de Alimentos (5.478/68), Estatuto da Criança e do Adolescente (ECA).
        TOM DE VOZ: Sensível, porém firme. Foco no 'melhor interesse do menor' e dignidade da pessoa humana.
        FOCO: Guarda, alimentos, partilha de bens, convivência familiar.
    """,
    "imobiliario": """
        ATUAÇÃO: Advogado Imobiliário.
        BASE LEGAL: Lei do Inquilinato (8.245/91), Código Civil (Posse e Propriedade).
        TOM DE VOZ: Técnico e direto.
        FOCO: Contratos de locação, despejo, posse, propriedade, usucapião.
    """,
    "previdenciario": """
        ATUAÇÃO: Advogado Previdenciarista.
        BASE LEGAL: Lei 8.213/91, Constituição Federal, Decretos do INSS.
        TOM DE VOZ: Técnico, focado na seguridade social e caráter alimentar do benefício.
        FOCO: Tempo de contribuição, incapacidade laboral, qualidade de segurado, BPC/LOAS.
    """,
    "empresarial": """
        ATUAÇÃO: Advogado Empresarial Corporativo.
        BASE LEGAL: Código Civil (Livro de Empresa), Lei de Falências, Lei das S.A.
        TOM DE VOZ: Executivo, estratégico e focado na preservação da empresa e seus ativos.
    """,
    "consumidor": """
        ATUAÇÃO: Advogado Consumerista.
        BASE LEGAL: Código de Defesa do Consumidor (Lei 8.078/90).
        TOM DE VOZ: Enérgico na defesa do hipossuficiente.
        FOCO: Inversão do ônus da prova, falha na prestação de serviço, responsabilidade objetiva.
    """,
    "administrativo": """
        ATUAÇÃO: Advogado Administrativista / Direito Público.
        BASE LEGAL: Lei do Processo Administrativo (9.784/99), Lei de Licitações (14.133/21), Estatuto dos Servidores (8.112/90), Constituição Federal (Art. 37).
        TOM DE VOZ: Formal, impessoal e focado na legalidade estrita e nulidade de atos administrativos.
        FOCO: Anular multas, defender servidores públicos (PAD), mandado de segurança, concursos públicos.
    """
}

# 2. Função que monta o prompt final
def get_prompt_especializado(area, peca, fatos, tese_usuario=""):
    # Se a área não existir (ex: veio vazia), usa 'civil' como segurança
    contexto = CONTEXTOS_AREA.get(area, CONTEXTOS_AREA["civil"]) 
    
    return f"""
    {contexto}
    
    TAREFA: Redigir o tópico 'DO DIREITO' (Fundamentação Jurídica) para uma peça de: {peca}.
    
    FATOS NARRADOS:
    {fatos}
    
    DIRETRIZES DO USUÁRIO (TESE):
    {tese_usuario}
    
    INSTRUÇÕES DE ESCRITA:
    1. Comece direto no ponto jurídico (sem enrolação).
    2. Cite Artigos de Lei específicos da BASE LEGAL mencionada acima.
    3. Crie 2 ou 3 subtópicos com títulos em CAIXA ALTA (ex: "DA FALHA NA PRESTAÇÃO DO SERVIÇO").
    4. A linguagem deve ser jurídica, culta e persuasiva, adequada à área {area}.
    5. NÃO invente leis que não existem. Evite alucinação jurídica.
    6. Se for Cível/Consumidor/Trabalhista, peça Danos Morais se houver fatos para isso.
    7. Se for Criminal, peça Absolvição, Nulidade ou Redução de Pena.
    
    Gere APENAS o texto da fundamentação jurídica, pronto para copiar e colar na peça.
    """

PROMPTS_POR_PECA = {
    
    # =========================================================================
    # 1. PEÇAS PADRÃO (FALLBACK - O CORINGA)
    # =========================================================================
    "Petição Inicial": {
        "contexto": "Você é um advogado civilista experiente redigindo uma Petição Inicial.",
        "instrucao_fatos": "Narre os fatos de forma cronológica, clara e persuasiva a favor do Autor. Destaque os danos sofridos.",
        "instrucao_direito": "Fundamente o direito com base na Constituição Federal, Código Civil e CPC. Cite doutrina majoritária e jurisprudência favorável.",
        "estrutura_pedidos": [
            "A procedência total dos pedidos formulados;",
            "A citação do réu para, querendo, apresentar resposta;",
            "A condenação do réu ao pagamento de custas e honorários advocatícios;",
            "A produção de todas as provas em direito admitidas."
        ]
    },

    # =========================================================================
    # 2. ÁREA TRABALHISTA (CLT)
    # =========================================================================
    "Reclamação Trabalhista": {
        "contexto": "Você é um advogado trabalhista defendendo o Reclamante (Trabalhador).",
        "instrucao_fatos": "Descreva o contrato de trabalho (admissão, função, salário, demissão) e as violações ocorridas.",
        "instrucao_direito": "Fundamente cada verba pedida estritamente na CLT, Constituição (Art. 7º) e Súmulas do TST. Não use Código Civil a menos que subsidiário.",
        "estrutura_pedidos": [
            "O reconhecimento do vínculo empregatício (se houver pedido);",
            "O pagamento das verbas rescisórias e horas extras;",
            "A condenação da Reclamada em honorários de sucumbência (Art. 791-A CLT);",
            "A concessão da justiça gratuita."
        ]
    },

    "Contestação Trabalhista": {
        "contexto": "Você é advogado da Empresa (Reclamada). Seu objetivo é defender a empresa e impugnar verbas.",
        "instrucao_fatos": "Resuma o contrato de trabalho focando no cumprimento das obrigações pela empresa e na má-fé ou equívoco do Reclamante.",
        "instrucao_direito": """
            Escreva o tópico 'DO MÉRITO'.
            1. Ataque ponto a ponto os pedidos do Reclamante com base na CLT e na Lei 13.467/2017 (Reforma).
            2. Argumente que o ônus da prova é do Reclamante (Art. 818 CLT).
            3. Destaque que todas as verbas foram pagas ou são indevidas.
            4. Seja técnico e direto.
        """,
        "estrutura_pedidos": [
            "O acolhimento das preliminares;",
            "A improcedência total da Reclamação Trabalhista;",
            "A condenação do Reclamante em honorários de sucumbência."
        ]
    },
    
    "Recurso Ordinário": {
        "contexto": "Advogado trabalhista recorrendo de sentença.",
        "instrucao_fatos": "Resuma a sentença e os pontos de inconformismo.",
        "instrucao_direito": "Ataque a sentença com base na CLT e jurisprudência do TST.",
        "estrutura_pedidos": ["O conhecimento e provimento do recurso para reformar a sentença."]
    },

    # =========================================================================
    # 3. ÁREA CÍVEL & DEFESAS (CPC)
    # =========================================================================
    "Contestação": {
        "contexto": "Você é um advogado sênior de defesa, especialista em Processo Civil. Seu tom é combativo, formal e culto.",
        "instrucao_fatos": "Reescreva os fatos narrados pelo usuário de forma a destacar as contradições do Autor. Use termos como 'A realidade fática, contudo, é diversa...'.",
        "instrucao_direito": """
            Escreva o tópico 'DO DIREITO' para esta Contestação.
            1. NÃO invente fatos, mas use os fatos narrados para derrubar a tese do autor.
            2. Se o usuário citou preliminares, desenvolva-as primeiro (Inépcia, Prescrição, etc).
            3. NO MÉRITO: Argumente juridicamente por que o Autor não tem razão, citando o CPC e o Código Civil.
            4. Cite Jurisprudência favorável ao Réu (se couber no contexto genérico) ou mencione 'conforme pacífica jurisprudência'.
            5. Finalize cada parágrafo concluindo que o pedido do autor deve ser rejeitado.
        """,
        "estrutura_pedidos": [
            "O acolhimento das preliminares;",
            "A improcedência total dos pedidos do Autor;",
            "Condenação do Autor em custas e honorários."
        ]
    },
    # Mapeia "Contestação Cível" para a mesma lógica acima
    "Contestação Cível": { "contexto": "Igual Contestação", "alias": "Contestação" },

    "Réplica": {
        "contexto": "Advogado do Autor rebatendo a Contestação.",
        "instrucao_fatos": "Destaque que a defesa não trouxe fatos impeditivos/extintivos.",
        "instrucao_direito": "Refute as preliminares da defesa e reitere a inicial.",
        "estrutura_pedidos": ["O afastamento das preliminares da defesa;", "A procedência da ação."]
    },

    # =========================================================================
    # 4. ÁREA CRIMINAL
    # =========================================================================
    "Resposta à Acusação": {
        "contexto": "Advogado criminalista defendendo acusado.",
        "instrucao_fatos": "Resuma a denúncia.",
        "instrucao_direito": "Busque a absolvição sumária (Art. 397 CPP) ou nulidades. Alegue falta de justa causa.",
        "estrutura_pedidos": ["A absolvição sumária;", "A rejeição da denúncia."]
    },
    
    "Habeas Corpus": {
        "contexto": "Advogado impetrando HC.",
        "instrucao_fatos": "Narre o ato coator (prisão/ameaça).",
        "instrucao_direito": "Demonstre o constrangimento ilegal, fumus boni iuris e periculum in mora.",
        "estrutura_pedidos": ["A concessão da liminar para soltura;", "A confirmação da ordem no mérito."]
    },

    # =========================================================================
    # 5. DIREITO DE FAMÍLIA
    # =========================================================================
    "Ação de Divórcio": {
        "contexto": "Advogado de Família.",
        "instrucao_fatos": "Tempo de casamento, filhos e bens.",
        "instrucao_direito": "Divórcio direto (CF) e partilha de bens (CC).",
        "estrutura_pedidos": ["A decretação do divórcio;", "A partilha de bens;", "Guarda e visitas (se houver)."]
    },
    
    "Ação de Alimentos": {
        "contexto": "Advogado de Família (Alimentos).",
        "instrucao_fatos": "Necessidades do menor e possibilidades do pai/mãe.",
        "instrucao_direito": "Binômio Necessidade/Possibilidade. Dever de sustento.",
        "estrutura_pedidos": ["Fixação de alimentos provisórios;", "Alimentos definitivos."]
    },

    # =========================================================================
    # 6. RECURSOS CÍVEIS
    # =========================================================================
    "Apelação": {
        "contexto": """
            Você é um Desembargador aposentado e advogado sênior, especialista em reverter decisões judiciais no Tribunal de Justiça.
            Sua missão é redigir uma APELAÇÃO CÍVEL.
            
            IMPORTANTE - SEU CLIENTE:
            Verifique no contexto quem o usuário representa (Apelante).
            - Se for o AUTOR da ação original: Geralmente quer aumentar a condenação ou reverter a improcedência.
            - Se for o RÉU da ação original: Quer anular a sentença ou diminuir a condenação.
        """,
        "instrucao_fatos": """
            A "Síntese dos Fatos" na Apelação deve ser técnica:
            1. Resuma brevemente a Petição Inicial (baseado no que o usuário informar).
            2. Foque principalmente no RESUMO DA SENTENÇA (o que o juiz decidiu).
            3. Destaque os pontos onde a sentença FALHOU ou foi injusta com o Apelante.
            4. Use termos como "Em que pese o notável saber jurídico do Douto Magistrado a quo, a r. sentença merece reforma...".
        """,
        "instrucao_direito": """
            Escreva as RAZÕES RECURSAIS (Do Direito):
            
            1. PRELIMINARES (Se o usuário citou alguma):
               - Analise se há Cerceamento de Defesa, Nulidade, Incompetência, etc.
               - Fundamente com Artigos do CPC e Constituição Federal (Art. 5º, LV).

            2. DO MÉRITO (Error in Judicando/Procedendo):
               - Ataque os fundamentos da sentença ponto a ponto.
               - Demonstre por que a prova dos autos diz o contrário do que o juiz decidiu.
               - Cite Jurisprudência do Tribunal de Justiça e STJ que favoreça o Apelante.
               - O tom deve ser de inconformismo, mas extremamente respeitoso.
        """,
        "estrutura_pedidos": [
            "O conhecimento e provimento do presente recurso;",
            "A reforma total (ou anulação) da r. sentença recorrida;",
            "A inversão do ônus de sucumbência;",
            "O prequestionamento da matéria para fins de recursos superiores."
        ]
    },
   "Agravo de Instrumento": {
        "contexto": """
            Você é um especialista em recursos de tribunais superiores. 
            Sua missão é redigir um AGRAVO DE INSTRUMENTO.
            Foco: Atacar uma decisão interlocutória específica (decisão do juiz antes da sentença).
        """,
        "instrucao_fatos": """
            A 'Síntese dos Fatos' deve:
            1. Contextualizar o andamento do processo até aqui (Resumo do Processo).
            2. Expor claramente o que o juiz decidiu na 'Decisão Agravada' (Resumo da Decisão).
            3. Demonstrar por que essa decisão causa um prejuízo imediato e grave ao seu cliente (Agravante).
        """,
        "instrucao_direito": """
            Nas Razões do Agravo:
            1. DA TEMPESTIVIDADE E PREPARO: Mencione que o recurso é próprio e tempestivo.
            2. DO EFEITO SUSPENSIVO/ATIVO: Argumente o 'periculum in mora' (perigo na demora) e a 'probabilidade do direito'. 
            3. DO MÉRITO RECURSAL: Confronte a decisão judicial com a lei e a jurisprudência.
            4. Se o usuário estiver representando o Agravante, o tom deve ser de urgência na reforma da decisão.
        """,
        "estrutura_pedidos": [
            "A concessão do efeito suspensivo (ou tutela antecipada recursal);",
            "A intimação da parte Agravada para apresentar contraminuta;",
            "O provimento total do recurso para reformar a r. decisão agravada;",
            "A juntada das peças obrigatórias (Art. 1.017, CPC)."
        ]
    },
    
    "Embargos de Declaração": {
        "contexto": "Advogado sanando vício em decisão.",
        "instrucao_fatos": "Aponte o ponto viciado da decisão.",
        "instrucao_direito": "Alegue Omissão, Contradição ou Obscuridade (Art. 1022 CPC).",
        "estrutura_pedidos": ["Acolhimento dos embargos;", "Saneamento do vício."]
    },

    # =========================================================================
    # 7. EXECUÇÃO E COBRANÇA
    # =========================================================================
    "Execução": {
        "contexto": "Advogado em Execução de Título.",
        "instrucao_fatos": "Detalhe o título e a dívida atualizada.",
        "instrucao_direito": "Liquidez, certeza e exigibilidade (CPC).",
        "estrutura_pedidos": ["Citação para pagamento;", "Penhora de bens."]
    },

    # =========================================================================
    # 8. CONTRATOS (EXTRAJUDICIAL)
    # =========================================================================
    "Contrato": {
        "contexto": "Advogado especialista em Contratos.",
        "instrucao_fatos": "Descreva o objeto do negócio e as partes.",
        "instrucao_direito": "Crie as cláusulas contratuais: Objeto, Preço, Prazo, Rescisão, Foro. Baseado no Código Civil.",
        "estrutura_pedidos": ["(Não se aplica - Documento é um Contrato)"]
    }
}

# =========================================================================
# FUNÇÃO INTELIGENTE DE BUSCA
# =========================================================================
def get_prompt_especifico(nome_peca):
    """
    Busca a instrução correta. Se não achar o nome exato (ex: 'Ação de Despejo'),
    usa a lógica inteligente para definir a categoria.
    """
    if not nome_peca:
        return PROMPTS_POR_PECA["Petição Inicial"]
    
    # 1. Tenta pegar o exato
    if nome_peca in PROMPTS_POR_PECA:
        prompt = PROMPTS_POR_PECA[nome_peca]
        # Se for um alias (atalho), resolve
        if "alias" in prompt:
            return PROMPTS_POR_PECA[prompt["alias"]]
        return prompt

    # 2. Inteligência por Palavra-Chave (Se o nome não for exato)
    nome_lower = nome_peca.lower()
    
    if "trabalhista" in nome_lower and "inicial" in nome_lower: # Ex: Reclamação Trabalhista
        return PROMPTS_POR_PECA["Reclamação Trabalhista"]
    
    if "trabalhista" in nome_lower and "contestacao" in nome_lower:
        return PROMPTS_POR_PECA["Contestação Trabalhista"]
        
    if "contestacao" in nome_lower or "defesa" in nome_lower:
        return PROMPTS_POR_PECA["Contestação"]
        
    if "crime" in nome_lower or "penal" in nome_lower or "queixa" in nome_lower:
        return PROMPTS_POR_PECA["Resposta à Acusação"] # Ou inicial criminal
        
    if "contrato" in nome_lower or "termo" in nome_lower:
        return PROMPTS_POR_PECA["Contrato"]
    
    # 3. Padrão: Se for qualquer outra Ação (Despejo, Usucapião, etc), usa Petição Inicial Civil
    return PROMPTS_POR_PECA["Petição Inicial"]