def gerar_template_especifico(peca_id: str, area: str, detalhes: dict) -> str:
 
    templates = {
        # ==================== CRIMINAL (7) ====================
        "queixa_crime": template_queixa_crime,
        "resposta_acusacao": template_resposta_acusacao,
        "habeas_corpus": template_habeas_corpus,
        "apelacao_criminal": template_apelacao_criminal,
        "alegacoes_finais_criminais": template_alegacoes_finais_criminais,
        "pedido_liberdade_provisoria": template_pedido_liberdade_provisoria,
        "recurso_sentido_estrito": template_recurso_sentido_estrito,
        
        # ==================== TRABALHISTA (6) ====================
        "reclamacao_trabalhista": template_reclamacao_trabalhista,
        "contestacao_trabalhista": template_contestacao_trabalhista,
        "impugnacao_contestacao_trabalhista": template_impugnacao_contestacao_trabalhista,
        "recurso_ordinario_trabalhista": template_recurso_ordinario_trabalhista,
        "contrarrazoes_recurso_ordinario": template_contrarrazoes_recurso_ordinario,
        "recurso_revista": template_recurso_revista,
        
        # ==================== PREVIDENCIÁRIO (5) ====================
        "requerimento_beneficio_administrativo": template_requerimento_beneficio_administrativo,
        "recurso_previdenciario_administrativo": template_recurso_previdenciario_administrativo,
        "revisao_beneficio_administrativo": template_revisao_beneficio_administrativo,
        "acao_concessao_beneficio": template_acao_concessao_beneficio,
        "acao_revisao_beneficio": template_acao_revisao_beneficio,
        
        # ==================== CONTRATOS (2) ====================
        "contrato": template_contrato,
        "termos_uso": template_termos_uso,
        
        # ==================== CÍVEL (26) ====================
        "peticao_inicial": template_peticao_inicial,
        "contestacao_civel": template_contestacao_civel,
        "impugnacao_contestacao": template_impugnacao_contestacao,
        "alegacoes_finais_civel": template_alegacoes_finais_civel,
        "apelacao_civel": template_apelacao_civel,
        "contrarrazoes_apelacao": template_contrarrazoes_apelacao,
        "contrarrazoes_recurso_inominado": template_contrarrazoes_recurso_inominado,
        "contrarrazoes_embargos_declaracao": template_contrarrazoes_embargos_declaracao,
        "agravo_instrumento": template_agravo_instrumento,
        "contraminuta_agravo": template_contraminuta_agravo,
        "embargos_declaracao": template_embargos_declaracao,
        "recurso_especial": template_recurso_especial,
        "mandado_seguranca": template_mandado_seguranca,
        "recurso_inominado": template_recurso_inominado,
        "impugnacao_cumprimento": template_impugnacao_cumprimento,
        "cumprimento_sentenca": template_cumprimento_sentenca,
        "embargos_execucao": template_embargos_execucao,
        "manifestacao_processual": template_manifestacao_processual,
        "impugnacao_embargos": template_impugnacao_embargos,
        "impugnacao_laudo": template_impugnacao_laudo,
        "agravo_interno": template_agravo_interno,
        "excecao_pre_executividade": template_excecao_pre_executividade,
        "agravo_recurso_especial": template_agravo_recurso_especial,
        "contrarrazoes_recurso_especial": template_contrarrazoes_recurso_especial,
        "embargos_terceiro": template_embargos_terceiro,
        "notificacao_extrajudicial": template_notificacao_extrajudicial,
    }
    
    template_func = templates.get(peca_id)
    
    if template_func:
        return template_func(detalhes)
    else:
        return f"[ERRO: Template específico não encontrado para {peca_id}]"


# ╔═══════════════════════════════════════════════════════════════╗
# ║                    TEMPLATES CRIMINAIS (7)                     ║
# ╚═══════════════════════════════════════════════════════════════╝

def template_queixa_crime(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA ___ª VARA CRIMINAL DA COMARCA DE _____

{d.get('querelante', '[NOME DO QUERELANTE]')}, brasileiro(a), {d.get('querelante_cpf', 'CPF nº ___')}, residente e domiciliado(a) em {d.get('querelante_endereco', '[ENDEREÇO]')}, por seu advogado que esta subscreve (procuração anexa), vem, respeitosamente, à presença de Vossa Excelência, ofertar a presente

QUEIXA-CRIME

em face de {d.get('querelado', '[NOME DO QUERELADO]')}, {d.get('querelado_qualificacao', '[QUALIFICAÇÃO]')}, pelos fatos e fundamentos a seguir expostos:

I - DOS FATOS

{d.get('fatos', '[DESCRIÇÃO DETALHADA DOS FATOS CRIMINOSOS]')}

II - DA MATERIALIDADE E AUTORIA

A materialidade delitiva resta demonstrada por {d.get('provas', '[PROVAS]')}.

A autoria é inequívoca, pois o(a) querelado(a) foi claramente identificado(a) como autor(a) dos fatos narrados.

III - DA TIPIFICAÇÃO PENAL

{d.get('tipificacao', '[ARTIGO DO CÓDIGO PENAL E DESCRIÇÃO DO TIPO PENAL]')}

IV - DOS PEDIDOS

Diante do exposto, requer:

a) O recebimento da presente queixa-crime;
b) A citação do(a) querelado(a) para responder à acusação;
c) A condenação do(a) querelado(a) nas penas do crime tipificado.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Nome do Advogado]
OAB/__ nº _____"""


def template_resposta_acusacao(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA ___ª VARA CRIMINAL

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('acusado', '[NOME DO ACUSADO]')}, já qualificado(a) nos autos, por seu advogado que esta subscreve, vem apresentar

RESPOSTA À ACUSAÇÃO

I - PRELIMINARES

{d.get('preliminares', '[PRELIMINARES - inépcia, falta de justa causa, etc]')}

II - DO MÉRITO

{d.get('merito', '[VERSÃO DA DEFESA E TESES]')}

III - DAS PROVAS

Requer a produção de: {d.get('provas', '[PROVAS A PRODUZIR]')}

IV - DOS PEDIDOS

Requer a absolvição sumária ou, subsidiariamente, a designação de audiência.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_habeas_corpus(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

{d.get('impetrante', '[ADVOGADO]')}, OAB/__ nº ___, vem impetrar

HABEAS CORPUS

com PEDIDO DE LIMINAR, em favor de {d.get('paciente', '[NOME DO PACIENTE]')}.

I - DOS FATOS

{d.get('fatos', '[DESCRIÇÃO DO CONSTRANGIMENTO ILEGAL]')}

II - DO CONSTRANGIMENTO ILEGAL

{d.get('constrangimento', '[FUNDAMENTAÇÃO DO CONSTRANGIMENTO ILEGAL]')}

III - DO PEDIDO DE LIMINAR

Requer liminar para {d.get('liminar', '[SOLTURA/MEDIDAS ALTERNATIVAS]')}.

IV - DOS PEDIDOS

Requer a concessão da ordem de habeas corpus.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_apelacao_criminal(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('apelante', '[NOME]')}, inconformado com a sentença, vem interpor

APELAÇÃO CRIMINAL

I - DA TEMPESTIVIDADE

Recurso tempestivo conforme art. 593 do CPP.

II - DAS RAZÕES

{d.get('razoes', '[RAZÕES DO RECURSO - nulidade, absolvição, dosimetria, etc]')}

III - DOS PEDIDOS

Requer a reforma da sentença para {d.get('pedido', '[ABSOLVIÇÃO/REDUÇÃO DE PENA/etc]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_alegacoes_finais_criminais(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('parte', 'A DEFESA')}, vem apresentar

ALEGAÇÕES FINAIS

I - BREVE RELATÓRIO

{d.get('relatorio', '[RESUMO DO PROCESSO]')}

II - DAS PROVAS PRODUZIDAS

{d.get('provas', '[ANÁLISE DAS PROVAS]')}

III - DA ARGUMENTAÇÃO JURÍDICA

{d.get('argumentacao', '[TESES DE DEFESA/ACUSAÇÃO]')}

IV - DOS PEDIDOS

Requer a {d.get('pedido', '[ABSOLVIÇÃO/CONDENAÇÃO]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_pedido_liberdade_provisoria(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('requerente', '[NOME]')}, vem requerer

LIBERDADE PROVISÓRIA

I - DOS FATOS

{d.get('fatos', '[SITUAÇÃO DA PRISÃO]')}

II - DO DIREITO

{d.get('fundamentacao', '[AUSÊNCIA DE REQUISITOS DA PRISÃO PREVENTIVA]')}

III - DOS PEDIDOS

Requer a concessão de liberdade provisória {d.get('medidas', '[COM/SEM MEDIDAS CAUTELARES]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_recurso_sentido_estrito(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrente', '[NOME]')}, vem interpor

RECURSO EM SENTIDO ESTRITO

I - DA DECISÃO RECORRIDA

{d.get('decisao', '[RESUMO DA DECISÃO]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO DO RECURSO]')}

III - DOS PEDIDOS

Requer a reforma da decisão para {d.get('pedido', '[PEDIDO ESPECÍFICO]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


# ╔═══════════════════════════════════════════════════════════════╗
# ║                   TEMPLATES TRABALHISTAS (6)                   ║
# ╚═══════════════════════════════════════════════════════════════╝

def template_reclamacao_trabalhista(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DO TRABALHO

{d.get('reclamante', '[NOME DO RECLAMANTE]')}, CPF {d.get('cpf', '___')}, vem propor

RECLAMAÇÃO TRABALHISTA

em face de {d.get('reclamada', '[RAZÃO SOCIAL]')}, CNPJ {d.get('cnpj', '___')}.

I - DA RELAÇÃO DE EMPREGO

Admissão: {d.get('admissao', '[DATA]')}
Função: {d.get('funcao', '[CARGO]')}
Salário: R$ {d.get('salario', '[VALOR]')}
Demissão: {d.get('demissao', '[DATA]')}

II - DOS PEDIDOS

{d.get('pedidos', '''a) Aviso prévio indenizado
b) 13º salário proporcional
c) Férias + 1/3
d) FGTS + 40%
e) Horas extras
f) [OUTROS PEDIDOS]''')}

III - DO VALOR DA CAUSA

R$ {d.get('valor_causa', '[VALOR]')}

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contestacao_trabalhista(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DO TRABALHO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('reclamada', '[RAZÃO SOCIAL]')}, já qualificada, vem apresentar

CONTESTAÇÃO

I - PRELIMINARES

{d.get('preliminares', '[PRELIMINARES - incompetência, prescrição, etc]')}

II - DO MÉRITO

{d.get('merito', '[IMPUGNAÇÃO DOS PEDIDOS DO RECLAMANTE]')}

III - DOS PEDIDOS

Requer a improcedência total dos pedidos.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_impugnacao_contestacao_trabalhista(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DO TRABALHO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('reclamante', '[NOME]')}, vem apresentar

IMPUGNAÇÃO À CONTESTAÇÃO

I - DAS PRELIMINARES

{d.get('preliminares', '[REFUTAÇÃO DAS PRELIMINARES]')}

II - DO MÉRITO

{d.get('merito', '[REFUTAÇÃO DOS ARGUMENTOS DA RECLAMADA]')}

III - DOS PEDIDOS

Requer a rejeição das preliminares e procedência dos pedidos iniciais.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_recurso_ordinario_trabalhista(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL REGIONAL DO TRABALHO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrente', '[NOME]')}, vem interpor

RECURSO ORDINÁRIO

I - DA SENTENÇA RECORRIDA

{d.get('sentenca', '[RESUMO DA SENTENÇA]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO - reforma total ou parcial]')}

III - DOS PEDIDOS

Requer o provimento do recurso para {d.get('pedido', '[REFORMA DA SENTENÇA]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contrarrazoes_recurso_ordinario(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL REGIONAL DO TRABALHO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrido', '[NOME]')}, vem apresentar

CONTRARRAZÕES AO RECURSO ORDINÁRIO

I - DA INTEMPESTIVIDADE/DESERÇÃO

{d.get('objecoes', '[SE HOUVER OBJEÇÕES PROCESSUAIS]')}

II - DO MÉRITO

{d.get('merito', '[DEFESA DA SENTENÇA RECORRIDA]')}

III - DOS PEDIDOS

Requer o não provimento do recurso e manutenção da sentença.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_recurso_revista(d: dict) -> str:
    return f"""EXCELENTÍSSIMO SENHOR MINISTRO PRESIDENTE DO TRIBUNAL SUPERIOR DO TRABALHO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrente', '[NOME]')}, vem interpor

RECURSO DE REVISTA

I - DA ADMISSIBILIDADE

{d.get('admissibilidade', '[DEMONSTRAÇÃO DOS REQUISITOS - violação de lei, divergência jurisprudencial]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO DO RECURSO]')}

III - DOS PEDIDOS

Requer o provimento do recurso para {d.get('pedido', '[REFORMA DO ACÓRDÃO]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


# ╔═══════════════════════════════════════════════════════════════╗
# ║                 TEMPLATES PREVIDENCIÁRIOS (5)                  ║
# ╚═══════════════════════════════════════════════════════════════╝

def template_requerimento_beneficio_administrativo(d: dict) -> str:
    return f"""AO INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS

{d.get('requerente', '[NOME]')}, CPF {d.get('cpf', '___')}, vem requerer

CONCESSÃO DE BENEFÍCIO PREVIDENCIÁRIO

I - DA QUALIFICAÇÃO

Nome: {d.get('nome', '[NOME COMPLETO]')}
CPF: {d.get('cpf', '[CPF]')}
Data de Nascimento: {d.get('nascimento', '[DATA]')}
Endereço: {d.get('endereco', '[ENDEREÇO]')}

II - DO BENEFÍCIO REQUERIDO

{d.get('beneficio', '[TIPO DE BENEFÍCIO - Aposentadoria por tempo de contribuição, por idade, auxílio-doença, etc]')}

III - DA FUNDAMENTAÇÃO

{d.get('fundamentacao', '[DEMONSTRAÇÃO DO PREENCHIMENTO DOS REQUISITOS]')}

IV - DOS DOCUMENTOS

{d.get('documentos', '''- RG e CPF
- Comprovante de residência
- CTPS
- Carnês de contribuição
- [OUTROS DOCUMENTOS]''')}

V - DOS PEDIDOS

Requer a concessão do benefício pleiteado.

[Cidade], [Data]

_______________________
[Requerente ou Advogado]"""


def template_recurso_previdenciario_administrativo(d: dict) -> str:
    return f"""AO CONSELHO DE RECURSOS DA PREVIDÊNCIA SOCIAL - CRPS

Processo Administrativo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrente', '[NOME]')}, vem interpor

RECURSO ADMINISTRATIVO

I - DA DECISÃO RECORRIDA

{d.get('decisao', '[RESUMO DA DECISÃO QUE INDEFERIU O BENEFÍCIO]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO - demonstração do preenchimento dos requisitos]')}

III - DOS PEDIDOS

Requer a reforma da decisão e concessão do benefício.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_revisao_beneficio_administrativo(d: dict) -> str:
    return f"""AO INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS

{d.get('requerente', '[NOME]')}, beneficiário(a) do NB {d.get('nb', '[NÚMERO]')}, vem requerer

REVISÃO DE BENEFÍCIO

I - DO BENEFÍCIO ATUAL

Benefício: {d.get('beneficio', '[TIPO]')}
NB: {d.get('nb', '[NÚMERO]')}
DIB: {d.get('dib', '[DATA]')}
RMI Atual: R$ {d.get('rmi_atual', '[VALOR]')}

II - DO PEDIDO DE REVISÃO

{d.get('pedido_revisao', '[FUNDAMENTAÇÃO - inclusão de períodos, recálculo, etc]')}

III - DOS PEDIDOS

Requer a revisão do benefício com pagamento das diferenças atrasadas.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_acao_concessao_beneficio(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) FEDERAL

{d.get('autor', '[NOME]')}, CPF {d.get('cpf', '___')}, vem propor

AÇÃO DE CONCESSÃO DE BENEFÍCIO PREVIDENCIÁRIO

em face do INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS.

I - DOS FATOS

{d.get('fatos', '[HISTÓRICO - requerimento administrativo negado, requisitos preenchidos]')}

II - DO DIREITO

{d.get('direito', '[DEMONSTRAÇÃO DO PREENCHIMENTO DOS REQUISITOS LEGAIS]')}

III - DOS PEDIDOS

a) Concessão do benefício {d.get('beneficio', '[TIPO]')};
b) Pagamento das parcelas atrasadas desde o requerimento administrativo;
c) Implantação do benefício na folha de pagamentos;
d) Tutela antecipada para implantação imediata.

Valor da causa: R$ {d.get('valor_causa', '[VALOR]')}

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_acao_revisao_beneficio(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) FEDERAL

{d.get('autor', '[NOME]')}, beneficiário NB {d.get('nb', '___')}, vem propor

AÇÃO DE REVISÃO DE BENEFÍCIO PREVIDENCIÁRIO

em face do INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS.

I - DO BENEFÍCIO ATUAL

{d.get('beneficio_atual', '[DESCRIÇÃO DO BENEFÍCIO E RMI ATUAL]')}

II - DO PEDIDO DE REVISÃO

{d.get('pedido_revisao', '[FUNDAMENTAÇÃO DA REVISÃO - tese jurídica, documentos não considerados, etc]')}

III - DOS PEDIDOS

a) Revisão do benefício com novo cálculo da RMI;
b) Pagamento das diferenças atrasadas (respeitada prescrição quinquenal);
c) Implantação do novo valor na folha de pagamentos.

Valor da causa: R$ {d.get('valor_causa', '[VALOR DAS DIFERENÇAS]')}

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


# ╔═══════════════════════════════════════════════════════════════╗
# ║                     TEMPLATES CONTRATOS (2)                    ║
# ╚═══════════════════════════════════════════════════════════════╝

def template_contrato(d: dict) -> str:
    return f"""{d.get('tipo_contrato', 'CONTRATO DE PRESTAÇÃO DE SERVIÇOS').upper()}

Pelo presente instrumento particular, de um lado:

CONTRATANTE: {d.get('contratante', '[NOME]')}, {d.get('contratante_qualificacao', '[QUALIFICAÇÃO COMPLETA]')};

CONTRATADO(A): {d.get('contratado', '[NOME]')}, {d.get('contratado_qualificacao', '[QUALIFICAÇÃO COMPLETA]')};

As partes acima qualificadas têm, entre si, justo e acertado o presente Contrato, que se regerá pelas cláusulas seguintes:

CLÁUSULA PRIMEIRA - DO OBJETO

{d.get('objeto', '[DESCRIÇÃO DO OBJETO DO CONTRATO]')}

CLÁUSULA SEGUNDA - DO PRAZO

O presente contrato terá vigência de {d.get('prazo', '[PRAZO]')}, iniciando-se em {d.get('data_inicio', '[DATA]')} e encerrando-se em {d.get('data_fim', '[DATA]')}.

CLÁUSULA TERCEIRA - DO VALOR E FORMA DE PAGAMENTO

{d.get('pagamento', '[VALOR E CONDIÇÕES DE PAGAMENTO]')}

CLÁUSULA QUARTA - DAS OBRIGAÇÕES DO CONTRATANTE

{d.get('obrigacoes_contratante', '[OBRIGAÇÕES]')}

CLÁUSULA QUINTA - DAS OBRIGAÇÕES DO CONTRATADO

{d.get('obrigacoes_contratado', '[OBRIGAÇÕES]')}

CLÁUSULA SEXTA - DA RESCISÃO

{d.get('rescisao', '[CONDIÇÕES DE RESCISÃO]')}

CLÁUSULA SÉTIMA - DAS PENALIDADES

{d.get('penalidades', '[MULTAS E PENALIDADES]')}

CLÁUSULA OITAVA - DO FORO

Fica eleito o foro de {d.get('foro', '[CIDADE]')} para dirimir quaisquer dúvidas oriundas do presente contrato.

E, por estarem assim justos e contratados, firmam o presente instrumento em duas vias de igual teor e forma.

[Cidade], [Data]

_______________________          _______________________
CONTRATANTE                      CONTRATADO(A)

Testemunhas:

_____________________ _____________________
Nome:                 Nome:
CPF:                  CPF:"""


def template_termos_uso(d: dict) -> str:
    return f"""TERMOS E CONDIÇÕES DE USO

{d.get('empresa', '[NOME DA EMPRESA/PLATAFORMA]')}

Última atualização: {d.get('data_atualizacao', '[DATA]')}

1. ACEITAÇÃO DOS TERMOS

Ao acessar e usar {d.get('plataforma', '[NOME DA PLATAFORMA]')}, você concorda com estes Termos de Uso.

2. DESCRIÇÃO DO SERVIÇO

{d.get('descricao_servico', '[DESCRIÇÃO DOS SERVIÇOS OFERECIDOS]')}

3. CADASTRO E CONTA DE ACESSO

{d.get('cadastro', '''3.1. Para utilizar determinadas funcionalidades, é necessário realizar cadastro.
3.2. Você é responsável por manter a confidencialidade de sua senha.
3.3. Você deve fornecer informações verdadeiras e atualizadas.''')}

4. OBRIGAÇÕES DO USUÁRIO

{d.get('obrigacoes_usuario', '''4.1. Não violar direitos de terceiros.
4.2. Não utilizar o serviço para fins ilícitos.
4.3. Respeitar as leis aplicáveis.''')}

5. PROPRIEDADE INTELECTUAL

{d.get('propriedade_intelectual', 'Todo o conteúdo da plataforma é protegido por direitos autorais.')}

6. LIMITAÇÃO DE RESPONSABILIDADE

{d.get('limitacao_responsabilidade', 'A plataforma não se responsabiliza por danos indiretos.')}

7. POLÍTICA DE PRIVACIDADE

{d.get('privacidade', 'Os dados pessoais são tratados conforme nossa Política de Privacidade.')}

8. MODIFICAÇÕES DOS TERMOS

Estes termos podem ser modificados a qualquer momento. Recomendamos revisão periódica.

9. RESCISÃO

{d.get('rescisao', 'Podemos suspender ou encerrar sua conta por violação destes termos.')}

10. LEI APLICÁVEL E FORO

Estes termos são regidos pela legislação brasileira. Foro: {d.get('foro', '[CIDADE]')}.

Contato: {d.get('contato', '[EMAIL/TELEFONE]')}"""


# ╔═══════════════════════════════════════════════════════════════╗
# ║                      TEMPLATES CÍVEL (26)                      ║
# ╚═══════════════════════════════════════════════════════════════╝

def template_peticao_inicial(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA ___ª VARA CÍVEL

{d.get('autor', '[NOME DO AUTOR]')}, {d.get('autor_qualificacao', '[QUALIFICAÇÃO]')}, por seu advogado que esta subscreve, vem propor

{d.get('tipo_acao', 'AÇÃO DE COBRANÇA').upper()}

em face de {d.get('reu', '[NOME DO RÉU]')}, {d.get('reu_qualificacao', '[QUALIFICAÇÃO]')}, pelos fatos e fundamentos a seguir:

I - DOS FATOS

{d.get('fatos', '[DESCRIÇÃO DETALHADA DOS FATOS]')}

II - DO DIREITO

{d.get('fundamentacao_juridica', '[FUNDAMENTAÇÃO LEGAL]')}

III - DOS PEDIDOS

Diante do exposto, requer:

{d.get('pedidos', '''a) A citação do réu para contestar sob pena de revelia;
b) A procedência dos pedidos para condenar o réu ao pagamento de R$ [VALOR];
c) Condenação em custas e honorários advocatícios;
d) Produção de provas.''')}

Dá-se à causa o valor de R$ {d.get('valor_causa', '[VALOR]')}.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contestacao_civel(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('reu', '[NOME DO RÉU]')}, já qualificado nos autos, vem apresentar

CONTESTAÇÃO

I - PRELIMINARES

{d.get('preliminares', '[PRELIMINARES - incompetência, ilegitimidade, prescrição, etc]')}

II - DO MÉRITO

{d.get('merito', '[IMPUGNAÇÃO DOS FATOS E PEDIDOS DO AUTOR]')}

III - DOS PEDIDOS

Requer a improcedência total dos pedidos.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_impugnacao_contestacao(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('autor', '[NOME]')}, vem apresentar

IMPUGNAÇÃO À CONTESTAÇÃO

I - DAS PRELIMINARES

{d.get('refutacao_preliminares', '[REFUTAÇÃO DAS PRELIMINARES ARGUIDAS]')}

II - DO MÉRITO

{d.get('refutacao_merito', '[REFUTAÇÃO DOS ARGUMENTOS DO RÉU]')}

III - DOS PEDIDOS

Requer a rejeição das preliminares e procedência dos pedidos iniciais.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_alegacoes_finais_civel(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('parte', '[AUTOR/RÉU]')}, vem apresentar

ALEGAÇÕES FINAIS

I - BREVE RELATÓRIO

{d.get('relatorio', '[RESUMO DO PROCESSO]')}

II - DAS PROVAS PRODUZIDAS

{d.get('provas', '[ANÁLISE DAS PROVAS]')}

III - DA ARGUMENTAÇÃO JURÍDICA

{d.get('argumentacao', '[ARGUMENTAÇÃO FINAL]')}

IV - DOS PEDIDOS

Requer a {d.get('pedido', '[PROCEDÊNCIA/IMPROCEDÊNCIA]')} dos pedidos.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_apelacao_civel(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('apelante', '[NOME]')}, inconformado com a sentença, vem interpor

APELAÇÃO CÍVEL

I - DA TEMPESTIVIDADE

Recurso tempestivo conforme CPC.

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO DO RECURSO]')}

III - DOS PEDIDOS

Requer o provimento do recurso para reformar a sentença.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contrarrazoes_apelacao(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('apelado', '[NOME]')}, vem apresentar

CONTRARRAZÕES DE APELAÇÃO

I - DA INTEMPESTIVIDADE/DESERÇÃO

{d.get('objecoes', '[SE HOUVER]')}

II - DO MÉRITO

{d.get('merito', '[DEFESA DA SENTENÇA]')}

III - DOS PEDIDOS

Requer o não provimento do recurso.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contrarrazoes_recurso_inominado(d: dict) -> str:
    return f"""EGRÉGIA TURMA RECURSAL

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrido', '[NOME]')}, vem apresentar

CONTRARRAZÕES AO RECURSO INOMINADO

I - DA TEMPESTIVIDADE/PREPARO

{d.get('objecoes', '[ANÁLISE]')}

II - DO MÉRITO

{d.get('merito', '[MANUTENÇÃO DA SENTENÇA]')}

III - DOS PEDIDOS

Requer o não provimento do recurso.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contrarrazoes_embargos_declaracao(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('embargado', '[NOME]')}, vem apresentar

CONTRARRAZÕES AOS EMBARGOS DE DECLARAÇÃO

{d.get('manifestacao', '[MANIFESTAÇÃO SOBRE OS EMBARGOS - concordância ou refutação]')}

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_agravo_instrumento(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('agravante', '[NOME]')}, vem interpor

AGRAVO DE INSTRUMENTO

com pedido de EFEITO SUSPENSIVO/ANTECIPAÇÃO DE TUTELA

I - DA DECISÃO AGRAVADA

{d.get('decisao', '[RESUMO DA DECISÃO]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO]')}

III - DO EFEITO SUSPENSIVO/TUTELA ANTECIPADA

{d.get('tutela', '[PEDIDO DE LIMINAR]')}

IV - DOS PEDIDOS

Requer a reforma da decisão.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contraminuta_agravo(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('agravado', '[NOME]')}, vem apresentar

CONTRAMINUTA DE AGRAVO

I - DA INTEMPESTIVIDADE

{d.get('objecoes', '[SE HOUVER]')}

II - DO MÉRITO

{d.get('merito', '[MANUTENÇÃO DA DECISÃO]')}

III - DOS PEDIDOS

Requer o não provimento do agravo.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_embargos_declaracao(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A)/DESEMBARGADOR(A)

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('embargante', '[NOME]')}, vem opor

EMBARGOS DE DECLARAÇÃO

I - DA DECISÃO EMBARGADA

{d.get('decisao', '[IDENTIFICAÇÃO DA DECISÃO]')}

II - DA OMISSÃO/CONTRADIÇÃO/OBSCURIDADE

{d.get('vicio', '[DEMONSTRAÇÃO DO VÍCIO - omissão, contradição ou obscuridade]')}

III - DOS PEDIDOS

Requer o acolhimento dos embargos para sanar o vício apontado.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_recurso_especial(d: dict) -> str:
    return f"""EXCELENTÍSSIMO SENHOR MINISTRO PRESIDENTE DO SUPERIOR TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrente', '[NOME]')}, vem interpor

RECURSO ESPECIAL

I - DA ADMISSIBILIDADE

{d.get('admissibilidade', '[DEMONSTRAÇÃO DOS REQUISITOS - violação de lei federal ou divergência]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO]')}

III - DOS PEDIDOS

Requer o provimento do recurso.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_mandado_seguranca(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

{d.get('impetrante', '[NOME]')}, vem impetrar

MANDADO DE SEGURANÇA

com pedido de LIMINAR

contra ato do(a) {d.get('autoridade_coatora', '[AUTORIDADE COATORA]')}.

I - DOS FATOS

{d.get('fatos', '[DESCRIÇÃO DO ATO COATOR]')}

II - DO DIREITO LÍQUIDO E CERTO

{d.get('direito', '[DEMONSTRAÇÃO DO DIREITO VIOLADO]')}

III - DA LIMINAR

{d.get('liminar', '[PEDIDO DE SUSPENSÃO DO ATO]')}

IV - DOS PEDIDOS

Requer a concessão da segurança.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_recurso_inominado(d: dict) -> str:
    return f"""EGRÉGIA TURMA RECURSAL DOS JUIZADOS ESPECIAIS

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrente', '[NOME]')}, vem interpor

RECURSO INOMINADO

I - DA SENTENÇA RECORRIDA

{d.get('sentenca', '[RESUMO]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO]')}

III - DOS PEDIDOS

Requer a reforma da sentença.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_impugnacao_cumprimento(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('executado', '[NOME]')}, vem apresentar

IMPUGNAÇÃO AO CUMPRIMENTO DE SENTENÇA

I - DO EXCESSO DE EXECUÇÃO

{d.get('excesso', '[DEMONSTRAÇÃO DO EXCESSO]')}

II - DOS CÁLCULOS CORRETOS

{d.get('calculos', '[PLANILHA DE CÁLCULOS]')}

III - DOS PEDIDOS

Requer o acolhimento da impugnação e redução do valor executado.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_cumprimento_sentenca(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('exequente', '[NOME]')}, vem promover

CUMPRIMENTO DE SENTENÇA

I - DO TÍTULO EXECUTIVO

{d.get('titulo', '[IDENTIFICAÇÃO DA SENTENÇA TRANSITADA EM JULGADO]')}

II - DO CÁLCULO DO DÉBITO

Valor principal: R$ {d.get('principal', '[VALOR]')}
Juros e correção: R$ {d.get('juros', '[VALOR]')}
Total: R$ {d.get('total', '[VALOR]')}

III - DOS PEDIDOS

Requer a intimação do executado para pagamento em 15 dias sob pena de multa de 10% e penhora.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_embargos_execucao(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('embargante', '[NOME]')}, vem opor

EMBARGOS À EXECUÇÃO

com pedido de EFEITO SUSPENSIVO

I - DAS PRELIMINARES

{d.get('preliminares', '[NULIDADES, VÍCIOS]')}

II - DO MÉRITO

{d.get('merito', '[INEXIGIBILIDADE, EXCESSO, PAGAMENTO, etc]')}

III - DO EFEITO SUSPENSIVO

{d.get('suspensivo', '[PEDIDO DE SUSPENSÃO DA EXECUÇÃO]')}

IV - DOS PEDIDOS

Requer o acolhimento dos embargos e extinção da execução.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_manifestacao_processual(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('parte', '[NOME]')}, vem manifestar-se nos autos sobre {d.get('assunto', '[ASSUNTO]')}.

{d.get('manifestacao', '[CONTEÚDO DA MANIFESTAÇÃO]')}

Termos em que, requer seja a presente juntada aos autos.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_impugnacao_embargos(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('exequente', '[NOME]')}, vem apresentar

IMPUGNAÇÃO AOS EMBARGOS À EXECUÇÃO

{d.get('impugnacao', '[REFUTAÇÃO DOS ARGUMENTOS DO EMBARGANTE]')}

Requer a rejeição dos embargos e prosseguimento da execução.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_impugnacao_laudo(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('parte', '[NOME]')}, vem apresentar

IMPUGNAÇÃO AO LAUDO PERICIAL

I - DO LAUDO PERICIAL

{d.get('laudo', '[IDENTIFICAÇÃO DO LAUDO]')}

II - DAS DIVERGÊNCIAS

{d.get('divergencias', '[PONTOS CONTESTADOS DO LAUDO]')}

III - DOS PEDIDOS

Requer a realização de nova perícia ou esclarecimentos pelo perito.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_agravo_interno(d: dict) -> str:
    return f"""EGRÉGIO TRIBUNAL/CÂMARA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('agravante', '[NOME]')}, vem interpor

AGRAVO INTERNO

contra decisão monocrática proferida por Vossa Excelência.

I - DA DECISÃO AGRAVADA

{d.get('decisao', '[RESUMO DA DECISÃO MONOCRÁTICA]')}

II - DAS RAZÕES

{d.get('razoes', '[FUNDAMENTAÇÃO]')}

III - DOS PEDIDOS

Requer a reforma da decisão pelo colegiado.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_excecao_pre_executividade(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('executado', '[NOME]')}, vem opor

EXCEÇÃO DE PRÉ-EXECUTIVIDADE

I - DA MATÉRIA DE ORDEM PÚBLICA

{d.get('materia', '[INEXIGIBILIDADE DO TÍTULO, PRESCRIÇÃO, NULIDADE, etc]')}

II - DA DESNECESSIDADE DE GARANTIA DO JUÍZO

Por se tratar de matéria de ordem pública, cognoscível de ofício, não há necessidade de garantia prévia.

III - DOS PEDIDOS

Requer o acolhimento da exceção e extinção da execução.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_agravo_recurso_especial(d: dict) -> str:
    return f"""EXCELENTÍSSIMO SENHOR MINISTRO PRESIDENTE DO SUPERIOR TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('agravante', '[NOME]')}, vem interpor

AGRAVO EM RECURSO ESPECIAL

contra decisão que inadmitiu o Recurso Especial.

I - DA DECISÃO AGRAVADA

{d.get('decisao', '[DECISÃO QUE NEGOU SEGUIMENTO AO RESP]')}

II - DA PRESENÇA DOS REQUISITOS

{d.get('requisitos', '[DEMONSTRAÇÃO DOS REQUISITOS DO RESP]')}

III - DOS PEDIDOS

Requer o provimento do agravo e processamento do Recurso Especial.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_contrarrazoes_recurso_especial(d: dict) -> str:
    return f"""EXCELENTÍSSIMO SENHOR MINISTRO DO SUPERIOR TRIBUNAL DE JUSTIÇA

Processo nº {d.get('numero_processo', '[NÚMERO]')}

{d.get('recorrido', '[NOME]')}, vem apresentar

CONTRARRAZÕES AO RECURSO ESPECIAL

I - DA INADMISSIBILIDADE

{d.get('inadmissibilidade', '[AUSÊNCIA DE REQUISITOS]')}

II - DO MÉRITO

{d.get('merito', '[MANUTENÇÃO DO ACÓRDÃO]')}

III - DOS PEDIDOS

Requer o não provimento do recurso.

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_embargos_terceiro(d: dict) -> str:
    return f"""EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO

Processo nº {d.get('numero_processo', '[NÚMERO - processo principal]')}

{d.get('embargante', '[NOME]')}, terceiro estranho à lide, vem opor

EMBARGOS DE TERCEIRO

I - DA LEGITIMIDADE

{d.get('legitimidade', '[DEMONSTRAÇÃO DE QUE É TERCEIRO]')}

II - DA POSSE/PROPRIEDADE DO BEM

{d.get('posse_propriedade', '[COMPROVAÇÃO DA TITULARIDADE DO BEM PENHORADO/ARRESTADO]')}

III - DA CONSTRIÇÃO INDEVIDA

{d.get('constricao', '[DESCRIÇÃO DA PENHORA/ARRESTO INDEVIDO]')}

IV - DOS PEDIDOS

Requer a procedência dos embargos para liberar o bem da constrição.

Valor da causa: R$ {d.get('valor_causa', '[VALOR DO BEM]')}

Termos em que, pede deferimento.

[Cidade], [Data]

_______________________
[Advogado]
OAB/__ nº _____"""


def template_notificacao_extrajudicial(d: dict) -> str:
    return f"""NOTIFICAÇÃO EXTRAJUDICIAL

{d.get('notificante', '[NOME DO NOTIFICANTE]')}, {d.get('notificante_qualificacao', '[QUALIFICAÇÃO]')}, por seu advogado que esta subscreve, vem, por meio da presente, NOTIFICAR:

NOTIFICADO(A): {d.get('notificado', '[NOME]')}, {d.get('notificado_qualificacao', '[QUALIFICAÇÃO]')}

FINALIDADE: {d.get('finalidade', '[CONSTITUIÇÃO EM MORA, RESCISÃO, AVISO, etc]')}

FUNDAMENTAÇÃO:

{d.get('fundamentacao', '[DESCRIÇÃO DOS FATOS E FUNDAMENTOS DA NOTIFICAÇÃO]')}

PRAZO PARA MANIFESTAÇÃO:

Fica o(a) notificado(a) INTIMADO(A) a, no prazo de {d.get('prazo', '[PRAZO]')}, contados do recebimento desta:

{d.get('exigencias', '''a) [AÇÃO REQUERIDA - ex: efetuar o pagamento, regularizar situação, etc]
b) [OUTRAS EXIGÊNCIAS]''')}

ADVERTÊNCIA:

O não atendimento no prazo estabelecido acarretará {d.get('consequencias', '[CONSEQUÊNCIAS - cobrança judicial, rescisão contratual, etc]')}, sem prejuízo das medidas judiciais cabíveis.

DOCUMENTOS ANEXOS:

{d.get('documentos', '[LISTA DE DOCUMENTOS COMPROBATÓRIOS]')}

Por ser a expressão da verdade, firma a presente.

[Cidade], [Data]

_______________________
[Nome do Advogado]
OAB/__ nº _____

COMPROVANTE DE RECEBIMENTO:

Recebi a presente notificação em ___/___/___

_______________________
Assinatura do(a) Notificado(a)
Nome:
RG:"""