# -*- coding: utf-8 -*-
"""
CityVision AI - Main Entrypoint
Este arquivo é o ponto de entrada do sistema. Sua função é:
1. Carregar as configurações (via config.py).
2. Carregar o briefing inicial (via prompts/briefing-inicial.md).
3. Instanciar os agentes (via agents.py).
4. Configurar a conversa em grupo (GroupChat) com fluxo de orquestração estruturado.
5. Rodar a simulação e salvar as evidências em logs/ e evidencias/execucoes/.
"""

import os
import sys
import autogen

# Ajustar o path para garantir que importações locais funcionem corretamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import (
    LM_STUDIO_BASE_URL,
    LM_STUDIO_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
    MAX_ROUND_CHAT,
)
from src.utils import load_briefing, save_debate_log
from src.agents import create_agents

def main():
    print("=" * 60)
    print("           CITYVISION AI - SISTEMA MULTIAGENTE            ")
    print("=" * 60)
    print("Inicializando componentes do sistema...")

    # 1. Configurar LLM usando os parâmetros do LM Studio
    llm_config = {
        "config_list": [
            {
                "model": MODEL_NAME,
                "base_url": LM_STUDIO_BASE_URL,
                "api_key": LM_STUDIO_API_KEY,
            }
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }

    # 2. Criar instâncias dos agentes
    agents = create_agents(llm_config)
    
    user_proxy = agents["user_proxy"]
    orchestrator = agents["orchestrator"]
    urbanist = agents["urbanista"]
    infrastructure = agents["infraestrutura"]
    mobility = agents["mobilidade"]
    environmentalist = agents["ambientalista"]
    sociologist = agents["sociologo"]
    economist = agents["economista"]
    presenter = agents["apresentador"]

    # 3. Carregar o Briefing Inicial do Cliente
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    briefing_path = os.path.join(project_root, "prompts", "briefing-inicial.md")
    
    briefing_content = load_briefing(briefing_path)
    if not briefing_content:
        print("Erro: Arquivo de briefing inicial não encontrado!")
        sys.exit(1)
        
    print("Briefing inicial carregado com sucesso.")

    # 4. Definir a lógica personalizada de seleção do próximo orador (Speaker Selection)
    def custom_speaker_selection(last_speaker, groupchat):
        """
        Controla o fluxo do debate garantindo uma orquestração limpa e profissional.
        Evita o caos gerado pela seleção aleatória de modelos locais menores.
        """
        messages = groupchat.messages
        if not messages:
            return orchestrator
            
        # Se a conversa acabou de começar com o briefing do Cliente, o Orquestrador assume
        if last_speaker.name == user_proxy.name:
            return orchestrator
            
        # Se o Apresentador já falou, terminamos o debate
        if last_speaker.name == presenter.name:
            return None
            
        # Se atingirmos o limite do chat, chamamos o Apresentador de Projeto para consolidar e finalizar
        if len(messages) >= MAX_ROUND_CHAT - 2:
            print("\n[Orquestração] Limite de debate se aproximando. Chamando o Apresentador para consolidar...\n")
            return presenter
            
        # Se o último orador foi o Orquestrador, analisamos a menção para escolher o especialista.
        # Caso contrário, seguimos a ordem natural.
        if last_speaker.name == orchestrator.name:
            last_msg = messages[-1]["content"].lower()
            
            # Dicionário de mapeamento de nomes/menções aos agentes
            agent_map = {
                "urbanista": urbanist,
                "infraestrutura": infrastructure,
                "mobilidade": mobility,
                "ambientalista": environmentalist,
                "sociologo": sociologist,
                "sociólogo": sociologist,
                "economista": economist,
                "apresentador": presenter,
            }
            
            for key, agent in agent_map.items():
                if key in last_msg:
                    print(f"\n[Orquestração] Orquestrador passou a palavra para: {agent.name}\n")
                    return agent
            
            # Se não houve menção explícita a nenhum agente, fazemos round-robin dos especialistas que ainda não falaram
            specialists = [urbanist, infrastructure, mobility, environmentalist, sociologist, economist]
            spoken_names = [msg["name"] for msg in messages]
            
            for spec in specialists:
                if spec.name not in spoken_names:
                    print(f"\n[Orquestração] Sequência de introdução. Passando para: {spec.name}\n")
                    return spec
            
            # Se todos já falaram, o Orquestrador pode escolher um aleatoriamente para debate ou voltar a palavra para ele mesmo
            return orchestrator
            
        # Se o último orador foi qualquer especialista, a palavra volta sempre para o Orquestrador moderar
        print(f"\n[Orquestração] {last_speaker.name} concluiu sua fala. Devolvendo controle ao Orquestrador...\n")
        return orchestrator

    # 5. Configurar o GroupChat e o GroupChatManager
    # Lista contendo os agentes ativos no debate
    debate_agents = [
        user_proxy,
        orchestrator,
        urbanist,
        infrastructure,
        mobility,
        environmentalist,
        sociologist,
        economist,
        presenter,
    ]
    
    groupchat = autogen.GroupChat(
        agents=debate_agents,
        messages=[],
        max_round=MAX_ROUND_CHAT,
        speaker_selection_method=custom_speaker_selection,
    )
    
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config,
    )

    print("\nIniciando o debate do projeto CityVision AI...")
    print("=" * 60)
    
    # 6. Disparar a conversa
    # O cliente envia o briefing inicial para o GroupChatManager
    user_proxy.initiate_chat(
        manager,
        message=f"Olá especialistas. Segue o nosso briefing de projeto para iniciarmos o debate:\n\n{briefing_content}"
    )
    
    print("=" * 60)
    print("Debate concluído com sucesso!")
    
    # 7. Salvar os Logs de Conversa
    log_file = save_debate_log(groupchat.messages)
    print(f"Execução finalizada com êxito! Evidências salvas em logs.")

if __name__ == "__main__":
    main()
