# Modelos de LLM Testados

> [!IMPORTANT]
> **Especificações do Ambiente de Desenvolvimento (Hardware)**:
> Os testes de desempenho e a escolha do modelo foram realizados localmente no computador de desenvolvimento com a seguinte especificação:
> - **Dispositivo**: Samsung Book4 360 (Book4-360-Gilberto)
> - **Processador**: Intel(R) Core(TM) 5 120U (1.40 GHz)
> - **Memória RAM Instalada**: 16,0 GB LPDDR5 (Velocidade: 6000 MT/s)
> - **Placa de Vídeo (GPU)**: Intel(R) Graphics (128 MB VRAM dedicada / memória compartilhada do sistema)
> - **Armazenamento**: SSD 477 GB
>
> Diante dessa configuração de hardware intermediário (com GPU integrada compartilhando a RAM do sistema), o consumo de memória VRAM é o fator mais crítico para garantir a estabilidade do debate multiagente simultâneo.

Use a tabela abaixo para mapear os modelos de IA testados localmente no LM Studio durante o desenvolvimento do projeto:

| Nome do Modelo | Compatibilidade AutoGen | Velocidade (t/s) | Qualidade da Resposta | Consumo de Recursos | Situação / Observações |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Qwen2.5-7B-Instruct-GGUF** | **Total (Adotado)** | **Excelente (Rápida)** | **Excelente** | **Médio (~4.68 GB)** | **Modelo Escolhido (Quantização Q4_K_M)**. Apresentou o melhor equilíbrio entre inteligência, obediência à persona e estabilidade em 16GB de RAM. |
| **GPT-OSS 20B** | Alta | Muito Baixa | Excelente | Altíssimo (>16GB VRAM) | **Inviabilizado**. O consumo excessivo de memória causou lentidão crítica e travamentos constantes no hardware intermediário. |
| **Llama 3 8B Instruct** | Alta | Boa | Excelente | Médio (~6GB VRAM) | Excelente, mas levemente mais pesado em VRAM comparado ao Qwen2.5. |
| **Mistral 7B Instruct v0.3**| Alta | Boa | Muito Boa | Médio (~5.5GB VRAM) | Bom desempenho, mas ligeiramente inferior na consistência em português. |
| **Phi 3 3.8B Instruct** | Média | Muito Rápido | Razoável | Baixo (~3.5GB VRAM) | Rápido, mas às vezes ignora restrições negativas (Dislikes). |
| **Gemma 4B** | Média | Muito Rápido | Baixa-Média | Baixo (~3.8GB VRAM) | Apresenta menor aderência à persona e instruções complexas sob turnos longos. |
| **Nvidia Nemotron** | Incompatível | N/A | N/A | N/A | Apresentou incompatibilidade de formato e quebra operacional com o framework AutoGen. |
