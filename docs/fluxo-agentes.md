# Fluxo de Conversa dos Agentes

O fluxo de comunicação no CityVision AI segue uma dinâmica de debate estruturado:

1. **Entrada do Briefing**: O usuário insere o briefing inicial no terminal ou arquivo de configuração.
2. **Início pelo Orquestrador**: O Agente Orquestrador analisa o briefing inicial, divide o problema em desafios principais e convoca a rodada de debates, direcionando a palavra para o primeiro especialista (geralmente o Urbanista ou Ambientalista).
3. **Fase de Debate e Contribuição**:
   - Cada agente especializado toma a palavra de forma sequencial ou dinâmica.
   - Os agentes analisam a proposta sob a ótica de sua persona (e.g., o Economista avalia o impacto financeiro da proposta do Ambientalista; o Sociólogo questiona a viabilidade habitacional do plano do Urbanista).
   - O Orquestrador faz a mediação caso haja loops ou desvios do tema.
4. **Consolidação**:
   - Uma vez que os especialistas chegam a um consenso básico ou o limite de interações é atingido, o Orquestrador repassa o histórico completo do debate para o **Apresentador de Projeto**.
5. **Narrativa Final**:
   - O Apresentador de Projeto traduz a linguagem estritamente técnica do debate para um relatório estruturado de consultoria de alto nível (Markdown), contendo Introdução, Proposta de Intervenção, Fatores Técnicos, Viabilidade e Conclusão.
