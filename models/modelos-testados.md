# Modelos de LLM Testados

> [!IMPORTANT]
> **Nota sobre os dados**: Os valores de velocidade, qualidade de resposta e consumo de recursos apresentados abaixo são **estimativas iniciais baseadas no material de aula e estudos de referência**. A equipe realizará testes empíricos de desempenho local na Fase 6 para consolidar o benchmark final de VRAM e velocidade real de inferência (tokens/segundo).

Use a tabela abaixo para mapear todos os modelos de IA testados localmente no LM Studio durante o desenvolvimento do projeto:

| Nome do Modelo | Compatibilidade AutoGen | Velocidade (t/s) | Qualidade da Resposta | Consumo de Recursos | Observações |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GPT-OSS 20B** | Alta | Baixa | Excelente | Alto (>16GB VRAM) | Modelo de referência destacado em aula; alto poder de raciocínio. |
| **Llama 3 8B Instruct** | Alta | Boa | Excelente | Médio (~6GB VRAM) | Excelente entendimento de persona e instruções complexas. |
| **Mistral 7B Instruct v0.3**| Alta | Boa | Muito Boa | Médio (~5.5GB VRAM) | Bom raciocínio de engenharia e economia. |
| **Phi 3 3.8B Instruct** | Média | Muito Rápido | Razoável | Baixo (~3.5GB VRAM) | Rápido, mas às vezes ignora restrições negativas (Dislikes). |
| **Gemma 4B** | Média | Muito Rápido | Baixa-Média | Baixo (~3.8GB VRAM) | Rápido, mas apresenta menor aderência à persona e instruções complexas. |
| **Nvidia Nemotron** | Incompatível | N/A | N/A | N/A | Apresentou incompatibilidade com o framework AutoGen nos testes preliminares. |
