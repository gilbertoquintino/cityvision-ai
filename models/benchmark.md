# Benchmark de Modelos - Critérios de Avaliação

Template de avaliação para novos modelos de LLM integrados ao sistema:

1. **Aderência à Persona (Peso 3)**: O modelo manteve o tom, linguagem e restrições do especialista designado ao longo de 5+ turnos?
2. **Coesão Lógica (Peso 3)**: A resposta do modelo se conecta diretamente com a última fala do agente anterior, ou ele respondeu algo genérico?
3. **Resolução de Instruções (Peso 2)**: Seguiu os formatos solicitados (Markdown, listas, etc.)?
4. **Desempenho Técnico (Peso 2)**: Velocidade (tokens por segundo) aceitável e consumo estável de memória VRAM na máquina de execução?

## Pontuação Final:
- **0 a 4**: Não recomendado.
- **5 a 7**: Utilizável com ressalvas.
- **8 a 10**: Altamente recomendado para uso no ecossistema multiagente.
