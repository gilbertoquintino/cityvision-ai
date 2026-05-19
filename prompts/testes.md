# Roteiro de Testes de Prompts

Use este arquivo para planejar e registrar as baterias de testes aplicados ao sistema de agentes:

## Teste 1: Consistência de Persona
- **Objetivo**: Testar se os agentes mantêm suas respectivas posições sem se desviar para a área técnica do outro.
- **Critério de Sucesso**: O Economista deve objetar a custos elevados; o Sociólogo deve debater moradia acessível; o Engenheiro deve focar em redes físicas.

## Teste 2: Resolução de Conflitos
- **Objetivo**: Avaliar a mediação do Orquestrador diante de opiniões opostas (ex: Sociólogo vs Economista sobre habitação social).
- **Critério de Sucesso**: O Orquestrador deve propor ou exigir uma alternativa híbrida que acomode ambos os limites.

## Teste 3: Coerência do Relatório Final
- **Objetivo**: Verificar se o Apresentador incluiu dados reais de todos os especialistas no documento final.
- **Critério de Sucesso**: O documento final não pode ter placeholders e deve detalhar a proposta integrada.
