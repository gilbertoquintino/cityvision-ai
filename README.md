# CityVision AI 🏙️🌿

> **Sistema multiagente de planejamento urbano sustentável utilizando Agentic AI com AutoGen e LM Studio.**

---

## 🎯 Objetivo
O **CityVision AI** é uma consultoria inteligente de planejamento urbano sustentável que utiliza sistemas multiagentes para elaborar, de forma autônoma e colaborativa, planos de revitalização para áreas degradadas de cidades. O sistema visa equilibrar as dimensões ecológica, social, financeira e de infraestrutura, garantindo soluções viáveis e integradas.

## 📌 Contexto
O planejamento de cidades modernas exige a consideração de múltiplos fatores interdependentes. Abordagens tradicionais costumam falhar ao isolar áreas técnicas. O CityVision AI propõe uma abordagem de **Agentic AI** onde múltiplos agentes com personalidades e especialidades distintas debatem entre si para propor uma solução urbana coesa com base em briefings de linguagem natural.

## 🛠️ Tecnologias Utilizadas
- **Autogen (Microsoft)**: Framework para orquestração de conversas multiagente e fluxos de trabalho cooperativos.
- **LM Studio**: Hospedagem local de Modelos de Linguagem de Grande Porte (LLMs) para privacidade, custo zero de tokens e testes controlados.
- **Python 3.10+**: Linguagem base para execução do sistema.
- **Modelos LLM**: Modelos locais integrados via API compatível com OpenAI fornecida pelo LM Studio.
   - **Modelo Adotado**: **Qwen2.5-7B-Instruct-GGUF** (especificamente o quantizado `Q4_K_M` de 4.68 GB), selecionado pelo excelente equilíbrio entre capacidade de raciocínio, aderência à persona e consumo de memória extremamente eficiente.
   - **Histórico de Testes**: A equipe testou inicialmente o **GPT-OSS 20B** como referência, contudo, seu alto consumo de recursos computacionais (>16GB VRAM) inviabilizou a execução estável em hardware intermediário de desenvolvimento pessoal.

## 👥 Estrutura de Agentes
O ecossistema é formado por 8 agentes obrigatórios:

1. **Orquestrador (Orchestrator)**: Responsável por coordenar o fluxo de debate, encaminhar perguntas e garantir que todos os especialistas colaborem antes da consolidação.
2. **Urbanista (Urbanist)**: Focado em zoneamento, uso do solo, estética urbana e aproveitamento de espaços públicos.
3. **Engenheiro de Infraestrutura (Infrastructure)**: Avalia a viabilidade física, saneamento, energia, conectividade e sustentabilidade física das estruturas.
4. **Especialista em Mobilidade (Mobility)**: Dedica-se ao transporte público, ciclovias, acessibilidade, trânsito ativo e redução de emissões no tráfego.
5. **Ambientalista (Environmentalist)**: Protege a biodiversidade, propõe áreas verdes, analisa impacto climático, drenagem urbana sustentável (microdrenagem) e pegada de carbono.
6. **Sociólogo Urbano (Sociologist)**: Defende a inclusão social, habitação popular, acessibilidade cultural, gentrificação mitigada e apropriação comunitária do espaço.
7. **Economista Urbano (Economist)**: Garante a viabilidade orçamentária, analisa retorno sobre investimento (ROI), custos de manutenção e fomento econômico local.
8. **Apresentador de Projeto (Presenter)**: Consolida as contribuições técnicas de todos os agentes em uma narrativa coerente, gerando a proposta executiva final para o cliente.

## 📂 Organização de Pastas
```text
cityvision-ai/
├── README.md                  # Visão geral do projeto e guia de leitura
├── .gitignore                 # Arquivo de exclusões para Git (ignora caches e pycaches)
├── docs/                      # Documentação detalhada do projeto
│   ├── projeto-geral.md       # Escopo, problemas e objetivos gerais
│   ├── arquitetura.md         # Integração AutoGen, LM Studio e LLMs
│   ├── fluxo-agentes.md       # Dinâmica de conversa e turnos dos agentes
│   ├── reflexoes.md           # Relatório acadêmico de reflexões e autoavaliação
│   └── apresentacoes/         # Vídeo pitch de demonstração e PDF da apresentação
├── agents/                    # Definição e diretrizes dos agentes de IA (Prompts)
│   ├── [nome-do-agente]/      # Pastas para os 8 agentes especialistas
│   │   ├── system-message.md  # Instrução de sistema principal (System Prompt em Inglês)
│   │   ├── personality.md     # Guia de tom, linguagem, restrições e vieses (Inglês)
│   │   └── prompts.md         # Registro histórico de testes de engenharia de prompts
├── prompts/                   # Repositório de briefings e roteiros de teste
│   ├── briefing-inicial.md    # Briefing original do cliente em linguagem natural
│   ├── testes.md              # Roteiros e variações de testes com prompts
│   └── prompts-finais.md      # Registro consolidado dos prompts reais executados
├── evidencias/                # Comprovações físicas e visuais da execução
│   ├── simulacao-local/       # Capturas de tela (LM Studio, Hardware e AutoGen Studio)
│   ├── execucoes/             # Transcrições completas em markdown dos debates reais
│   └── resultados/            # Relatórios executivos finais gerados pelos agentes
├── models/                    # Estudo e avaliação dos modelos de LLM
│   ├── modelos-testados.md    # Tabela comparativa e especificações físicas de hardware
│   └── benchmark.md           # Critérios de pontuação e peso dos testes
├── src/                       # Código-fonte Python para execução autônoma (CLI)
│   ├── main.py                # Arquivo principal (GroupChat e orquestração customizada)
│   ├── agents.py              # Instanciação dos agentes via biblioteca pyautogen
│   ├── config.py              # Parâmetros de inferência e conexão do LM Studio
│   └── utils.py               # Rotinas auxiliares (leitura, escrita e logs)
├── logs/                      # Registro histórico das simulações locais executadas
└── referencias/               # Material teórico de apoio e pesquisa
    ├── artigos/
    ├── links/
    └── materiais-aula/
```

## 🚀 Fases de Desenvolvimento Concluídas
O projeto foi executado e validado em sua totalidade de acordo com o seguinte cronograma de engenharia:
1. **Fase 1: Concepção e Setup**: Criação da infraestrutura de diretórios, definição conceitual dos agentes especialistas e estruturação do Git.
2. **Fase 2: Engenharia de Prompts**: Elaboração e tradução para o inglês das system messages e guias de persona, garantindo melhor desempenho cognitivo com restrição de saída para português.
3. **Fase 3: Implementação de Código**: Desenvolvimento do script Python integrado ao framework `pyautogen`, incorporando uma rotina personalizada de seleção de oradores (Speaker Selection) para evitar desvios no debate.
4. **Fase 4: Integração Local e Simulação**: Configuração da inferência no LM Studio com o modelo local estável **Qwen2.5-7B-Instruct-GGUF** e execução do debate interativo na plataforma do AutoGen Studio.
5. **Fase 5: Extração e Consolidação de Resultados**: Gravação dos históricos de execução de debates reais nas pastas do projeto e extração do relatório final de revitalização portuária.
6. **Fase 6: Relatório Acadêmico**: Análise crítica de conflitos (custos vs. orçamento, restrições ambientais vs. sociais) e preenchimento das reflexões exigidas no roteiro avaliativo.

## 👥 Integrantes da Equipe
- **Membro 1**: Gilberto Quintino de Santana Filho / GitHub: gilbertoquintino
- **Membro 2**: Thayana Anália dos Santos / GitHub: thayanalira
