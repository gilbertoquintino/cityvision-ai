# Documento de Reflexões e Autoavaliação do Projeto - CityVision AI

> [!NOTE]
> **Sobre este documento**: Este arquivo contém as análises reflexivas sobre o comportamento do sistema multiagente durante a simulação de planejamento urbano do **CityVision AI**, executado com sucesso no AutoGen Studio utilizando o modelo local **Qwen2.5-7B-Instruct-GGUF** (quantização Q4_K_M) em um hardware intermediário (Samsung Book4 360, 16GB RAM, Intel Graphics).

---

## 1. Quais foram os principais conflitos observados entre os agentes?

Durante a execução da sessão `Equipe_CityVision_AI` no AutoGen Studio, o debate revelou divergências fundamentais de prioridades entre os especialistas:
* **Desenvolvimento Estrutural vs. Limitação Orçamentária**: O **Engenheiro de Infraestrutura** e o **Especialista em Mobilidade** propuseram grandes obras civis, como viadutos elevados, passagens subterrâneas, redes subterrâneas e frotas de ônibus elétricos. O **Economista Urbano** agiu como limitador técnico, alertando sobre a necessidade de avaliar criteriosamente a viabilidade financeira frente ao orçamento estrito de R$ 15 milhões, sugerindo que tais intervenções fossem escalonadas ou financiadas via Parcerias Público-Privadas (PPPs).
* **Intervenções Tecnológicas vs. Impacto Social**: O **Ambientalista** sugeriu a instalação de turbinas eólicas e painéis solares em espaços visíveis da comunidade. O **Sociólogo Urbano** aceitou a proposta, mas fez uma ressalva crítica de que estas instalações devem ser posicionadas com extrema cautela para minimizar os impactos sociais negativos no cotidiano dos moradores e evitar a descaracterização do espaço de convivência da comunidade.
* **Gentrificação vs. Moradia Adaptável**: Enquanto a necessidade de renovar a área portuária era defendida pelo **Urbanista**, o **Sociólogo** e o **Economista** debateram intensamente como oferecer habitações modulares que permitissem que as 350 famílias de baixa renda residissem e crescessem na área revitalizada, sem sofrerem um processo de expulsão (gentrificação) impulsionado por investimentos privados em PPPs.

---

## 2. Quais são os riscos inerentes à atuação de cada agente?

A análise do comportamento dos agentes revelou vieses técnicos e operacionais específicos:

| Agente Especialista | Risco de Atuação (Viés Técnico) | Impacto no Projeto Observado |
| :--- | :--- | :--- |
| **Orquestrador** | Tendência a repetir resumos estruturados e convergir rapidamente. | Em vez de aprofundar os pontos de atrito, o orquestrador consolidou consensos amplos de maneira linear. |
| **Urbanista** | Foco puramente estético e espacial. | Propôs corredores exclusivos e calçadas biofílicas sem mensurar custos ou impacto estrutural no subsolo portuário. |
| **Engenheiro de Infraestrutura** | Sobredimensionamento técnico de soluções tradicionais. | Propôs viadutos e passagens subterrâneas caras que consomem grande parte do orçamento disponível. |
| **Especialista em Mobilidade** | Viés de transporte ativo radical. | Propôs ciclovias elevadas com separação física sem considerar os impactos de custo ou a logística comercial portuária. |
| **Ambientalista** | Preservacionismo com foco em tecnologias caras. | Defendeu microgeração eólica e solar e jardins verticais em todos os edifícios, gerando alta complexidade de manutenção. |
| **Sociólogo Urbano** | Protecionismo comunitário e resistência a parcerias. | Focou na permanência das 350 famílias e capacitação comunitária, mas ofereceu poucos planos de viabilidade técnica. |
| **Economista Urbano** | Foco na eficiência e atração de capital (PPP). | Priorizou o controle de gastos e sugeriu parcerias privadas, o que abre espaço para especulação imobiliária se não houver regulação. |
| **Apresentador de Projeto** | Repetição e síntese redutiva. | Aglutinou os argumentos de forma organizada, mas simplificou os atritos técnicos reais que ocorreram durante as falas. |

---

## 3. Como a orquestração lidou com impasses técnicos?

A orquestração do debate ocorreu em um formato estruturado de rodadas (`RoundRobinGroupChat` configurado no AutoGen Studio):
1. **Introdução Estruturada**: O **Orquestrador** abriu a sessão carregando o briefing com sucesso e direcionou perguntas específicas para cada tema, servindo como guia temático do debate.
2. **Ciclo de Contribuição**: O fluxo sequencial garantiu que todos os 7 especialistas tivessem a oportunidade de falar uma vez, respondendo às provocações do orquestrador de forma disciplinada.
3. **Consolidação em Cascata**: Ao final do ciclo, o **Apresentador de Projeto** e o **Orquestrador** compilaram as contribuições de todas as áreas (Mobilidade, Infraestrutura, Meio Ambiente, Habitação, Inclusão e Orçamento) em um plano Markdown único.
4. **Resolução de Conflitos**: O Orquestrador acomodou os impasses técnicos adicionando cláusulas condicionais nas diretrizes. Por exemplo, a sugestão de ciclovias elevadas foi mantida, mas acompanhada do termo *"no entanto, devemos avaliar cuidadosamente os custos e benefícios"*, integrando o ponto de vista do Economista.

---

## 4. Que melhorias poderiam ser aplicadas no fluxo do sistema?

A análise prática da execução no AutoGen Studio sugere as seguintes otimizações:
* **Fuga da Repetição Excessiva**: Observou-se que o modelo `Qwen2.5` tendeu a repetir blocos inteiros de textos dos agentes anteriores na hora de consolidar a resposta (por exemplo, as conclusões e estruturas de tópicos do Apresentador e do Orquestrador ficaram bastante semelhantes). Isso pode ser mitigado reduzindo a temperatura do modelo para valores como `0.3` a `0.5`, ou ajustando o prompt de sistema do Apresentador para proibir cópias de trechos literais.
* **Transição de Estados Dinâmica (SelectorGroupChat)**: O uso de `RoundRobin` força uma ordem fixa e previsível. Substituir por um fluxo dinâmico ou por uma máquina de estados (onde o Orquestrador pode escolher diretamente quem responde a quem, por exemplo, fazendo o Economista responder logo após uma proposta de alto custo do Engenheiro) tornaria o debate mais realista e enérgico.
* **Mecanismo de Validação Financeira**: Integrar uma ferramenta de execução de código (Python Tool) para que o Economista pudesse calcular os custos estimados das propostas dos colegas de forma matemática e rejeitar propostas que estourassem a verba de R$ 15 milhões com base em dados reais.

---

### Evidências da Simulação Local
* Imagem de setup do Hardware e LM Studio: ![Hardware Specs](file:///C:/Users/gilbe/.gemini/antigravity/scratch/cityvision-ai/evidencias/configuracao-modelos/hardware_specs.png)
* Imagem do modelo carregado no LM Studio: ![Qwen2.5 Model Setup](file:///C:/Users/gilbe/.gemini/antigravity/scratch/cityvision-ai/evidencias/configuracao-modelos/qwen2.5_model_lmstudio.png)
* Imagem do AutoGen Studio em execução: ![AutoGen Studio Playground](file:///C:/Users/gilbe/.gemini/antigravity/scratch/cityvision-ai/evidencias/testes/autogenstudio_session1.png)
* Diagrama do Workflow da Equipe no AutoGen Studio: ![AutoGen Studio Workflow](file:///C:/Users/gilbe/.gemini/antigravity/scratch/cityvision-ai/evidencias/testes/autogenstudio_workflow.png)
