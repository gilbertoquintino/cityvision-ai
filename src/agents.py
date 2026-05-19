# -*- coding: utf-8 -*-
"""
CityVision AI - Configuração e Instanciação de Agentes AutoGen
Este arquivo será responsável por:
1. Ler os arquivos de system-message.md e personality.md de cada agente.
2. Criar os objetos AssistantAgent ou UserProxyAgent do AutoGen para cada participante:
   - Orchestrator
   - Urbanist
   - Infrastructure
   - Mobility
   - Environmentalist
   - Sociologist
   - Economist
   - Presenter
3. Definir as configurações de conexão (llm_config) apontando para o servidor local do LM Studio.
"""

import os

def create_agents(llm_config):
    """
    Cria e retorna a lista de agentes configurados no AutoGen.
    """
    # TODO: Implementar leitura dinâmica das pastas em 'agents/'
    # TODO: Instanciar AssistantAgent do AutoGen com as system messages lidas
    return {}
