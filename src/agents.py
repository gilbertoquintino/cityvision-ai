# -*- coding: utf-8 -*-
"""
CityVision AI - Configuração e Instanciação de Agentes AutoGen
Este arquivo é responsável por:
1. Ler os arquivos de system-message.md e personality.md de cada agente.
2. Criar os objetos AssistantAgent ou UserProxyAgent do AutoGen para cada participante.
3. Definir as configurações de conexão (llm_config) apontando para o servidor local do LM Studio.
"""

from autogen import AssistantAgent, UserProxyAgent
from src.utils import load_agent_prompts

def create_agents(llm_config):
    """
    Cria e retorna a lista de agentes configurados no AutoGen.
    """
    # 1. User Proxy Agent (Representa o Cliente/Usuário final que fornece o briefing)
    user_proxy = UserProxyAgent(
        name="Cliente",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,  # Não responde de volta no meio do debate automático
        code_execution_config=False,  # Sem execução de código local
    )
    
    # 2. Orquestrador (Moderador do debate)
    orchestrator = AssistantAgent(
        name="Orquestrador",
        llm_config=llm_config,
        system_message=load_agent_prompts("orchestrator"),
    )
    
    # 3. Especialista - Urbanista (Urbanist)
    urbanist = AssistantAgent(
        name="Urbanista",
        llm_config=llm_config,
        system_message=load_agent_prompts("urbanista"),
    )
    
    # 4. Especialista - Engenheiro de Infraestrutura (Infrastructure Engineer)
    infrastructure = AssistantAgent(
        name="Engenheiro_de_Infraestrutura",
        llm_config=llm_config,
        system_message=load_agent_prompts("infraestrutura"),
    )
    
    # 5. Especialista - Especialista em Mobilidade (Mobility Specialist)
    mobility = AssistantAgent(
        name="Especialista_em_Mobilidade",
        llm_config=llm_config,
        system_message=load_agent_prompts("mobilidade"),
    )
    
    # 6. Especialista - Ambientalista (Environmentalist)
    environmentalist = AssistantAgent(
        name="Ambientalista",
        llm_config=llm_config,
        system_message=load_agent_prompts("ambientalista"),
    )
    
    # 7. Especialista - Sociólogo Urbano (Urban Sociologist)
    sociologist = AssistantAgent(
        name="Sociologo_Urbano",
        llm_config=llm_config,
        system_message=load_agent_prompts("sociologo"),
    )
    
    # 8. Especialista - Economista Urbano (Urban Economist)
    economist = AssistantAgent(
        name="Economista_Urbano",
        llm_config=llm_config,
        system_message=load_agent_prompts("economista"),
    )
    
    # 9. Apresentador de Projeto (Compilador da proposta final)
    presenter = AssistantAgent(
        name="Apresentador_de_Projeto",
        llm_config=llm_config,
        system_message=load_agent_prompts("apresentador"),
    )
    
    return {
        "user_proxy": user_proxy,
        "orchestrator": orchestrator,
        "urbanista": urbanist,
        "infraestrutura": infrastructure,
        "mobilidade": mobility,
        "ambientalista": environmentalist,
        "sociologo": sociologist,
        "economista": economist,
        "apresentador": presenter,
    }
