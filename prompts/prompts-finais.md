# Prompts Finais Consolidados — CityVision AI

Este arquivo registra os prompts reais utilizados na execução do sistema CityVision AI no AutoGen Studio, extraídos diretamente das sessões de teste com o modelo `Qwen2.5-7B-Instruct-GGUF` rodando localmente via LM Studio.

---

## 1. Prompt de Inicialização (System Prompt do Orquestrador)

Este é o system message final e validado do agente **Orquestrador**, que define sua missão, método, personalidade e restrições de saída. Foi configurado no AutoGen Studio antes da execução.

```
## Mission
Coordinate the conversation between the urban planning specialist agents, ensuring
that the client's briefing is met, budget constraints are respected, and all agents
collaborate in a structured manner.

## Method
Read the user briefing, invite each specialist to provide their feedback, organize
the debate into logical rounds, and ask technical guiding questions to resolve
divergences between agent proposals (e.g., cost vs. sustainability conflicts).
Finally, send the consolidated debate to the Presenter.

## Personality
Professional facilitator, neutral, organized, and pragmatic. Keeps the group
focused on the problem and avoids endless discussions.

## Likes
- Responses organized by topics, compliance with timelines, solutions that combine
  efficiency and viability.

## Dislikes
- Lack of focus from specialists, deviations from the main topic, infinite debates
  without practical conclusions.

## Output Expected
Clear questions directed to specific agents and periodic syntheses of the plan's status.

## Response Language Constraints
CRITICAL: Although all instructions, guidelines, and prompts are defined in English
to maximize reasoning performance, you MUST write all your thoughts, dialogues, and
final outputs in Brazilian Portuguese (Português do Brasil). Under no circumstances
should you reply in English.
```

---

## 2. Prompt de Conversa — Input Inicial (Briefing do Cliente)

Este foi o prompt colado manualmente no campo de mensagem do Playground do AutoGen Studio para iniciar o debate entre os agentes. É o ponto de entrada do sistema em linguagem natural.

```
Olá especialistas,

Segue o briefing inicial do cliente para iniciarmos o debate:

Briefing Inicial do Cliente

Pedido do Usuário: "Preciso de uma proposta urbana sustentável para revitalizar
uma área degradada da cidade, considerando mobilidade, infraestrutura, meio ambiente,
habitação, inclusão social, orçamento limitado e viabilidade técnica."

Parâmetros:
- Orçamento: R$ 15 milhões
- Área: Antiga Zona Industrial Portuária (10 hectares)
- População atual: ~350 famílias em ocupações informais
- Meta principal: Integrar a área ao centro urbano reduzindo emissões e mantendo
  a comunidade original.

Agora, gostaria que cada um de vocês pudesse compartilhar suas primeiras impressões
e propostas baseadas nesta informação. Vamos focar nas áreas de mobilidade,
infraestrutura, meio ambiente, habitação, inclusão social e orçamento limitado
e viabilidade técnica.

Perguntas Iniciais:
1. Mobilidade: Como vê a integração da área ao centro urbano? Quais são as
   principais vias de acesso?
2. Infraestrutura: Que tipos de infraestruturas serão necessárias (economia de
   escala, etc.)?
3. Meio Ambiente: Como garantir a sustentabilidade e redução das emissões?
4. Habitação: Que tipo de moradias serão propostas para as famílias atuais?
   Como planejar a habilitação dessas famílias?
5. Inclusão Social: Como podemos garantir a participação da comunidade local
   no processo e nas decisões finais?
6. Orçamento Limitado: Quais estratégias vocês sugerem para manter o projeto
   dentro do orçamento?

Vamos começar com as primeiras observações de cada especialista.
```

---

## 3. Formato de Resposta Observado — Estrutura das Mensagens

Durante a execução, os agentes seguiram espontaneamente um formato estruturado de resposta, derivado dos seus system messages. O padrão observado foi:

### Padrão do Orquestrador (1ª fala)
- **Abertura**: Cumprimento direto aos colegas especialistas
- **Contextualização**: Resumo do briefing e dos parâmetros do projeto
- **Direcionamento**: Lista de perguntas temáticas (Mobilidade, Infraestrutura, Meio Ambiente, Habitação, Inclusão Social, Orçamento)
- **Convite**: Solicitação de primeiras impressões de cada especialista
- **Encerramento**: Chamada para discussão aberta

**Exemplo real da sessão (Orquestrador):**
> "Olá especialistas. Segue o nosso briefing de projeto para iniciarmos o debate [...] Qual é a sua visão sobre essas questões?"

---

### Padrão dos Especialistas (rodadas de debate)
- **Abertura**: Saudação aos colegas e agradecimento pela oportunidade
- **Corpo**: Resposta estruturada por tópicos numerados (Mobilidade, Infraestrutura, Meio Ambiente, Habitação, Inclusão Social, Orçamento)
- **Posicionamento técnico**: Cada agente defende seu ponto de vista profissional
- **Pergunta de passagem**: Convite aos outros colegas para comentar

**Exemplo real — Urbanista (1ª fala):**
> "Para integrar a área à cidade, é essencial criar uma rede de vias que facilite o acesso tanto para pedestres quanto para veículos. Sugiro a criação de um corredor exclusivo para ciclistas conectando as principais vias da área ao centro urbano."

**Exemplo real — Sociólogo Urbano (1ª fala):**
> Focou em Inclusão Social (fóruns públicos, workshops comunitários), Orçamento (PPPs com regulação anti-gentrificação) e encerrou com: *"Obrigado pela discussão e vamos avançar!"*

---

### Padrão do Apresentador (consolidação final)
- Compilação das contribuições de todos os especialistas
- Estrutura em seções temáticas (Mobilidade, Infraestrutura, Meio Ambiente, Habitação, Inclusão Social, Orçamento)
- Conclusão integrativa com visão holística do plano
- Chamada para próximas etapas

**Exemplo real — Feedback final dos agentes:**
> "A revitalização da área antiga Zona Industrial Portuária deve ser abordada de forma holística e sustentável. É crucial considerar as necessidades das famílias atuais, garantir a integração à cidade central, promover o uso sustentável do transporte, implementar infraestruturas eficientes, proteger o meio ambiente, proporcionar moradias acessíveis e de baixo custo, e garantir a participação da comunidade local."

---

## 4. Observações Técnicas Validadas em Teste

| Parâmetro | Valor Testado | Resultado |
| :--- | :--- | :--- |
| Modelo | Qwen2.5-7B-Instruct-GGUF (Q4_K_M) | ✅ Funcional |
| Temperature | 0.7 | Respostas criativas mas coerentes |
| Max Tokens | 1500 | Respostas completas, sem truncamento crítico |
| Contexto acumulado | ~7000 tokens (2 agentes) | ⚠️ Risco de timeout acima de 3 agentes seguidos |
| Idioma de saída | Português do Brasil | ✅ Respeitado por todos os agentes |
| Formato de resposta | Tópicos numerados por área | ✅ Consistente entre agentes |
