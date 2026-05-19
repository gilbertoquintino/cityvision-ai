# -*- coding: utf-8 -*-
"""
CityVision AI - Configurações Gerais do Sistema
Este arquivo centraliza:
1. Parâmetros de rede para conexão com a API do LM Studio (URL e porta base).
2. Nome do modelo de LLM carregado no LM Studio.
3. Hiperparâmetros de inferência (temperatura, max_tokens, etc.).
4. Limites de iteração (número máximo de mensagens no debate).
"""

import os

# Configuração da API do LM Studio (Compatível com OpenAI)
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
LM_STUDIO_API_KEY = "not-needed" # LM Studio local não exige chave de API ativa

# Configuração do Modelo carregado
MODEL_NAME = "llama-3-8b-instruct" # Nome do modelo ativo no LM Studio

# Parâmetros de Inferência
TEMPERATURE = 0.7
MAX_TOKENS = 1500

# Parâmetros do Debate
MAX_ROUND_CHAT = 15 # Limite máximo de falas no debate antes de consolidar
