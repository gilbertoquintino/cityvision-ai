# Documento de Reflexões e Autoavaliação do Projeto

> [!NOTE]
> **Sobre este documento**: Este arquivo contém as respostas reflexivas sobre o comportamento do sistema multiagente durante a simulação de planejamento urbano do **CityVision AI**. O preenchimento final das respostas deve ser feito pelo aluno com base na execução real no LM Studio.

---

## 1. Quais foram os principais conflitos observados entre os agentes?

*Preencha aqui os conflitos gerados entre os especialistas. Por exemplo:*
- **Economista vs. Ambientalista / Urbanista**: Divergências em relação ao custo de implantação de parques lineares urbanos, fachadas ativas ecológicas e fontes de energias renováveis frente ao orçamento restrito de R$ 15 milhões.
- **Especialista em Mobilidade vs. Sociólogo / Urbanista**: Propostas de redução de vias de carros ou pedagiamento urbano que podem isolar a comunidade local ou impactar negativamente a acessibilidade de moradores de baixa renda.
- **Engenheiro de Infraestrutura vs. Ambientalista**: Dilema técnico sobre a complexidade de implantação de smart grids subterrâneos e pavimentação sustentável versus o impacto ecológico imediato.

*(Espaço reservado para relato da execução real)*
> 

---

## 2. Quais são os riscos inerentes à atuação de cada agente?

Mapeamento de riscos e vieses observados na atuação autônoma de cada papel no sistema:

| Agente Especialista | Risco de Atuação (Viés Técnico) | Impacto no Projeto Final |
| :--- | :--- | :--- |
| **Orquestrador** | Pressa para fechar acordos e convergir rápido, silenciando discussões profundas. | Soluções genéricas e debate pouco aprofundado se o limite de turnos for curto. |
| **Urbanista** | Foco excessivo na estética arquitetônica conceitual ("cidade perfeita"). | Propostas financeiramente inviáveis ou de difícil execução no mundo real. |
| **Engenheiro de Infraestrutura** | Ceticismo quanto a inovações ecológicas ousadas ou novas tecnologias construtivas. | Projeto excessivamente tradicional, perdendo oportunidades inovadoras. |
| **Especialista em Mobilidade** | Defesa intransigente do banimento de carros sem faseamento de transição gradual. | Insatisfação popular e estrangulamento comercial da área se feito repentinamente. |
| **Ambientalista** | Rigidez radical quanto ao impacto ecológico, rejeitando qualquer concessão de infraestrutura. | Travamento ou paralisação das negociações com o Economista e Engenheiro. |
| **Sociólogo Urbano** | Oposição a todo investimento imobiliário privado por medo de gentrificação imediata. | Inviabilização financeira da revitalização, dependente apenas de verba pública escassa. |
| **Economista Urbano** | Priorização do retorno financeiro (ROI) de curto prazo ou parcerias privadas predatórias. | Risco de gentrificação forçada e perda do caráter público e comunitário da área. |
| **Apresentador de Projeto** | Simplificação excessiva de detalhes técnicos complexos em prol de uma narrativa bonita. | Falta de robustez técnica nos relatórios apresentados a investidores reais. |

---

## 3. Como a orquestração lidou com impasses técnicos?

*Descreva como o agente **Orquestrador** atuou para resolver os pontos críticos durante o debate. Considere:*
- A formulação de perguntas provocativas para forçar compromissos ("trade-offs") inteligentes.
- A condução do debate em direção a um equilíbrio comum (ex: propor que o Economista e a Ambientalista concordem em um modelo híbrido de PPP com incentivo fiscal ecológico).
- A chamada do Apresentador de Projeto para consolidar apenas o que era consenso técnico entre as partes.

*(Espaço reservado para relato da execução real)*
> 

---

## 4. Que melhorias poderiam ser aplicadas no fluxo do sistema?

*Sugestões de otimização da arquitetura multiagente para versões futuras do projeto:*
- **Critérios de Votação**: Implementar uma função de votação numérica onde os agentes classificam a viabilidade de cada proposta antes de gerar o relatório final.
- **Validação de Restrições por Código**: Integrar ferramentas de cálculo (Python execution) para que o Engenheiro e o Economista validem as estimativas de custos matematicamente durante o debate.
- **Agente de Feedback do Cidadão**: Incluir um nono agente que represente ativamente a associação de moradores local ("Voz da Comunidade"), reagindo em tempo real às propostas dos especialistas.
- **Controle de Temperatura Dinâmica**: Reduzir a temperatura do modelo à medida que o debate se aproxima do fim para forçar respostas mais objetivas e focadas na conclusão da proposta.

---

### Evidências da Simulação
Guarde nesta seção os caminhos ou links para as imagens salvas na pasta `evidencias/` mostrando:
1. O LM Studio configurado com a API ligada.
2. O terminal executando o debate no AutoGen.
