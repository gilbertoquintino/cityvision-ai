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
├── README.md                  # Este arquivo com a visão geral do projeto
├── docs/                      # Documentação detalhada do projeto
│   ├── projeto-geral.md       # Escopo, problemas e objetivos gerais
│   ├── arquitetura.md         # Integração AutoGen, LM Studio e LLMs
│   ├── fluxo-agentes.md       # Dinâmica de conversa e turnos dos agentes
│   └── apresentacoes/         # Materiais de apresentação e pitches
├── agents/                    # Definição e diretrizes dos agentes de IA
│   ├── [nome-do-agente]/
│   │   ├── system-message.md  # Instrução de sistema (System Prompt)
│   │   ├── personality.md     # Tom, linguagem e vieses técnicos
│   │   └── prompts.md         # Registro de prompts de teste e finais
├── prompts/                   # Repositório de briefings e testes de execução
│   ├── briefing-inicial.md    # Briefing de entrada do cliente
│   ├── testes.md              # Roteiros de testes com prompts
│   └── prompts-finais.md      # Prompts finais consolidados
├── evidencias/                # Registros visuais e textuais do funcionamento
│   ├── configuracao-modelos/  # Prints e configs do LM Studio
│   ├── testes/                # Resultados de testes parciais
│   ├── execucoes/             # Logs brutos de debates
│   └── resultados/            # Relatórios finais gerados
├── models/                    # Estudo e avaliação dos modelos de LLM
│   ├── modelos-testados.md    # Tabela comparativa de modelos testados
│   └── benchmark.md           # Critérios de avaliação
├── src/                       # Código-fonte Python do sistema
│   ├── main.py                # Entrada principal do sistema
│   ├── agents.py              # Declaração dos agentes AutoGen
│   ├── config.py              # Variáveis de ambiente e portas do LM Studio
│   └── utils.py               # Funções de suporte e exportação
├── logs/                      # Pasta para arquivos de log gerados em tempo de execução
└── referencias/               # Material teórico de apoio e pesquisa
    ├── artigos/
    ├── links/
    └── materiais-aula/
```

## 🚀 Como o Projeto Será Evoluído
1. **Fase 1: Concepção e Setup**: Definição da estrutura de pastas, personas de agentes e instalação do ambiente (Concluído).
2. **Fase 2: Engenharia de Prompts**: Refinamento de prompts e system messages individuais.
3. **Fase 3: Integração Local**: Conexão do AutoGen com o LM Studio local e validação de comunicação.
4. **Fase 4: Simulações**: Execução de debates com o briefing inicial e refinamento de parâmetros de temperatura/contexto.
5. **Fase 5: Consolidação**: Ajuste do agente Apresentador para entregar relatórios formatados em Markdown.
6. **Fase 6: Avaliação de Modelos**: Execução de benchmarks para determinar o melhor modelo local custo-benefício.

## 👥 Integrantes da Equipe
- **Membro 1**: Gilberto Quintino de Santana Filho/ GitHub: gilbertoquintino
- **Membro 2**: Thayana Anália dos Santos/ GitHub: thayanalira
