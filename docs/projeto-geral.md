# Projeto Geral - CityVision AI

## 🎯 Objetivo Geral
Desenvolver um framework inteligente multiagente capaz de atuar como uma consultoria autônoma de planejamento urbano, gerando propostas completas de revitalização para áreas degradadas com foco em sustentabilidade e inclusão social.

## ⚠️ O Problema Urbano
Cidades possuem áreas degradadas (zonas industriais abandonadas, centros históricos desvalorizados, periferias sem infraestrutura) que necessitam de intervenção. Revitalizar essas áreas envolve conflitos de interesse:
- O economista quer o menor custo e maior retorno financeiro.
- O ambientalista quer preservar ecossistemas e criar áreas verdes.
- O sociólogo quer evitar a gentrificação e garantir moradias acessíveis.
- O engenheiro quer viabilidade técnica e infraestrutura robusta.

Integrar essas visões de maneira manual é demorado e sujeito a falhas de comunicação técnica.

## 💡 Proposta de Solução
Utilizar a tecnologia de **Agentic AI** através do framework **AutoGen** para simular uma mesa redonda de especialistas. O sistema recebe as dores da região em linguagem natural (briefing) e ativa agentes especializados para debater o problema de forma autônoma. O debate converge em uma proposta de revitalização equilibrada, compilada em um documento final pelo agente Apresentador.

## 📦 Entregas Esperadas
1. **Código-fonte**: Script de orquestração multiagente funcional integrado com LLM local.
2. **Histórico de Execução**: Transcrições completas dos debates dos agentes provando a colaboração.
3. **Proposta Final**: O relatório executivo estruturado gerado pelo agente Apresentador.
4. **Benchmark**: Relatório comparativo com a performance dos modelos de IA testados localmente.
