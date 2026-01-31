import React, { useState, useEffect } from 'react';
import { Home, Scale, Building, Shield, Briefcase, FileText, Download, Loader, ArrowLeft, Upload, Edit3, Save, AlertCircle, CheckCircle, XCircle, Search, BookOpen, Plus, Star, Users, Settings, ImageIcon, Zap, Trash2, Brain, Menu } from 'lucide-react';

// ============================================================================
// 1. ESTILOS GLOBAIS E TIPOGRAFIA
// ============================================================================
const fontStyles = `
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap');
  
  :root {
    --color-gold: #C5A059;
    --color-gold-dark: #9A7B3A;
    --color-text-primary: #2C3E50;
    --color-text-secondary: #64748B;
    --color-bg-main: #F8F9FA;
    --color-bg-card: #FFFFFF;
    --color-border: #E2E8F0;
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }
  
  .font-serif { font-family: 'Playfair Display', serif; }
  .font-sans { font-family: 'Outfit', sans-serif; }
  
  .text-gold { color: var(--color-gold); }
  .text-primary { color: var(--color-text-primary); }
  
  /* Gradiente Dourado Luxuoso */
  .bg-gradient-gold { 
    background: linear-gradient(135deg, #C5A059 0%, #AB8A4B 100%);
    color: white;
  }
  .bg-gradient-gold:hover { 
    background: linear-gradient(135deg, #D4AF6A 0%, #BFA05F 100%);
    box-shadow: 0 4px 12px rgba(197, 160, 89, 0.3);
  }

  /* Cards Premium */
  .card-premium {
    background-color: var(--color-bg-card);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
  }
  .card-premium:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--color-gold);
  }
  
  /* Inputs Limpos */
  .input-premium {
    width: 100%;
    background-color: #FFFFFF;
    border: 1px solid var(--color-border);
    color: var(--color-text-primary);
    padding: 1rem;
    border-radius: 0.5rem;
    transition: all 0.3s;
    font-size: 16px; /* Evita zoom no iPhone */
  }
  .input-premium:focus {
    border-color: var(--color-gold);
    outline: none;
    box-shadow: 0 0 0 3px rgba(197, 160, 89, 0.1);
  }

  /* Documento Final */
  .doc-container {
    font-family: 'Times New Roman', serif;
    font-size: 12pt;
    line-height: 1.5;
    color: black;
    text-align: justify;
    background-color: white;
  }
  
  .modo-foco {
    background: #EFEBE9;
    min-height: 100vh;
  }
  
  .jurisprudencia-citacao {
    background: #FFFBF2;
    border-left: 4px solid #C5A059;
    padding: 16px;
    font-style: italic;
    margin: 20px 0;
  }

  /* Utilitário para esconder scrollbar no stepper mobile mas permitir scroll */
  .no-scrollbar::-webkit-scrollbar { display: none; }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
`;

// ============================================================================
// 2. CONFIGURAÇÕES GLOBAIS
// ============================================================================

const iconMap = {
  building: Building,
  shield: Shield,
  briefcase: Briefcase,
  scale: Scale,
  users: Users
};

const CAMPOS_CONFIG = {
  enderecamento: { label: "Endereçamento", tipo: "text", obrigatorio: true, placeholder: "EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA..." },
  nome_acao: { label: "Nome da Ação", tipo: "text", obrigatorio: true, placeholder: "AÇÃO DE INDENIZAÇÃO POR..." },
  autor: { label: "Nome do Autor", tipo: "text", obrigatorio: true },
  autor_qualificacao: { label: "Qualificação do Autor", tipo: "textarea", obrigatorio: true, placeholder: "nacionalidade, estado civil, profissão, portador do CPF..." },
  reu: { label: "Nome do Réu", tipo: "text", obrigatorio: true },
  reu_qualificacao: { label: "Qualificação do Réu", tipo: "textarea", obrigatorio: true },
  autor_cpf: { label: "CPF do Autor", tipo: "text", obrigatorio: true },
  autor_endereco: { label: "Endereço do Autor", tipo: "textarea", obrigatorio: true },
  reu_endereco: { label: "Endereço do Réu", tipo: "textarea", obrigatorio: true },
  fatos: { label: "Narrativa dos Fatos", tipo: "textarea", obrigatorio: true, dica: "Escreva os fatos simples. A IA vai reescrever de forma robusta e jurídica." },
  danos_materiais: { label: "Danos Materiais", tipo: "textarea", obrigatorio: false },
  danos_morais: { label: "Danos Morais", tipo: "textarea", obrigatorio: false },
  fundamentos: { label: "Do Direito", tipo: "textarea", obrigatorio: false, dica: "Será gerado automaticamente pela IA ao finalizar." },
  pedidos: { label: "Dos Pedidos", tipo: "textarea", obrigatorio: true },
  valor_causa: { label: "Valor da Causa (R$)", tipo: "number", obrigatorio: true },
  numero_processo: { label: "Número do Processo (CNJ)", tipo: "text", obrigatorio: true, placeholder: "0000000-00.0000.8.26.0000" },
  resumo_fatos: { label: "Síntese da Inicial (Resumo)", tipo: "textarea", obrigatorio: true, dica: "Resuma brevemente o que o Autor alegou na inicial." },
  preliminares: { label: "Preliminares (Opcional)", tipo: "textarea", obrigatorio: false, dica: "Ex: Inépcia da inicial, Ilegitimidade, Prescrição... A IA vai desenvolver o texto." },
  teses_defesa: { label: "Teses de Mérito (Sua Defesa)", tipo: "textarea", obrigatorio: true, dica: "Quais são seus argumentos de defesa? A IA vai fundamentar juridicamente." },
  provas: { label: "Provas a Produzir", tipo: "textarea", obrigatorio: false, placeholder: "Ex: Testemunhal, pericial, depoimento pessoal...", dica: "Deixe em branco se não houver provas específicas." },
  fundamentos_recurso: { label: "Fundamentos do Recurso", tipo: "textarea", obrigatorio: true },
  refutacao: { label: "Refutação", tipo: "textarea", obrigatorio: true },
  contratante: { label: "Contratante", tipo: "text", obrigatorio: true },
  contratado: { label: "Contratado", tipo: "text", obrigatorio: true },
  objeto: { label: "Objeto do Contrato", tipo: "textarea", obrigatorio: true },
  valor: { label: "Valor (R$)", tipo: "number", obrigatorio: true },
  prazo: { label: "Prazo", tipo: "text", obrigatorio: true },
  parte1: { label: "Primeira Parte", tipo: "text", obrigatorio: true },
  parte2: { label: "Segunda Parte", tipo: "text", obrigatorio: true },
  locador: { label: "Locador", tipo: "text", obrigatorio: true },
  locatario: { label: "Locatário", tipo: "text", obrigatorio: true },
  imovel: { label: "Imóvel", tipo: "textarea", obrigatorio: true },
  valor_aluguel: { label: "Valor Aluguel", tipo: "number", obrigatorio: true },
  vendedor: { label: "Vendedor", tipo: "text", obrigatorio: true },
  comprador: { label: "Comprador", tipo: "text", obrigatorio: true },
  bem: { label: "Bem/Produto", tipo: "textarea", obrigatorio: true },
  empresa: { label: "Empresa", tipo: "text", obrigatorio: true },
  plataforma: { label: "Plataforma", tipo: "text", obrigatorio: false },
  tratamento_dados: { label: "Tratamento de Dados", tipo: "textarea", obrigatorio: false },
  titular: { label: "Titular", tipo: "text", obrigatorio: false },
  finalidade: { label: "Finalidade", tipo: "textarea", obrigatorio: false },
  credor: { label: "Credor", tipo: "text", obrigatorio: true },
  devedor: { label: "Devedor", tipo: "text", obrigatorio: true },
  valor_total: { label: "Valor Total", tipo: "number", obrigatorio: true },
  parcelas: { label: "Parcelas", tipo: "number", obrigatorio: false },
  valor_divida: { label: "Valor Dívida", tipo: "number", obrigatorio: true },
  notificante: { label: "Notificante", tipo: "text", obrigatorio: true },
  notificado: { label: "Notificado", tipo: "text", obrigatorio: true },
  valor_devido: { label: "Valor Devido", tipo: "number", obrigatorio: false },
  motivo: { label: "Motivo", tipo: "textarea", obrigatorio: false },
  obrigacao_descumprida: { label: "Obrigação Descumprida", tipo: "textarea", obrigatorio: false },
  contrato_original: { label: "Contrato Original", tipo: "textarea", obrigatorio: true },
  objeto_conflito: { label: "Objeto Conflito", tipo: "textarea", obrigatorio: false },
  condicoes: { label: "Condições", tipo: "textarea", obrigatorio: false },
  clausulas: { label: "Cláusulas", tipo: "textarea", obrigatorio: false },
  responsavel: { label: "Responsável", tipo: "text", obrigatorio: false },
  aceitante: { label: "Aceitante", tipo: "text", obrigatorio: false },
  parte_reveladora: { label: "Parte Reveladora", tipo: "text", obrigatorio: false },
  parte_receptora: { label: "Parte Receptora", tipo: "text", obrigatorio: false },
  empregador: { label: "Empregador", tipo: "text", obrigatorio: false },
  empregado: { label: "Empregado", tipo: "text", obrigatorio: false },
  cargo: { label: "Cargo", tipo: "text", obrigatorio: false },
  salario: { label: "Salário", tipo: "number", obrigatorio: false },
  quem_representa: { label: "Quem você representa? (Apelante)", tipo: "text", obrigatorio: true, placeholder: "Ex: Autor da ação, Réu, Empresa X...", dica: "Fundamental para a IA saber se deve atacar ou defender a condenação." },
  resumo_sentenca: { label: "Resumo da Sentença (Decisão do Juiz)", tipo: "textarea", obrigatorio: true, dica: "Faça o Upload da Sentença na etapa anterior ou cole aqui o que o juiz decidiu." },
  sintese_inicial: { label: "Síntese da Petição Inicial", tipo: "textarea", obrigatorio: true, dica: "Resuma brevemente o que foi pedido lá no começo do processo (como a Eduarda sugeriu)." },
};

// LISTA COMPLETA DE PEÇAS
const PECAS_JURIDICAS = {
  civil: {
    nome: "Peças Cíveis",
    icon: "building",
    pecas: [
      { id: "peticao_inicial", nome: "Petição Inicial", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "autor_qualificacao", "reu", "reu_qualificacao", "fatos", "danos_materiais", "danos_morais", "fundamentos", "pedidos", "valor_causa"] },
      { id: "acao_monitoria", nome: "Ação Monitória", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos", "valor_causa"] },
      { id: "execucao", nome: "Execução", camada: "INICIAL", modelo: "EXECUCAO", uploadObrigatorio: false, campos: ["enderecamento", "autor", "reu", "fatos", "fundamentos", "pedidos", "valor_causa"] },
      { id: "contestacao_civel", nome: "Contestação", camada: "DEFESA", modelo: "DEFESA", uploadObrigatorio: true, arquivoNecessario: "Petição Inicial", campos: ["numero_processo", "preliminares", "impugnacao_fatos", "teses_defesa"] },
      { id: "replica_civel", nome: "Réplica", camada: "DEFESA", modelo: "REPLICA", uploadObrigatorio: true, arquivoNecessario: "Contestação", campos: ["numero_processo", "autor", "refutacao"] },
      { id: "embargos_declaracao", nome: "Embargos de Declaração", camada: "RECURSO", modelo: "RECURSO", uploadObrigatorio: true, arquivoNecessario: "Decisão", campos: ["numero_processo", "fundamentos_recurso"] },
      { id: "apelacao_civel", nome: "Apelação", camada: "RECURSO", modelo: "RECURSO_APELACAO", uploadObrigatorio: true, arquivoNecessario: "Sentença (PDF/DOCX)", campos: ["enderecamento", "numero_processo", "quem_representa", "sintese_inicial", "resumo_sentenca", "preliminares", "teses_defesa"] },   
      { id: "agravo_instrumento", nome: "Agravo de Instrumento", camada: "RECURSO", modelo: "RECURSO_AGRAVO", uploadObrigatorio: true, arquivoNecessario: "Decisão Agravada (PDF)", campos: ["enderecamento", "numero_processo", "quem_representa", "resumo_fatos", "resumo_sentenca", "teses_defesa", "pedidos"]},    
      { id: "manifestacao_processual", nome: "Manifestação", camada: "INCIDENTAL", modelo: "INCIDENTE", uploadObrigatorio: true, arquivoNecessario: "Peça Anterior", campos: ["numero_processo", "fatos"] },
      { id: "tutela_urgencia", nome: "Pedido de Tutela de Urgência", camada: "INCIDENTAL", modelo: "INCIDENTE", uploadObrigatorio: false, campos: ["autor", "fatos", "fundamentos", "pedidos"] },
      { id: "cumprimento_sentenca", nome: "Cumprimento de Sentença", camada: "INCIDENTAL", modelo: "EXECUCAO", uploadObrigatorio: true, arquivoNecessario: "Sentença", campos: ["numero_processo", "autor", "reu", "fatos", "pedidos"] },
    ]
  },
  imobiliario: {
    nome: "Peças Imobiliárias",
    icon: "building",
    pecas: [
      { id: "acao_despejo", nome: "Ação de Despejo", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos"] },
      { id: "cobranca_aluguel", nome: "Ação de Cobrança de Aluguel", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos", "valor_causa"] },
      { id: "usucapiao", nome: "Ação de Usucapião", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "fatos", "fundamentos", "pedidos", "valor_causa"] },
      { id: "reintegracao_posse", nome: "Ação de Reintegração de Posse", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos"] },
    ]
  },
  consumidor: {
    nome: "Direito do Consumidor",
    icon: "shield",
    pecas: [
      { id: "indenizacao_moral", nome: "Ação de Indenização (Moral)", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "danos_morais", "fundamentos", "pedidos", "valor_causa"] },
      { id: "obrigacao_fazer", nome: "Ação de Obrigação de Fazer", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos"] },
    ]
  },
  empresarial: {
    nome: "Direito Empresarial",
    icon: "briefcase",
    pecas: [
      { id: "dissolucao_societaria", nome: "Ação de Dissolução Societária", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos", "valor_causa"] },
      { id: "cobranca_empresarial", nome: "Ação de Cobrança Empresarial", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos", "valor_causa"] },
    ]
  },
  trabalhista: {
    nome: "Peças Trabalhistas",
    icon: "briefcase",
    pecas: [
      { id: "reclamacao_trabalhista", nome: "Reclamação Trabalhista", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "autor_qualificacao", "reu", "fatos", "fundamentos", "pedidos"] },
      { id: "contestacao_trabalhista", nome: "Contestação Trabalhista", camada: "DEFESA", modelo: "DEFESA", uploadObrigatorio: true, arquivoNecessario: "Reclamação", campos: ["numero_processo", "impugnacao_fatos", "teses_defesa"] },
    ]
  },
  criminal: {
    nome: "Peças Criminais",
    icon: "scale",
    pecas: [
      { id: "resposta_acusacao", nome: "Resposta à Acusação", camada: "DEFESA", modelo: "DEFESA", uploadObrigatorio: true, arquivoNecessario: "Denúncia", campos: ["numero_processo", "impugnacao_fatos", "teses_defesa"] },
      { id: "habeas_corpus", nome: "Habeas Corpus", camada: "INCIDENTAL", modelo: "CONSTITUCIONAL", uploadObrigatorio: false, campos: ["autor", "fatos", "fundamentos", "pedidos"] },
    ]
  },
  previdenciario: {
    nome: "Peças Previdenciárias",
    icon: "shield",
    pecas: [
      { id: "peticao_previdenciaria", nome: "Petição Inicial Previdenciária", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "autor", "fatos", "fundamentos", "pedidos"] },
    ]
  },
  administrativo: {
    nome: "Direito Administrativo",
    icon: "building",
    pecas: [
      { id: "peticao_administrativa", nome: "Petição Administrativa", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "autor", "fatos", "fundamentos", "pedidos"] },
    ]
  },
  familia: {
    nome: "Direito de Família",
    icon: "users",
    pecas: [
      { id: "acao_divorcio", nome: "Ação de Divórcio", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos"] },
      { id: "acao_alimentos", nome: "Ação de Alimentos", camada: "INICIAL", modelo: "PETICAO_INICIAL", uploadObrigatorio: false, campos: ["enderecamento", "nome_acao", "autor", "reu", "fatos", "fundamentos", "pedidos"] },
    ]
  },
  contratos: {
    nome: "Contratos",
    icon: "file-text",
    subtipos: {
      contratos_classicos: {
        nome: "Contratos Clássicos",
        descricao: "Relação jurídica com obrigações entre partes",
        pecas: [
          { id: "contrato_prestacao_servicos", nome: "Contrato de Prestação de Serviços", camada: "EXTRAJUDICIAL", modelo: "CONTRATUAL", uploadObrigatorio: false, campos: ["contratante", "contratado", "objeto", "valor", "prazo"] },
          { id: "contrato_compra_venda", nome: "Contrato de Compra e Venda", camada: "EXTRAJUDICIAL", modelo: "CONTRATUAL", uploadObrigatorio: false, campos: ["vendedor", "comprador", "bem", "valor"] },
          { id: "contrato_locacao", nome: "Contrato de Locação", camada: "EXTRAJUDICIAL", modelo: "CONTRATUAL", uploadObrigatorio: false, campos: ["locador", "locatario", "imovel", "valor_aluguel", "prazo"] },
        ]
      },
      termos: {
        nome: "Termos",
        descricao: "Documentos unilaterais ou de adesão",
        pecas: [
          { id: "termos_uso", nome: "Termos de Uso", camada: "EXTRAJUDICIAL", modelo: "TERMO", uploadObrigatorio: false, campos: ["empresa", "plataforma", "clausulas"] },
          { id: "politica_privacidade", nome: "Política de Privacidade", camada: "EXTRAJUDICIAL", modelo: "TERMO", uploadObrigatorio: false, campos: ["empresa", "tratamento_dados"] },
        ]
      },
      acordos: {
        nome: "Acordos",
        descricao: "Ajustes para encerrar ou prevenir conflitos",
        pecas: [
          { id: "acordo_extrajudicial", nome: "Acordo Extrajudicial", camada: "EXTRAJUDICIAL", modelo: "ACORDO", uploadObrigatorio: false, campos: ["parte1", "parte2", "valor_total", "objeto_conflito", "condicoes"] },
          { id: "acordo_pagamento", nome: "Acordo de Pagamento", camada: "EXTRAJUDICIAL", modelo: "ACORDO", uploadObrigatorio: false, campos: ["credor", "devedor", "valor_total", "parcelas"] },
        ]
      },
      distratos: {
        nome: "Distratos",
        descricao: "Encerramento de contratos existentes",
        pecas: [
          { id: "distrato_generico", nome: "Distrato (Genérico)", camada: "EXTRAJUDICIAL", modelo: "DISTRATO", uploadObrigatorio: false, campos: ["parte1", "parte2", "contrato_original"] },
        ]
      },
      notificacoes: {
        nome: "Notificações Extrajudiciais",
        descricao: "Comunicação formal com efeito jurídico",
        pecas: [
          { id: "notificacao_cobranca", nome: "Notificação de Cobrança", camada: "EXTRAJUDICIAL", modelo: "NOTIFICACAO", uploadObrigatorio: false, campos: ["notificante", "notificado", "valor_devido"] },
          { id: "notificacao_rescisao", nome: "Notificação para Rescisão", camada: "EXTRAJUDICIAL", modelo: "NOTIFICACAO", uploadObrigatorio: false, campos: ["notificante", "notificado", "motivo"] },
        ]
      }
    }
  }
};

const STEPS_POR_MODELO = {
  PETICAO_INICIAL: [
    { id: 1, titulo: "Endereçamento e Qualificação", descricao: "Para quem vai e quem são as partes?", campos: ["enderecamento", "nome_acao", "autor", "autor_qualificacao", "reu", "reu_qualificacao"], icon: Users },
    { id: 2, titulo: "Narrativa dos Fatos", descricao: "Descreva o que aconteceu", campos: ["fatos", "danos_materiais", "danos_morais"], icon: FileText, dica: "💡 Detalhe bem os fatos. A IA usará este texto para construir a tese jurídica completa." },
    { id: 3, titulo: "Direito e Pedidos", descricao: "Fundamentação jurídica", campos: ["fundamentos", "pedidos", "valor_causa"], icon: Scale }
  ],
  DEFESA: [
    { id: 1, titulo: "Análise da Inicial", descricao: "Upload da Petição do Autor", campos: [], acao: "analisar_upload", icon: Upload },
    { id: 2, titulo: "Processo e Partes", descricao: "Número e Qualificação", campos: ["enderecamento", "numero_processo", "reu", "reu_qualificacao", "autor", "autor_qualificacao"], icon: Users },
    { id: 3, titulo: "Fatos e Preliminares", descricao: "Síntese e Defesas Processuais", campos: ["resumo_fatos", "preliminares"], icon: FileText },
    { id: 4, titulo: "Mérito e Direito", descricao: "Teses de Defesa", campos: ["teses_defesa", "provas", "pedidos"], icon: Shield, dica: "A IA vai usar suas teses para escrever o tópico 'Do Direito' completo com artigos de lei." }
  ],
  EXECUCAO: [
    { id: 1, titulo: "Partes", descricao: "Exequente e Executado", campos: ["enderecamento", "autor", "reu"], icon: Users },
    { id: 2, titulo: "Título e Dívida", descricao: "O que está sendo cobrado?", campos: ["fatos", "fundamentos", "pedidos", "valor_causa"], icon: FileText }
  ],
  REPLICA: [
    { id: 1, titulo: "Análise da Contestação", descricao: "Upload da contestação adversa", campos: [], acao: "analisar_upload", icon: Upload },
    { id: 2, titulo: "Refutação", descricao: "Contra-argumentos", campos: ["refutacao"], icon: Zap }
  ],
  RECURSO: [
    { id: 1, titulo: "Análise da Decisão", descricao: "Upload da sentença/decisão", campos: [], acao: "analisar_upload", icon: Upload },
    { id: 2, titulo: "Fundamentos do Recurso", descricao: "Por que a decisão está errada?", campos: ["fundamentos_recurso"], icon: Brain }
  ],
  CONTRATUAL: [
    { id: 1, titulo: "Partes Contratantes", descricao: "Quem assina o contrato?", campos: ["contratante", "contratado"], icon: Users },
    { id: 2, titulo: "Objeto e Condições", descricao: "O que está sendo contratado?", campos: ["objeto", "valor", "prazo"], icon: FileText }
  ],
  TERMO: [
    { id: 1, titulo: "Identificação", descricao: "Empresa/Responsável", campos: ["empresa"], icon: Building },
    { id: 2, titulo: "Conteúdo do Termo", descricao: "Dados e condições", campos: ["tratamento_dados", "finalidade"], icon: FileText }
  ],
  ACORDO: [
    { id: 1, titulo: "Partes do Acordo", descricao: "Quem está acordando?", campos: ["parte1", "parte2"], icon: Users },
    { id: 2, titulo: "Condições do Acordo", descricao: "Valores e pagamento", campos: ["valor_total", "parcelas"], icon: FileText }
  ],
  DISTRATO: [
    { id: 1, titulo: "Partes do Distrato", descricao: "Quem está encerrando o contrato?", campos: ["parte1", "parte2"], icon: Users },
    { id: 2, titulo: "Contrato Original", descricao: "Qual contrato será desfeito?", campos: ["contrato_original"], icon: FileText }
  ],
  NOTIFICACAO: [
    { id: 1, titulo: "Identificação", descricao: "Quem notifica quem?", campos: ["notificante", "notificado"], icon: Users },
    { id: 2, titulo: "Motivo da Notificação", descricao: "Por que está notificando?", campos: ["valor_devido", "motivo", "obrigacao_descumprida"], icon: AlertCircle }
  ],
  INCIDENTE: [
    { id: 1, titulo: "Dados do Processo", descricao: "Processo em andamento", campos: ["numero_processo"], icon: FileText },
    { id: 2, titulo: "Fundamentação", descricao: "Por que esse pedido?", campos: ["fatos", "fundamentos", "pedidos"], icon: Brain }
  ],
  CONSTITUCIONAL: [
    { id: 1, titulo: "Identificação", descricao: "Paciente/Impetrante", campos: ["autor"], icon: Users },
    { id: 2, titulo: "Fundamentação", descricao: "Violação de direitos", campos: ["fatos", "fundamentos", "pedidos"], icon: Scale }
  ],
  RECURSO_APELACAO: [
    { 
      id: 1, 
      titulo: "Análise da Sentença", 
      descricao: "Upload da Decisão do Juiz", 
      campos: [], 
      acao: "analisar_upload", 
      icon: Upload 
    },
    { 
      id: 2, 
      titulo: "Processo e Partes", 
      descricao: "Identificação", 
      campos: ["enderecamento", "numero_processo", "quem_representa"], 
      icon: Users 
    },
    { 
      id: 3, 
      titulo: "Fatos Processuais", 
      descricao: "Inicial e Sentença", 
      campos: ["sintese_inicial", "resumo_sentenca", "preliminares"], 
      icon: FileText,
      dica: "A IA vai cruzar o resumo da inicial com a sentença para achar as falhas."
    },
    { 
      id: 4, 
      titulo: "Razões Recursais", 
      descricao: "Por que reformar?", 
      campos: ["teses_defesa", "pedidos"], 
      icon: Scale,
      dica: "Aqui entra a IA confrontando juridicamente a decisão."
    }
  ],
  RECURSO_AGRAVO: [
    { 
      id: 1, 
      titulo: "Decisão Agravada", 
      descricao: "Upload da decisão que você quer atacar", 
      campos: [], 
      acao: "analisar_upload", 
      icon: Upload 
    },
    { 
      id: 2, 
      titulo: "Partes e Processo", 
      descricao: "Quem você representa?", 
      campos: ["enderecamento", "numero_processo", "quem_representa"], 
      icon: Users 
    },
    { 
      id: 3, 
      titulo: "Histórico e Decisão", 
      descricao: "Resumo do Processo e da Decisão", 
      campos: ["resumo_fatos", "resumo_sentenca"], 
      icon: FileText,
      dica: "A IA vai cruzar o seu resumo do processo com a decisão do juiz."
    },
    { 
      id: 4, 
      titulo: "Razões do Agravo", 
      descricao: "Teses de Reforma", 
      campos: ["teses_defesa", "pedidos"], 
      icon: Scale,
      dica: "Foco na urgência (Efeito Suspensivo)."
    }
  ],
};

const ValorCausaValidator = ({ valor }) => {
  const salarioMinimo = 1412;
  const limiteJEC = 40 * salarioMinimo;
  
  if (valor <= 20 * salarioMinimo) {
    return <div className="mt-2 p-3 bg-blue-50 border border-blue-200 rounded text-sm text-blue-700">✅ <strong>Juizado Especial Cível</strong> - Sem necessidade de advogado</div>;
  } else if (valor <= limiteJEC) {
    return <div className="mt-2 p-3 bg-green-50 border border-green-200 rounded text-sm text-green-700">✅ <strong>Juizado Especial Cível</strong> - Necessário advogado</div>;
  } else {
    return <div className="mt-2 p-3 bg-yellow-50 border border-yellow-200 rounded text-sm text-yellow-700">⚠️ <strong>Vara Cível Comum</strong> - Valor acima do limite do JEC (R$ {limiteJEC.toLocaleString('pt-BR')})</div>;
  }
};

const Stepper = ({ steps, currentStep, onStepClick }) => {
  return (
    // Ajuste Responsivo: overflow-x-auto para scroll horizontal no mobile
    <div className="flex items-center justify-start md:justify-between mb-8 md:mb-12 relative overflow-x-auto pb-4 gap-4 px-2 no-scrollbar">
        {/* Linha escondida no mobile para não atrapalhar */}
        <div className="hidden md:block absolute h-[2px] bg-gray-200 top-[30px] left-10 right-10 z-0"></div>
      {steps.map((step, index) => {
        const Icon = step.icon || FileText;
        const isActive = currentStep === index;
        const isCompleted = currentStep > index;
        
        return (
          // min-w para garantir que não amasse no mobile
          <div key={step.id} className="flex-none min-w-[100px] md:min-w-0 md:flex-1 flex flex-col items-center z-10 relative">
              <button
                onClick={() => onStepClick(index)}
                className={`w-12 h-12 md:w-16 md:h-16 rounded-full border-2 flex items-center justify-center transition-all mb-2 md:mb-3 shadow-sm ${
                  isActive ? 'bg-gold border-gold text-white shadow-md scale-110' : isCompleted ? 'bg-green-600 border-green-600 text-white' : 'bg-white border-gray-300 text-gray-400 hover:border-gold hover:text-gold'
                }`}
              >
                {isCompleted ? <CheckCircle size={20} className="md:w-7 md:h-7" /> : <Icon size={20} className="md:w-7 md:h-7" />}
              </button>
              <div className="text-center">
                <p className={`font-bold text-xs md:text-sm font-serif ${isActive ? 'text-gold' : 'text-primary'}`}>{step.titulo}</p>
                {/* Esconde descrição no mobile */}
                <p className="text-[10px] md:text-xs text-secondary mt-1 hidden md:block">{step.descricao}</p>
              </div>
          </div>
        );
      })}
    </div>
  );
};

const FormField = ({ campo, config, value, onChange, erro }) => {
  if (!config) return null;
  return (
    <div className="mb-6">
      <label className="block text-primary font-bold mb-3 text-sm uppercase tracking-wider">
        {config.label}
        {config.obrigatorio && <span className="text-red-500 ml-1">*</span>}
      </label>
      {config.dica && <p className="text-xs text-secondary mb-2 italic flex items-center gap-1"><AlertCircle size={12}/> {config.dica}</p>}
      {config.tipo === 'textarea' ? (
        <textarea rows={5} value={value || ''} onChange={(e) => onChange(campo, e.target.value)} placeholder={config.placeholder} className={`input-premium ${erro ? 'border-red-500 bg-red-50' : ''}`} required={config.obrigatorio} />
      ) : (
        <input type={config.tipo} value={value || ''} onChange={(e) => onChange(campo, e.target.value)} placeholder={config.placeholder} className={`input-premium ${erro ? 'border-red-500 bg-red-50' : ''}`} required={config.obrigatorio} />
      )}
      {erro && <p className="text-red-500 text-xs mt-2 flex items-center gap-1"><XCircle size={12}/> {erro}</p>}
      {campo === 'valor_causa' && value && <ValorCausaValidator valor={parseFloat(value)} />}
    </div>
  );
};

// ============================================================================
// 4. COMPONENTE PRINCIPAL (APP)
// ============================================================================

function App() {
  const [tela, setTela] = useState('home');
  const [modoFoco, setModoFoco] = useState(false);
  const [areaSelecionada, setAreaSelecionada] = useState(null);
  const [subtipoSelecionado, setSubtipoSelecionado] = useState(null);
  const [pecaSelecionada, setPecaSelecionada] = useState(null);
  const [processoExiste, setProcessoExiste] = useState(null);
  const [numeroProcesso, setNumeroProcesso] = useState('');
  const [currentStep, setCurrentStep] = useState(0);
  const [formData, setFormData] = useState({});
  const [errosValidacao, setErrosValidacao] = useState({});
  const [documentoGerado, setDocumentoGerado] = useState('');
  const [modoEdicao, setModoEdicao] = useState(false);
  const [loading, setLoading] = useState(false);
  const [statusIA, setStatusIA] = useState('');
  const [arquivoUpload, setArquivoUpload] = useState(null);
  
  // Estados Extras (Jurisprudência/Histórico/Config)
  const [modalJurisprudencia, setModalJurisprudencia] = useState(false);
  const [buscaJurisprudencia, setBuscaJurisprudencia] = useState('');
  const [jurisprudencias, setJurisprudencias] = useState([]);
  const [loadingJurisprudencia, setLoadingJurisprudencia] = useState(false);
  const [historico, setHistorico] = useState([]);
  const [jurisFavoritas, setJurisFavoritas] = useState([]);
  
  // ESTADO MOBILE
  const [menuMobileAberto, setMenuMobileAberto] = useState(false);

  const [configCabecalho, setConfigCabecalho] = useState(() => {
    const salvo = localStorage.getItem('dados_escritorio');
    return salvo ? JSON.parse(salvo) : {
      nome: 'NOGUEIRA ADVOCACIA',
      oab: 'OAB/SP 000.000',
      endereco: 'Avenida Paulista, 1000',
      cidade: 'São Paulo',
      estado: 'SP',
      cep: '01310-100',
      telefone: '(11) 99999-9999',
      email: 'contato@nogueira.adv.br',
      logoBase64: null
    };
  });
  
  // --- BLOCO NOVO: ESCUTA O DJANGO (IFRAME) ---
  useEffect(() => {
    const receberDadosIA = (event) => {
      // Verifica se a mensagem veio do nosso sistema (ação: IMPORTAR_IA)
      if (event.data && event.data.acao === 'IMPORTAR_IA') {
        const { fatos, estrategia, riscos } = event.data;
        
        console.log("Recebido do Django:", event.data);

        // Preenche o formulário automaticamente!
        setFormData(prev => ({
          ...prev,
          // Preenche os Fatos
          fatos: fatos, 
          impugnacao_fatos: fatos, // Caso seja defesa
          
          // Preenche o Direito/Estratégia (Junta Estratégia + Riscos)
          fundamentos: estrategia + '\n\n' + riscos,
          teses_defesa: estrategia + '\n\n=== PONTOS DE ATENÇÃO ===\n' + riscos,
          fundamentos_recurso: estrategia
        }));

        // Avisa e direciona
        alert("✨ Análise da IA importada com sucesso!\n\nSelecione agora qual peça jurídica você deseja criar com esses dados.");
        setTela('pecas'); // Manda para a escolha de peças
      }
    };

    window.addEventListener('message', receberDadosIA);
    return () => window.removeEventListener('message', receberDadosIA);
  }, []);
  // ---------------------------------------------

  const salvarConfiguracoesEscritorio = () => {
    localStorage.setItem('dados_escritorio', JSON.stringify(configCabecalho));
    alert('✅ Configurações salvas com sucesso!');
    voltarHome();
  };

  useEffect(() => {
    const hist = localStorage.getItem('historico_documentos');
    if (hist) setHistorico(JSON.parse(hist));
    const fav = localStorage.getItem('jurisprudencias_favoritas');
    if (fav) setJurisFavoritas(JSON.parse(fav));
  }, []);

  const voltarHome = () => {
    setTela('home');
    setAreaSelecionada(null);
    setPecaSelecionada(null);
    setCurrentStep(0);
    setFormData({});
    setDocumentoGerado('');
    setModoFoco(false);
    setProcessoExiste(null);
    setNumeroProcesso('');
    setSubtipoSelecionado(null);
  };

  // Funções de Navegação
  const handleAreaClick = (areaKey) => {
    setAreaSelecionada({ key: areaKey, ...PECAS_JURIDICAS[areaKey] });
    setProcessoExiste(null);
    setNumeroProcesso('');
    setSubtipoSelecionado(null);
    if (areaKey === 'contratos') setTela('subtipos_contratos');
    else setTela('tela_zero');
  };

  const handleConfirmarTelaZero = () => {
    if (processoExiste === null) { alert('⚠️ Por favor, responda se o processo já existe.'); return; }
    setTela('pecas');
  };

  const handlePecaClick = (peca) => {
    setPecaSelecionada(peca);
    setFormData({ numero_processo: numeroProcesso });
    setDocumentoGerado('');
    setArquivoUpload(null);
    setCurrentStep(0);
    setTela('formulario');
  };

  const handleInputChange = (campo, valor) => {
      setFormData(prev => ({ ...prev, [campo]: valor }));
      if (errosValidacao[campo]) {
        setErrosValidacao(prev => { const novos = { ...prev }; delete novos[campo]; return novos; });
      }
  };

// 🔥 GERAÇÃO DO DOCUMENTO (VERSÃO FINAL COMPLETA E CORRIGIDA)
  const gerarDocumentoPorModelo = (modelo, dadosAtuais = formData) => {
    
    // 1. DADOS COMUNS PADRONIZADOS
    const ENDERECAMENTO = dadosAtuais.enderecamento 
        ? dadosAtuais.enderecamento.toUpperCase() 
        : 'EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA ____ VARA CÍVEL DA COMARCA DE...';
        
    const NOME_ACAO = dadosAtuais.nome_acao 
        ? dadosAtuais.nome_acao.toUpperCase() 
        : 'AÇÃO...';

    const DATA_HOJE = new Date().toLocaleDateString('pt-BR');
    
    const ASSINATURA = `
${configCabecalho.cidade}/${configCabecalho.estado}, ${DATA_HOJE}

________________________________________________
${configCabecalho.nome}
${configCabecalho.oab}`;

    if (modelo === 'PETICAO_INICIAL') {
      return `
${ENDERECAMENTO}

${dadosAtuais.numero_processo ? `Processo nº ${dadosAtuais.numero_processo}` : '(Espaço para Protocolo / Distribuição)'}

${dadosAtuais.autor}, ${dadosAtuais.autor_qualificacao || 'qualificação completa...'}, por seu advogado que esta subscreve, vem, respeitosamente, à presença de Vossa Excelência, propor a presente

${NOME_ACAO}

em face de ${dadosAtuais.reu}, ${dadosAtuais.reu_qualificacao || 'qualificação completa...'}, pelos motivos de fato e de direito a seguir aduzidos:

I - DOS FATOS
${dadosAtuais.fatos || '[A IA irá descrever os fatos aqui...]'}

${dadosAtuais.danos_materiais || dadosAtuais.danos_morais ? 'II - DOS DANOS' : ''}
${dadosAtuais.danos_materiais ? `\nDo Dano Material: ${dadosAtuais.danos_materiais}` : ''}
${dadosAtuais.danos_morais ? `\nDo Dano Moral: ${dadosAtuais.danos_morais}` : ''}

III - DO DIREITO
${dadosAtuais.fundamentos || '[A fundamentação jurídica será inserida aqui...]'}

IV - DOS PEDIDOS
Diante do exposto, requer:

${dadosAtuais.pedidos || 'a) A citação do Réu;\nb) A procedência total da ação;\nc) A condenação em custas e honorários.'}

Dá-se à causa o valor de R$ ${dadosAtuais.valor_causa || '0,00'}.

Nestes termos,
Pede deferimento.

${ASSINATURA}
`;
    }

    
    if (modelo === 'DEFESA') {
      const textoProvas = dadosAtuais.provas || "o depoimento pessoal do Autor, oitiva de testemunhas e juntada de novos documentos";
      const blocoPreliminares = dadosAtuais.preliminares ? `II - DAS PRELIMINARES\n${dadosAtuais.preliminares}\n` : '';

      return `
${ENDERECAMENTO}

Processo nº ${dadosAtuais.numero_processo}

${dadosAtuais.reu}, ${dadosAtuais.reu_qualificacao || 'já qualificado nos autos em epígrafe'}, por seu advogado infra-assinado, vem, respeitosamente, à presença de Vossa Excelência, apresentar:

CONTESTAÇÃO

Em face da Ação movida por ${dadosAtuais.autor}, ${dadosAtuais.autor_qualificacao || 'já qualificado'}, pelos motivos de fato e de direito a seguir aduzidos:

I - SÍNTESE DA INICIAL E REALIDADE DOS FATOS
${dadosAtuais.resumo_fatos || dadosAtuais.impugnacao_fatos || '[Resumo dos fatos...]'}

${blocoPreliminares}

III - DO MÉRITO (FUNDAMENTAÇÃO DA DEFESA)
${dadosAtuais.teses_defesa || dadosAtuais.fundamentos || '[Tese de defesa...]'}

IV - DOS PEDIDOS
Diante de todo o exposto, requer:
${dadosAtuais.pedidos || '- O acolhimento das preliminares;\n- A TOTAL IMPROCEDÊNCIA da ação;\n- A condenação do Autor em sucumbência.'}

Protesta provar o alegado por todos os meios em direito admitidos, especialmente ${textoProvas}.

Nestes termos,
Pede deferimento.

${ASSINATURA}
`;
    }

    if (modelo === 'EXECUCAO') {
      return `
${ENDERECAMENTO}

EXECUÇÃO DE TÍTULO EXTRAJUDICIAL

EXEQUENTE: ${dadosAtuais.autor}
EXECUTADO: ${dadosAtuais.reu}

I - DOS FATOS (DÍVIDA)
${dadosAtuais.fatos}

II - DO DIREITO
${dadosAtuais.fundamentos}

III - DOS PEDIDOS
${dadosAtuais.pedidos}

Dá-se à causa o valor de R$ ${dadosAtuais.valor_causa || '0,00'}.

${ASSINATURA}
`;
    }

    if (modelo === 'RECURSO' || modelo === 'RECURSO_APELACAO') {
        const NOME_RECURSO = pecaSelecionada ? pecaSelecionada.nome.toUpperCase() : 'RECURSO';
        return `
${ENDERECAMENTO}

Processo nº ${dadosAtuais.numero_processo}

${dadosAtuais.quem_representa || dadosAtuais.autor || 'APELANTE'}, já qualificado nos autos, inconformado com a r. decisão/sentença de fls., vem, respeitosamente, interpor o presente

${NOME_RECURSO}

requerendo o seu recebimento e remessa ao Egrégio Tribunal competente.

Nestes termos,
Pede deferimento.

${ASSINATURA}

---------------------------------------------------
(NOVA PÁGINA - RAZÕES DO RECURSO)

RAZÕES DO RECURSO

APELANTE: ${dadosAtuais.quem_representa || dadosAtuais.autor}
PROCESSO: ${dadosAtuais.numero_processo}

EGRÉGIO TRIBUNAL,
COLENDA CÂMARA,

I - SÍNTESE DO PROCESSO
${dadosAtuais.sintese_inicial || dadosAtuais.resumo_fatos || ''}

II - DA DECISÃO RECORRIDA
${dadosAtuais.resumo_sentenca || ''}

III - DAS RAZÕES PARA REFORMA (DO DIREITO)
${dadosAtuais.teses_defesa || dadosAtuais.fundamentos_recurso || '[Fundamentação recursal...]'}

IV - DOS PEDIDOS
Diante do exposto, requer o CONHECIMENTO e PROVIMENTO do presente recurso para reformar a decisão recorrida, conforme fundamentação supra.

${ASSINATURA}

`; 
    }
    
if (modelo === 'RECURSO_AGRAVO') {
        return `
${ENDERECAMENTO}

Processo nº ${dadosAtuais.numero_processo}

${dadosAtuais.quem_representa}, já devidamente qualificado nos autos, vem, por seu advogado, interpor o presente

AGRAVO DE INSTRUMENTO

contra a r. decisão interlocutória de fls., em face de ${dadosAtuais.reu || 'Parte Contrária'}, requerendo a remessa das razões anexas ao Egrégio Tribunal de Justiça.

Informa-se que o Agravante deixa de juntar as peças obrigatórias por se tratarem de autos eletrônicos (Art. 1.017, §5º do CPC).

Pede Deferimento.
${ASSINATURA}

---------------------------------------------------
RAZÕES DO AGRAVO DE INSTRUMENTO

AGRAVANTE: ${dadosAtuais.quem_representa}
PROCESSO DE ORIGEM: ${dadosAtuais.numero_processo}

EGRÉGIO TRIBUNAL,
COLENDA CÂMARA,

I - SÍNTESE DO PROCESSO (Resumo do Processo)
${dadosAtuais.resumo_fatos}

II - DA DECISÃO AGRAVADA
${dadosAtuais.resumo_sentenca}

III - DO DIREITO E DO PEDIDO DE EFEITO SUSPENSIVO
${dadosAtuais.teses_defesa || '[A IA fundamentará a urgência e o direito aqui...]'}

IV - DOS PEDIDOS
Ante o exposto, requer o recebimento do recurso no EFEITO SUSPENSIVO, e, ao final, o seu PROVIMENTO para reformar a r. decisão.

${ASSINATURA}
`;
}
    

    return `

${dadosAtuais.nome_acao ? dadosAtuais.nome_acao.toUpperCase() : 'CONTRATO / DOCUMENTO'}

Pelo presente instrumento particular, as partes abaixo qualificadas:

CONTRATANTE/PARTE 1: ${dadosAtuais.contratante || dadosAtuais.parte1 || dadosAtuais.autor || 'Nome da Parte 1'}, ${dadosAtuais.autor_qualificacao || ''}

CONTRATADO/PARTE 2: ${dadosAtuais.contratado || dadosAtuais.parte2 || dadosAtuais.reu || 'Nome da Parte 2'}, ${dadosAtuais.reu_qualificacao || ''}

Têm entre si justo e contratado o seguinte:

DO OBJETO
${dadosAtuais.objeto || dadosAtuais.fatos || dadosAtuais.objeto_conflito || ''}

DAS CONDIÇÕES E VALORES
${dadosAtuais.valor ? `Valor: R$ ${dadosAtuais.valor}` : ''}
${dadosAtuais.prazo ? `Prazo: ${dadosAtuais.prazo}` : ''}
${dadosAtuais.condicoes || ''}

DO FORO
As partes elegem o foro da Comarca de ${configCabecalho.cidade}/${configCabecalho.estado} para dirimir quaisquer dúvidas.

${ASSINATURA}

______________________________
Testemunha 1

______________________________
Testemunha 2
`;
};

const handleGenerar = async () => {
    // 1. Validação Básica
    if (!validarStepAtual()) { alert('⚠️ Por favor, preencha todos os campos obrigatórios.'); return; }
    if (pecaSelecionada.uploadObrigatorio && !arquivoUpload) { alert('⚠️ O upload do arquivo anterior é obrigatório para esta peça.'); return; }
    
    setLoading(true);
    setStatusIA("🤖 Fase 1/2: A IA está analisando sua defesa e formalizando a linguagem...");

    try {
        // 2. Mapeamento Inteligente: Pega o texto de onde quer que ele esteja
        // (Funciona para Inicial, Contestação, Trabalhista, etc)
        const txtFatos = formData.fatos || formData.impugnacao_fatos || formData.resumo_fatos || "";
        const txtDanos = (formData.danos_materiais || '') + ' ' + (formData.danos_morais || '');
        const txtPreliminares = formData.preliminares || "";
        
        let teseOriginal = formData.fundamentos || formData.teses_defesa || "";
        
        // Se tiver preliminares, junta na tese para a IA considerar
        if (txtPreliminares) {
            teseOriginal = `PRELIMINARES ARGUIDAS: ${txtPreliminares}\n\nTESES DE MÉRITO: ${teseOriginal}`;
        }

        let fatosMelhorados = txtFatos;
        let teseGerada = teseOriginal;

       if (txtFatos.length > 5 || teseOriginal.length > 5) {
             const res = await fetch('https://api-nogueira.onrender.com/api/gerar-tese', {
                method: 'POST', 
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ 
                    tipo_peca: pecaSelecionada.nome,
                    
                    // 👇 ADICIONE ESSA LINHA AQUI:
                    area: areaSelecionada ? areaSelecionada.key : "civil", 
                    
                    fatos: txtFatos, 
                    danos: txtDanos + " " + teseOriginal 
                })
            });
            const json = await res.json();
            
            // Pega os textos turbinados da IA
            if (json.fatos_melhorados) fatosMelhorados = json.fatos_melhorados;
            if (json.tese) teseGerada = json.tese;
            
            setStatusIA("🤖 Fase 2/2: IA finalizando a fundamentação jurídica e citações...");
        }

        // 4. Atualiza os dados para o documento final (Aqui é o pulo do gato!)
        const novosDados = { ...formData };
        
        if (pecaSelecionada.camada === 'DEFESA') {
            // Se for Contestação, salva nos campos específicos da Eduarda
            novosDados.resumo_fatos = fatosMelhorados; // Resumo formal dos fatos
            novosDados.teses_defesa = teseGerada;      // Direito robusto com artigos
        } else {
            // Se for Inicial ou outros
            novosDados.fatos = fatosMelhorados;
            novosDados.fundamentos = teseGerada;
        }
        
        // Atualiza visualmente para o usuário ver a mágica
        setFormData(novosDados);

        // 5. Gera o Documento Visual
        const docFinal = gerarDocumentoPorModelo(pecaSelecionada.modelo, novosDados);
        setDocumentoGerado(docFinal);
        
        // 6. Salva no Histórico
        const novoDoc = { 
            id: Date.now(), 
            tipo: pecaSelecionada.nome, 
            area: areaSelecionada.nome, 
            data: new Date().toLocaleString(), 
            conteudo: docFinal, 
            dados: novosDados, 
            peca: pecaSelecionada, 
            areaObj: areaSelecionada 
        };
        
        const novoHist = [novoDoc, ...historico];
        setHistorico(novoHist);
        localStorage.setItem('historico_documentos', JSON.stringify(novoHist));
        
        // 7. Abre o Editor
        setModoFoco(true);
        setModoEdicao(true);

    } catch (error) {
        console.error(error);
        alert('❌ Erro ao conectar com a IA Inteligente. Verifique sua conexão.');
    } finally {
        setLoading(false);
        setStatusIA("");
    }
  };
  // 🔥 NOVA FUNÇÃO: BOTÃO MÁGICO INDIVIDUAL (Cole logo abaixo do handleGenerar)
  const handleMagicClick = async (campoAlvo) => {
    // Pega os fatos para dar contexto pra IA
    const textoFatos = formData.fatos || formData.impugnacao_fatos || formData.resumo_fatos || "";
    
    // Se não tiver fatos escritos, avisa o usuário (a menos que ele esteja escrevendo os próprios fatos)
    if (!textoFatos && campoAlvo !== 'fatos' && campoAlvo !== 'impugnacao_fatos' && campoAlvo !== 'resumo_fatos') {
        alert("⚠️ Escreva pelo menos um resumo dos Fatos/Síntese antes para a IA ter base para trabalhar!");
        return;
    }

    setLoading(true);
    setStatusIA(`🤖 A IA está escrevendo o campo: ${campoAlvo.toUpperCase()}...`);

    try {
        const res = await fetch('https://api-nogueira.onrender.com/api/gerar-tese', {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ 
                tipo_peca: pecaSelecionada.nome, 
                fatos: textoFatos, 
                // Manda o nome do campo para a IA saber o que fazer
                campo_especifico: campoAlvo 
            })
        });
        
        const json = await res.json();
        let textoNovo = "";

        // Lógica para decidir qual texto pegar da IA (Fatos ou Direito?)
        if (['fatos', 'impugnacao_fatos', 'resumo_fatos'].includes(campoAlvo)) {
            textoNovo = json.fatos_melhorados || json.tese;
        } else {
             textoNovo = json.tese; 
        }

        // Preenche o campo sozinho na tela!
        handleInputChange(campoAlvo, textoNovo);

    } catch (error) {
        console.error(error);
        alert('Erro ao conectar com a IA.');
    } finally {
        setLoading(false);
        setStatusIA("");
    }
  };
  // Funções Auxiliares
  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setArquivoUpload(file);
    setLoading(true);
    setStatusIA("Lendo documento e extraindo dados...");
    
    try {
      const fd = new FormData();
      fd.append('arquivo', file);
      fd.append('tipo_peca', pecaSelecionada.nome);
      fd.append('campos', STEPS_POR_MODELO[pecaSelecionada.modelo]?.flatMap(s=>s.campos||[]).join(','));
      
      const res = await fetch('https://api-nogueira.onrender.com/api/extrair-documento', {method:'POST', body:fd});
      const json = await res.json();
      
      if(json.sucesso) {
         setFormData(prev=>({...prev, ...json.dados}));
         alert('✅ Leitura concluída! Dados preenchidos.');
      } else {
         alert(`⚠️ Erro na leitura: ${json.erro}`);
      }
    } catch(err) { alert('❌ Erro de conexão.'); } finally { setLoading(false); setStatusIA(""); }
  };
// 🔥 AVANÇO AUTOMÁTICO COM IA (A Mágica Invisível)
  const handleProximaEtapa = async () => {
    // 1. Valida se preencheu o atual
    if (!validarStepAtual()) return;

    const steps = STEPS_POR_MODELO[pecaSelecionada.modelo] || [];
    const stepAtualObj = steps[currentStep];
    const proximoIndex = currentStep + 1;
    
    // Se não tiver mais steps, não faz nada
    if (proximoIndex >= steps.length) return;

    const camposAtuais = stepAtualObj.campos || [];
    const camposFuturos = steps[proximoIndex].campos || [];

    // 🕵️ DETETIVE: Estamos saindo de uma tela de "Fatos" e indo para uma de "Direito"?
    const temFatosAgora = camposAtuais.some(c => ['fatos', 'resumo_fatos', 'impugnacao_fatos'].includes(c));
    const temDireitoDepois = camposFuturos.some(c => ['fundamentos', 'teses_defesa', 'pedidos'].includes(c));

    // Lógica: Se eu tenho fatos escritos AGORA, e o próximo campo de Direito está VAZIO... A IA PREENCHE!
    if (temFatosAgora && temDireitoDepois) {
        // Pega o texto dos fatos
        const txtFatos = formData.fatos || formData.impugnacao_fatos || formData.resumo_fatos || "";
        
        // Verifica qual campo de direito vamos preencher (fundamentos ou teses_defesa)
        const campoAlvo = camposFuturos.find(c => ['fundamentos', 'teses_defesa'].includes(c));
        const valorAlvo = formData[campoAlvo];

        // Só gera se tiver fatos E o destino estiver vazio (para não apagar o que você já fez)
        if (txtFatos.length > 10 && !valorAlvo) {
            setLoading(true);
            setStatusIA("⚡ Analisando seus Fatos e escrevendo a Tese Jurídica automaticamente...");

            try {
                const res = await fetch('https://api-nogueira.onrender.com/api/gerar-tese', {
                    method: 'POST', 
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ 
                        tipo_peca: pecaSelecionada.nome, 
                        fatos: txtFatos, 
                        campo_especifico: campoAlvo 
                    })
                });
                
                const json = await res.json();
                
                // Preenche o formulário silenciosamente
                if (json.tese) {
                    setFormData(prev => ({ ...prev, [campoAlvo]: json.tese }));
                }

            } catch (error) {
                console.error("Erro na automação:", error);
            } finally {
                setLoading(false);
                setStatusIA("");
            }
        }
    }

    // AVANÇA NORMALMENTE
    setCurrentStep(c => c + 1);
  };
  const buscarJurisprudencia = async () => {
    if (!buscaJurisprudencia.trim()) { alert('⚠️ Digite um tema para buscar.'); return; }
    setLoadingJurisprudencia(true);
    try {
      const response = await fetch('http://localhost:8000/api/gerar-jurisprudencia', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tema: buscaJurisprudencia, contexto: { peca: pecaSelecionada?.nome } })
      });
      const data = await response.json();
      setJurisprudencias(data.jurisprudencias || []);
    } catch (e) { alert('Erro na busca de jurisprudência.'); }
    finally { setLoadingJurisprudencia(false); }
  };

  const inserirJurisprudencia = (jurisp) => {
    const htmlJurisprudencia = `<div class="jurisprudencia-citacao"><p>"<strong>${jurisp.ementa}</strong>"</p><span class="fonte">(${jurisp.tribunal} - ${jurisp.numero}, Rel. ${jurisp.relator})</span></div><p><br/></p>`;
    const editor = document.getElementById('editor-documento');
    if (editor) { 
        editor.innerHTML += htmlJurisprudencia; 
        setDocumentoGerado(editor.innerHTML); 
    }
    setModalJurisprudencia(false);
  };

  const salvarFavorito = (jurisp) => {
    const novosFavoritos = [...jurisFavoritas, { ...jurisp, id: Date.now() }];
    setJurisFavoritas(novosFavoritos);
    localStorage.setItem('jurisprudencias_favoritas', JSON.stringify(novosFavoritos));
    alert('⭐ Jurisprudência salva nos favoritos!');
  };

  const handleDownload = async () => {
    setLoading(true);
    setStatusIA("Gerando arquivo Word formatado...");
    try {
      const res = await fetch('https://api-nogueira.onrender.com/api/gerar-docx', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ area: areaSelecionada?.nome, tipo_documento: pecaSelecionada?.nome, detalhes: {...formData, conteudo_customizado: documentoGerado}, dados_escritorio: configCabecalho })
      });
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = `${pecaSelecionada.nome}.docx`; document.body.appendChild(a); a.click(); a.remove();
    } catch(e) { alert('Erro no download'); } finally { setLoading(false); setStatusIA(""); }
  };

  const handleLogoUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => setConfigCabecalho({ ...configCabecalho, logoBase64: reader.result });
      reader.readAsDataURL(file);
    }
  };

  const handleExcluirHistorico = (id) => {
    if(window.confirm("Deseja realmente excluir este documento?")) {
        const novoHist = historico.filter(h => h.id !== id);
        setHistorico(novoHist);
        localStorage.setItem('historico_documentos', JSON.stringify(novoHist));
    }
  };

  const handleAbrirHistorico = (doc) => {
      if (doc.peca && doc.areaObj) { setAreaSelecionada(doc.areaObj); setPecaSelecionada(doc.peca); }
      setFormData(doc.dados || {});
      setDocumentoGerado(doc.conteudo);
      setModoEdicao(true);
      setModoFoco(true);
  };

  const validarStepAtual = () => {
      const steps = STEPS_POR_MODELO[pecaSelecionada.modelo] || [];
      const stepAtual = steps[currentStep];
      if (!stepAtual) return true;
      const novosErros = {};
      stepAtual.campos?.forEach(campo => {
        const config = CAMPOS_CONFIG[campo];
        if (config?.obrigatorio && !formData[campo]) {
          novosErros[campo] = 'Este campo é obrigatório.';
        }
      });
      setErrosValidacao(novosErros);
      return Object.keys(novosErros).length === 0;
  };

  // Filtro de peças para "Processo Novo" vs "Existente"
  const pecasFiltradas = areaSelecionada?.pecas?.filter(peca => {
      if (processoExiste === false) {
          return peca.camada === "INICIAL";
      }
      return true;
  }) || [];

  // ============================================================================
  // RENDERIZAÇÃO DA INTERFACE (HTML)
  // ============================================================================
  return (
    <div className="flex h-screen bg-main text-primary font-sans overflow-hidden relative flex-col md:flex-row">
      <style>{fontStyles}</style>

      {/* OVERLAY DE LOADING COM STATUS DA IA */}
      {loading && (
        <div className="fixed inset-0 bg-black/80 z-[60] flex flex-col items-center justify-center text-white backdrop-blur-sm">
            <Loader size={64} className="animate-spin text-gold mb-6"/>
            <h2 className="text-2xl font-serif font-bold mb-2">Trabalhando...</h2>
            <p className="text-gray-300 animate-pulse text-lg">{statusIA || "Processando..."}</p>
        </div>
      )}

      {/* HEADER MOBILE (APENAS VISÍVEL NO CELULAR) */}
      {!modoFoco && (
        <div className="md:hidden flex items-center justify-between p-4 bg-white border-b border-light shadow-sm z-30 shrink-0">
           <div className="flex items-center gap-3">
             <div className="w-8 h-8 rounded-full bg-gradient-gold flex items-center justify-center text-white text-xs shadow-md">
               EN
             </div>
             <span className="font-serif font-bold text-lg text-primary">Eduarda Nogueira</span>
           </div>
           <button onClick={() => setMenuMobileAberto(!menuMobileAberto)} className="text-primary p-2">
             {menuMobileAberto ? <XCircle className="text-secondary"/> : <Menu className="text-primary"/>}
           </button>
        </div>
      )}

      {/* SIDEBAR (MENU LATERAL RESPONSIVO) */}
      {!modoFoco && (
        <>
          {/* Overlay escuro para mobile quando menu aberto */}
          <div 
            className={`fixed inset-0 bg-black/60 z-40 transition-opacity md:hidden ${menuMobileAberto ? 'opacity-100' : 'opacity-0 pointer-events-none'}`} 
            onClick={() => setMenuMobileAberto(false)}
          />

          <div className={`
            fixed md:static top-0 left-0 h-full z-50 w-72 bg-white border-r border-light flex flex-col shadow-2xl md:shadow-sm transform transition-transform duration-300 ease-in-out
            ${menuMobileAberto ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
          `}>
            {/* Botão Fechar no Mobile dentro da Sidebar */}
            <button onClick={() => setMenuMobileAberto(false)} className="absolute top-4 right-4 md:hidden text-secondary p-2"><XCircle size={24}/></button>

            <div className="p-8 border-b border-light text-center">
              <div className="w-24 h-24 rounded-full p-[3px] bg-gradient-gold mb-4 mx-auto shadow-md">
                {configCabecalho.logoBase64 ? <img src={configCabecalho.logoBase64} className="w-full h-full rounded-full object-cover border-2 border-white" alt="Logo" /> : <div className="w-full h-full rounded-full bg-white flex items-center justify-center text-gold"><Scale size={36}/></div>}
              </div>
              <h2 className="font-serif text-2xl text-primary font-bold">Eduarda Nogueira</h2>
              <p className="text-[10px] text-gold font-bold tracking-[0.3em] mt-2 uppercase">Legal Intelligence</p>
            </div>
            <nav className="flex-1 p-6 space-y-3 overflow-y-auto">
              <button onClick={() => { voltarHome(); setMenuMobileAberto(false); }} className={`w-full flex items-center gap-4 px-4 py-4 rounded-lg transition-all font-medium ${tela === 'home' ? 'bg-gold/10 text-gold border-l-4 border-gold shadow-sm' : 'text-secondary hover:bg-gray-50 hover:text-primary'}`}>
                <Home size={20} /><span>Início</span>
              </button>
              <button onClick={() => { setTela('configuracoes'); setMenuMobileAberto(false); }} className={`w-full flex items-center gap-4 px-4 py-4 rounded-lg transition-all font-medium ${tela === 'configuracoes' ? 'bg-gold/10 text-gold border-l-4 border-gold shadow-sm' : 'text-secondary hover:bg-gray-50 hover:text-primary'}`}>
                <Settings size={20} /><span>Escritório</span>
              </button>
              <button onClick={() => { setTela('historico'); setMenuMobileAberto(false); }} className={`w-full flex items-center gap-4 px-4 py-4 rounded-lg transition-all font-medium ${tela === 'historico' ? 'bg-gold/10 text-gold border-l-4 border-gold shadow-sm' : 'text-secondary hover:bg-gray-50 hover:text-primary'}`}>
                <FileText size={20} /><span>Histórico</span>
              </button>
            <button onClick={() => { setTela('analisador'); setMenuMobileAberto(false); }} className={`w-full flex items-center gap-4 px-4 py-4 rounded-lg transition-all font-medium ${tela === 'analisador' ? 'bg-gold/10 text-gold border-l-4 border-gold shadow-sm' : 'text-secondary hover:bg-gray-50 hover:text-primary'}`}>
                <Brain size={20} /><span>Analisador IA</span>
              </button>
            </nav>
          </div>
        </>
      )}

      {/* CONTEÚDO PRINCIPAL */}
      <div className="flex-1 overflow-y-auto bg-main relative z-0 w-full">
        
        {/* MODO FOCO (EDITOR FINAL) */}
        {modoFoco && (
          <div className="modo-foco fixed inset-0 z-50 overflow-y-auto bg-[#EFEBE9] text-black">
            <div className="max-w-6xl mx-auto py-6 px-4 md:py-16 md:px-8">
              <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4">
                <button onClick={() => setModoFoco(false)} className="flex gap-2 text-secondary hover:text-primary transition-colors"><ArrowLeft /> Voltar ao Painel</button>
                <div className="flex gap-2 w-full md:w-auto">
                    <button onClick={() => setModalJurisprudencia(true)} className="flex-1 md:flex-none justify-center px-6 py-3 bg-white border border-gold text-gold rounded-lg flex items-center gap-2 hover:bg-gold hover:text-white transition-all shadow-sm font-bold"><BookOpen size={18}/> Jurisprudência IA</button>
                </div>
              </div>
              
              <div className="flex justify-center">
                {/* PAPEL RESPONSIVO: w-full no mobile, w-[21cm] no desktop */}
                <div className="bg-white w-full md:w-[21cm] min-h-[60vh] md:min-h-[29.7cm] p-6 md:p-[3cm_2cm_2cm_3cm] shadow-2xl relative flex flex-col doc-container border-t-4 border-gold">
                  
                  {configCabecalho.logoBase64 && (
                    <div className="w-full flex justify-center mb-8">
                      <img src={configCabecalho.logoBase64} className="w-20 h-20 md:w-24 md:h-24 object-contain" alt="Logo Doc" />
                    </div>
                  )}

                  <div 
                    id="editor-documento" 
                    contentEditable={modoEdicao} 
                    suppressContentEditableWarning={true} 
                    onInput={(e) => setDocumentoGerado(e.currentTarget.innerHTML)} 
                    className="flex-1 whitespace-pre-wrap focus:outline-none outline-none" 
                    dangerouslySetInnerHTML={{ __html: documentoGerado }} 
                  />

                  <div className="mt-12 pt-6 border-t border-gray-200 text-center text-xs text-gray-500 uppercase font-sans">
                    <p className="font-bold text-gold mb-1">{configCabecalho.nome}</p>
                    <p>{configCabecalho.endereco} • {configCabecalho.cidade}/{configCabecalho.estado} • {configCabecalho.telefone}</p>
                    <p>{configCabecalho.email}</p>
                  </div>
                </div>
              </div>
              
              {/* Botões flutuantes ajustados para mobile */}
              <div className="mt-8 flex flex-col md:flex-row gap-3 justify-end sticky bottom-4 z-50 px-2 md:px-0">
                <button onClick={() => setModoEdicao(!modoEdicao)} className="px-8 py-4 bg-white text-primary border border-light rounded-lg shadow-lg hover:border-gold transition-all font-bold flex items-center justify-center gap-3">{modoEdicao ? <><Save size={20} className="text-gold"/> Salvar Edição</> : <><Edit3 size={20} className="text-gold"/> Editar Texto</>}</button>
                <button onClick={handleDownload} className="px-8 py-4 bg-gradient-gold text-white rounded-lg font-bold shadow-lg hover:shadow-xl transition-all flex items-center justify-center gap-3"><Download size={20}/> Baixar DOCX</button>
              </div>
            </div>
          </div>
        )}

        {/* DASHBOARD HOME */}
        {tela === 'home' && !modoFoco && (
          <div className="max-w-7xl mx-auto p-6 md:p-16">
            <div className="text-center mb-10 md:mb-20">
                <h1 className="text-3xl md:text-5xl font-serif font-bold mb-4 text-primary">Bem-vindo(a), <span className="text-gold italic">a maior Tecnologia Jurídica</span></h1>
                <p className="text-secondary text-base md:text-lg max-w-2xl mx-auto">Selecione a área de atuação para iniciar a elaboração inteligente de seus documentos jurídicos.</p>
            </div>
            {/* Grid responsivo: 1 col mobile, 2 tablet, 3 desktop */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
              {Object.entries(PECAS_JURIDICAS).map(([key, area]) => {
                const Icon = iconMap[area.icon] || FileText;
                return (
                  <button key={key} onClick={() => handleAreaClick(key)} className="card-premium p-6 md:p-10 rounded-xl group text-left relative overflow-hidden">
                    <div className="absolute top-0 right-0 p-4 opacity-5 text-gold group-hover:opacity-10 transition-opacity"><Icon size={80} className="md:w-[100px] md:h-[100px]"/></div>
                    <div className="w-14 h-14 md:w-16 md:h-16 rounded-2xl bg-gold/10 flex items-center justify-center text-gold mb-6 shadow-sm group-hover:scale-110 transition-transform">
                      <Icon size={28} className="md:w-8 md:h-8" />
                    </div>
                    <h3 className="text-xl md:text-2xl font-serif font-bold mb-2 text-primary group-hover:text-gold transition-colors">{area.nome}</h3>
                    <p className="text-secondary text-sm mb-6">Acesse os modelos e fluxos de trabalho para a área {area.nome.toLowerCase()}.</p>
                    <div className="flex items-center text-gold text-sm font-bold uppercase tracking-wider">
                      Início Rápido <ArrowLeft size={16} className="rotate-180 ml-2 group-hover:translate-x-2 transition-transform"/>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* TELA DE CONFIGURAÇÕES */}
        {tela === 'configuracoes' && !modoFoco && (
          <div className="max-w-4xl mx-auto p-6 md:p-16">
            <button onClick={voltarHome} className="flex items-center gap-3 text-secondary hover:text-primary mb-10 transition-colors"><ArrowLeft size={16} /> Voltar</button>
            <h1 className="text-3xl md:text-4xl font-serif font-bold mb-4 text-primary">Identidade do Escritório</h1>
            
            <div className="card-premium p-6 md:p-10 rounded-xl space-y-8">
              <div className="flex flex-col md:flex-row items-center md:items-start gap-10 pb-10 border-b border-light">
                  <div className="border-2 border-dashed border-light rounded-xl p-8 text-center hover:border-gold transition-all bg-main w-full md:w-1/3 flex flex-col items-center justify-center relative group cursor-pointer">
                    <input type="file" accept="image/*" onChange={handleLogoUpload} className="hidden" id="logo-upload" />
                    {configCabecalho.logoBase64 ? (
                      <div className="relative">
                        <img src={configCabecalho.logoBase64} className="w-32 h-32 mx-auto object-contain mb-4" alt="Logo" />
                        <label htmlFor="logo-upload" className="absolute inset-0 bg-black/50 flex items-center justify-center text-white opacity-0 group-hover:opacity-100 transition-opacity rounded-lg cursor-pointer font-bold"><Edit3 className="mr-2"/>Alterar</label>
                      </div>
                    ) : (
                      <label htmlFor="logo-upload" className="cursor-pointer flex flex-col items-center">
                        <div className="w-16 h-16 bg-gold/10 rounded-full flex items-center justify-center text-gold mb-4"><ImageIcon size={32} /></div>
                        <p className="text-primary font-bold">Upload da Logo</p>
                        <p className="text-secondary text-xs mt-2">PNG, JPG (Max. 2MB)</p>
                      </label>
                    )}
                  </div>
                  <div className="flex-1 space-y-6 w-full">
                     <FormField campo="nome" config={{label: "Nome do Escritório / Advogado(a)", tipo: "text"}} value={configCabecalho.nome} onChange={(c, v) => setConfigCabecalho({...configCabecalho, nome: v})} />
                     <FormField campo="oab" config={{label: "Registro OAB", tipo: "text"}} value={configCabecalho.oab} onChange={(c, v) => setConfigCabecalho({...configCabecalho, oab: v})} />
                  </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="md:col-span-2"><FormField campo="endereco" config={{label: "Endereço Completo", tipo: "text"}} value={configCabecalho.endereco} onChange={(c, v) => setConfigCabecalho({...configCabecalho, endereco: v})} /></div>
                <FormField campo="cidade" config={{label: "Cidade", tipo: "text"}} value={configCabecalho.cidade} onChange={(c, v) => setConfigCabecalho({...configCabecalho, cidade: v})} />
                <div className="grid grid-cols-3 gap-4">
                    <div className="col-span-1"><FormField campo="estado" config={{label: "UF", tipo: "text"}} value={configCabecalho.estado} onChange={(c, v) => setConfigCabecalho({...configCabecalho, estado: v.toUpperCase()})} /></div>
                    <div className="col-span-2"><FormField campo="cep" config={{label: "CEP", tipo: "text"}} value={configCabecalho.cep} onChange={(c, v) => setConfigCabecalho({...configCabecalho, cep: v})} /></div>
                </div>
                <FormField campo="telefone" config={{label: "Telefone / WhatsApp", tipo: "text"}} value={configCabecalho.telefone} onChange={(c, v) => setConfigCabecalho({...configCabecalho, telefone: v})} />
                <FormField campo="email" config={{label: "E-mail Profissional", tipo: "email"}} value={configCabecalho.email} onChange={(c, v) => setConfigCabecalho({...configCabecalho, email: v})} />
              </div>
              <button onClick={salvarConfiguracoesEscritorio} className="w-full bg-gradient-gold py-5 rounded-lg font-bold text-sm uppercase tracking-[0.2em] hover:shadow-lg transition-all">Salvar Alterações</button>
            </div>
          </div>
        )}

        {/* TELA DE HISTÓRICO */}
        {tela === 'historico' && !modoFoco && (
          <div className="max-w-6xl mx-auto p-6 md:p-16">
            <button onClick={voltarHome} className="flex items-center gap-3 text-secondary hover:text-primary mb-10 transition-colors"><ArrowLeft size={16} /> Voltar</button>
            <h1 className="text-3xl md:text-4xl font-serif font-bold mb-12 text-primary">Documentos Recentes</h1>
            
            {historico.length === 0 ? (
                <div className="text-center text-secondary py-20 border-2 border-dashed border-light rounded-xl bg-main">
                    <FileText size={64} className="mx-auto mb-6 text-gold/50" />
                    <p className="text-xl font-serif mb-2">Nenhum documento encontrado</p>
                    <p>Seus documentos gerados aparecerão aqui.</p>
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
                    {historico.map((doc) => (
                        <div key={doc.id} className="card-premium p-6 rounded-xl flex flex-col justify-between h-56 relative group">
                            <div className="absolute top-4 right-4 opacity-100 md:opacity-0 md:group-hover:opacity-100 transition-opacity">
                                <button onClick={() => handleExcluirHistorico(doc.id)} className="p-2 text-red-400 hover:text-red-600 hover:bg-red-50 rounded-full transition-colors"><Trash2 size={18}/></button>
                            </div>
                            <div>
                                <div className="flex items-center gap-3 mb-4">
                                    <div className="p-3 bg-gold/10 rounded-lg text-gold">
                                        {doc.areaObj?.icon && React.createElement(iconMap[doc.areaObj.icon] || FileText, { size: 20 })}
                                    </div>
                                    <div>
                                         <p className="text-xs text-secondary font-mono uppercase tracking-wider">{doc.data}</p>
                                         <p className="text-xs font-bold text-gold mt-1">{doc.area}</p>
                                    </div>
                                </div>
                                <h3 className="text-xl font-serif font-bold text-primary mb-2 truncate" title={doc.tipo}>{doc.tipo}</h3>
                                {doc.dados?.autor && <p className="text-sm text-secondary truncate">Cliente: {doc.dados.autor}</p>}
                            </div>
                            
                            <button onClick={() => handleAbrirHistorico(doc)} className="w-full py-3 mt-4 bg-main text-primary border border-light rounded-lg font-bold text-sm hover:bg-gold hover:text-white hover:border-gold transition-all uppercase tracking-wider flex items-center justify-center gap-2">
                                Abrir Documento <ArrowLeft size={14} className="rotate-180"/>
                            </button>
                        </div>
                    ))}
                </div>
            )}
          </div>
        )}
      {tela === 'analisador' && (
          <div className="w-full h-full flex flex-col">
              {/* Botão para voltar */}
              <div className="p-4 bg-white border-b">
                  <button onClick={() => setTela('home')} className="flex items-center gap-2 text-gray-600 hover:text-gold">
                      <ArrowLeft size={20}/> Voltar para o Escritório
                  </button>
              </div>
              
              {/* O IFRAME QUE CARREGA O DJANGO */}
              <iframe 
                src="https://tevox-analisador.onrender.com" 
                className="flex-1 w-full border-0" 
                title="Analisador IA"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                loading="lazy"
              ></iframe>
          </div>
      )}

        {/* NAVEGAÇÃO: SUBTIPOS, TELA ZERO E PEÇAS */}
        {(tela === 'subtipos_contratos' || tela === 'tela_zero' || tela === 'pecas' || tela === 'pecas_contratos') && (
           <div className="max-w-7xl mx-auto p-6 md:p-16">
             <button onClick={() => setTela(tela === 'pecas' ? 'tela_zero' : (tela === 'pecas_contratos' ? 'subtipos_contratos' : 'home'))} className="flex items-center gap-3 text-secondary hover:text-primary mb-10 transition-colors"><ArrowLeft size={16} /> Voltar</button>
             
             <div className="text-center mb-10 md:mb-16">
                <h1 className="text-3xl md:text-4xl font-serif font-bold mb-4 text-primary">
                    {tela === 'subtipos_contratos' ? "Qual tipo de contrato?" : (subtipoSelecionado ? subtipoSelecionado.nome : areaSelecionada.nome)}
                </h1>
             </div>

             {tela === 'subtipos_contratos' && (
                 <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
                   {Object.entries(areaSelecionada.subtipos).map(([key, subtipo]) => (
                     <button key={key} onClick={() => { setSubtipoSelecionado({ key, ...subtipo }); setTela('pecas_contratos'); }} className="card-premium p-8 rounded-xl text-center group">
                       <div className="w-16 h-16 mx-auto rounded-2xl bg-gold/10 flex items-center justify-center text-gold mb-6 shadow-sm group-hover:scale-110 transition-transform"><FileText size={32} /></div>
                       <h3 className="text-xl font-serif font-bold mb-2 text-primary group-hover:text-gold transition-colors">{subtipo.nome}</h3>
                       <p className="text-secondary text-sm">{subtipo.descricao}</p>
                     </button>
                   ))}
                 </div>
             )}

             {tela === 'tela_zero' && (
               <div className="card-premium p-6 md:p-12 rounded-xl max-w-3xl mx-auto">
                 <h2 className="text-xl md:text-2xl font-serif font-bold mb-8 text-center text-primary">Este é um processo novo ou já existente?</h2>
                 <div className="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 mb-10">
                   <button onClick={() => { setProcessoExiste(true); }} className={`p-6 md:p-10 rounded-xl border-2 transition-all flex flex-col items-center gap-4 group ${processoExiste === true ? 'border-gold bg-gold/5 shadow-md' : 'border-light bg-main hover:border-gold/50'}`}>
                     <CheckCircle size={48} className={processoExiste === true ? 'text-gold' : 'text-secondary group-hover:text-gold'} />
                     <span className={`font-bold text-lg md:text-xl ${processoExiste === true ? 'text-primary' : 'text-secondary group-hover:text-primary'}`}>Já Existe (Tenho o Número)</span>
                   </button>
                   <button onClick={() => { setProcessoExiste(false); setNumeroProcesso(''); }} className={`p-6 md:p-10 rounded-xl border-2 transition-all flex flex-col items-center gap-4 group ${processoExiste === false ? 'border-gold bg-gold/5 shadow-md' : 'border-light bg-main hover:border-gold/50'}`}>
                     <Plus size={48} className={processoExiste === false ? 'text-gold' : 'text-secondary group-hover:text-gold'} />
                     <span className={`font-bold text-lg md:text-xl ${processoExiste === false ? 'text-primary' : 'text-secondary group-hover:text-primary'}`}>É Novo (Vou Iniciar)</span>
                   </button>
                 </div>
                 
                 {processoExiste === true && (
                    <div className="mb-8">
                        <FormField campo="numero_processo_tela_zero" config={{label: "Informe o Número do Processo (CNJ)", tipo: "text", placeholder: "0000000-00.0000.0.00.0000"}} value={numeroProcesso} onChange={(c, v) => setNumeroProcesso(v)} />
                    </div>
                 )}

                 <button onClick={handleConfirmarTelaZero} className="w-full bg-gradient-gold py-5 rounded-lg font-bold text-sm uppercase tracking-[0.2em] hover:shadow-lg transition-all">Continuar para Modelos</button>
               </div>
             )}
             
             {(tela === 'pecas' || tela === 'pecas_contratos') && (
               <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                 {(subtipoSelecionado ? subtipoSelecionado.pecas : pecasFiltradas).map(p => (
                   <button key={p.id} onClick={() => handlePecaClick(p)} className="card-premium p-6 md:p-8 rounded-xl text-left group hover:bg-gold/5 transition-all relative overflow-hidden">
                     <div className={`absolute top-4 right-4 text-[10px] md:text-xs font-bold px-3 py-1 rounded-full ${p.uploadObrigatorio ? 'bg-blue-50 text-blue-600' : 'bg-green-50 text-green-600'}`}>
                        {p.uploadObrigatorio ? 'REQUER ANÁLISE' : 'CRIAÇÃO RÁPIDA'}
                     </div>
                     <div className="w-12 h-12 rounded-lg bg-gold/10 flex items-center justify-center text-gold mb-6 group-hover:scale-110 transition-transform">
                        {React.createElement(iconMap[areaSelecionada.icon] || FileText, { size: 24 })}
                     </div>
                     <h3 className="text-lg md:text-xl font-serif font-bold text-primary group-hover:text-gold transition-colors mb-2">{p.nome}</h3>
                     <p className="text-xs md:text-sm text-secondary">{p.camada} • {p.modelo}</p>
                   </button>
                 ))}
               </div>
             )}
           </div>
        )}

        {/* FORMULÁRIO */}
        {tela === 'formulario' && pecaSelecionada && (
          <div className="max-w-5xl mx-auto p-6 md:p-16">
            <button onClick={() => setTela(subtipoSelecionado ? 'pecas_contratos' : 'pecas')} className="flex items-center gap-3 text-secondary hover:text-primary mb-10 transition-colors"><ArrowLeft size={16} /> Voltar para Modelos</button>
            
            {/* STEPPER RESPONSIVO */}
            <Stepper steps={STEPS_POR_MODELO[pecaSelecionada.modelo] || []} currentStep={currentStep} onStepClick={(idx) => idx < currentStep && setCurrentStep(idx)} />
            
            <div className="card-premium p-6 md:p-12 rounded-xl">
               <div className="mb-8 md:mb-10 pb-6 border-b border-light">
                   <h2 className="text-2xl md:text-3xl font-serif font-bold text-primary mb-2 flex items-center gap-3">
                       {(STEPS_POR_MODELO[pecaSelecionada.modelo] || [])[currentStep]?.icon && React.createElement((STEPS_POR_MODELO[pecaSelecionada.modelo] || [])[currentStep].icon, { size: 32, className: 'text-gold' })}
                       {(STEPS_POR_MODELO[pecaSelecionada.modelo] || [])[currentStep]?.titulo}
                   </h2>
                   <p className="text-secondary text-base md:text-lg">{(STEPS_POR_MODELO[pecaSelecionada.modelo] || [])[currentStep]?.descricao}</p>
               </div>

              {(STEPS_POR_MODELO[pecaSelecionada.modelo] || [])[currentStep]?.acao === 'analisar_upload' ? (
                <div className="border-3 border-dashed border-light p-8 md:p-16 text-center rounded-xl hover:border-gold hover:bg-gold/5 transition-all group cursor-pointer bg-main">
                  <input type="file" id="upload" className="hidden" onChange={handleFileUpload} accept=".pdf,.docx,.doc,.txt" />
                  <label htmlFor="upload" className="cursor-pointer flex flex-col items-center">
                    <div className="w-16 h-16 md:w-20 md:h-20 bg-white rounded-full flex items-center justify-center text-gold shadow-md mb-6 group-hover:scale-110 transition-transform">
                        {loading ? <Loader className="animate-spin" size={40} /> : <Upload size={40}/>}
                    </div>
                    <h3 className="text-xl md:text-2xl font-bold text-primary mb-2 group-hover:text-gold transition-colors">Upload da {pecaSelecionada.arquivoNecessario}</h3>
                    <p className="text-secondary mb-6 max-w-md mx-auto text-sm md:text-base">Arraste seu arquivo aqui ou clique para selecionar. Nossa IA analisará o conteúdo automaticamente.</p>
                    <span className="px-6 py-3 bg-white border border-light rounded-full text-sm font-bold text-gold shadow-sm group-hover:shadow-md transition-all">Formatos: PDF, DOCX, TXT</span>
                  </label>
                </div>
              ) : (
                <div className="space-y-8">
                    {(STEPS_POR_MODELO[pecaSelecionada.modelo] || [])[currentStep]?.campos.map(campo => (
                    <div key={campo} className="relative">
                        <FormField 
                          campo={campo} 
                          config={CAMPOS_CONFIG[campo]} 
                          value={formData[campo]} 
                          onChange={handleInputChange} 
                          erro={errosValidacao[campo]} 
                          onMagic={handleMagicClick}   
                          loading={loading}            
                      />
                    </div>
                    ))}
                </div>
              )}

              <div className="flex flex-col md:flex-row justify-between mt-12 pt-8 border-t border-light gap-4 md:gap-0">
                <button onClick={() => setCurrentStep(c => Math.max(0, c - 1))} disabled={currentStep === 0} className="w-full md:w-auto px-8 py-4 text-secondary font-bold hover:text-primary hover:bg-main rounded-lg transition-all disabled:opacity-50 text-center">Voltar Etapa</button>
                {currentStep === (STEPS_POR_MODELO[pecaSelecionada.modelo] || []).length - 1 ? (
                  <button onClick={handleGenerar} disabled={loading} className="w-full md:w-auto px-10 py-4 bg-gradient-gold text-white font-bold rounded-lg shadow-lg hover:shadow-xl transition-all flex items-center justify-center gap-3 text-lg tracking-wider">
                     {loading ? <Loader className="animate-spin" size={24}/> : <FileText size={24}/>} GERAR DOCUMENTO FINAL
                  </button>
                ) : (
                  <button onClick={handleProximaEtapa} className="w-full md:w-auto px-10 py-4 bg-primary text-slate-600 font-bold rounded-lg shadow-md hover:bg-primary/90 transition-all flex items-center justify-center gap-3">
                  Próxima Etapa <ArrowLeft size={18} className="rotate-180"/>
                </button>
                )}
              </div>
            </div>
          </div>
        )}

        {/* MODAL JURISPRUDÊNCIA */}
        {modalJurisprudencia && (
          <div className="fixed inset-0 bg-primary/50 backdrop-blur-sm flex items-center justify-center z-[70] p-4 md:p-8">
            <div className="card-premium rounded-xl w-full max-w-5xl h-[90vh] md:h-[85vh] flex flex-col overflow-hidden shadow-2xl">
              <div className="p-6 md:p-8 border-b border-light flex justify-between items-center bg-main">
                <div>
                    <h2 className="text-xl md:text-3xl font-serif font-bold text-primary mb-2 flex items-center gap-3"><BookOpen className="text-gold"/> Banco de Jurisprudência IA</h2>
                    <p className="text-secondary text-xs md:text-base">Pesquise em nossa base de dados inteligente para fortalecer seus argumentos.</p>
                </div>
                <button onClick={() => setModalJurisprudencia(false)} className="p-2 text-secondary hover:text-primary hover:bg-light rounded-full transition-colors"><XCircle size={28}/></button>
              </div>
              <div className="p-6 md:p-8 border-b border-light bg-white">
                <div className="flex flex-col md:flex-row gap-4">
                  <div className="flex-1 relative">
                      <Search size={20} className="absolute left-4 top-1/2 -translate-y-1/2 text-secondary"/>
                      <input className="input-premium pl-12 text-base md:text-lg" placeholder="Digite o tema (ex: dano moral atraso voo)..." value={buscaJurisprudencia} onChange={e => setBuscaJurisprudencia(e.target.value)} onKeyPress={e => e.key === 'Enter' && buscarJurisprudencia()} />
                  </div>
                  <button onClick={buscarJurisprudencia} disabled={loadingJurisprudencia} className="px-8 py-4 md:py-0 bg-gradient-gold text-white font-bold rounded-lg shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-3 disabled:opacity-70">
                      {loadingJurisprudencia ? <Loader className="animate-spin" size={20}/> : <Search size={20}/>} Pesquisar
                  </button>
                </div>
              </div>
              <div className="flex-1 overflow-y-auto p-6 md:p-8 bg-main">
                {jurisprudencias.length === 0 ? (
                    <div className="h-full flex flex-col items-center justify-center text-secondary opacity-60">
                        <BookOpen size={64} className="mb-4 text-gold"/>
                        <p className="text-xl font-serif">Nenhuma jurisprudência encontrada.</p>
                        <p>Tente buscar por outro termo ou área.</p>
                    </div>
                ) : (
                    <div className="space-y-6">
                        {jurisprudencias.map((jur, idx) => (
                        <div key={idx} className="card-premium p-6 rounded-xl hover:border-gold group transition-all bg-white">
                            <div className="flex flex-col md:flex-row justify-between items-start mb-4 pb-4 border-b border-light gap-4">
                                <div>
                                    <span className="inline-block px-3 py-1 bg-gold/10 text-gold text-xs font-bold rounded-full mb-2">{jur.tribunal}</span>
                                    <h3 className="font-bold text-primary text-lg">{jur.numero}</h3>
                                    <p className="text-sm text-secondary">Relator(a): {jur.relator} • Julgado em: {jur.data}</p>
                                </div>
                                <div className="flex gap-2 self-end md:self-auto">
                                    <button onClick={() => salvarFavorito(jur)} className="p-2 text-yellow-400 hover:text-yellow-500 transition-colors"><Star size={20}/></button>
                                    <button onClick={() => inserirJurisprudencia(jur)} className="px-6 py-3 bg-primary text-white text-sm font-bold rounded-lg hover:bg-gold transition-all shadow-sm flex items-center gap-2">
                                        <Plus size={16}/> Inserir no Documento
                                    </button>
                                </div>
                            </div>
                            <div className="bg-main p-5 rounded-lg border border-light leading-relaxed text-justify text-primary font-serif relative pl-10">
                                <span className="absolute left-4 top-4 text-4xl text-gold/30 font-serif">“</span>
                                {jur.ementa}
                            </div>
                        </div>
                        ))}
                    </div>
                )}
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;