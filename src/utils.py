# -*- coding: utf-8 -*-
"""
CityVision AI - Funções Auxiliares (Utilities)
Este arquivo contém funções úteis para suporte ao sistema:
1. Leitura e parsing dos briefings do usuário.
2. Carregamento unificado dos system prompts dos agentes.
3. Salvamento estruturado das conversas em arquivos de evidência e log.
"""

import os
import time

def load_briefing(file_path):
    """
    Carrega o texto do briefing inicial de revitalização.
    """
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_agent_prompts(agent_name, base_dir=None):
    """
    Carrega o system-message.md e o personality.md de um agente e os concatena.
    """
    if base_dir is None:
        # Pega a pasta 'agents' no diretório raiz do projeto (um nível acima de 'src')
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.join(os.path.dirname(current_dir), "agents")
        
    agent_dir = os.path.join(base_dir, agent_name)
    system_message_path = os.path.join(agent_dir, "system-message.md")
    personality_path = os.path.join(agent_dir, "personality.md")
    
    system_msg = ""
    if os.path.exists(system_message_path):
        with open(system_message_path, "r", encoding="utf-8") as f:
            system_msg = f.read()
            
    personality = ""
    if os.path.exists(personality_path):
        with open(personality_path, "r", encoding="utf-8") as f:
            personality = f.read()
            
    full_prompt = f"{system_msg}\n\n{personality}"
    return full_prompt.strip()

def save_debate_log(chat_history, output_dir=None):
    """
    Salva o log de debate dos agentes em formato legível (.txt ou .md).
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    if output_dir is None:
        output_dir = os.path.join(project_root, "logs")
        
    os.makedirs(output_dir, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    log_file = os.path.join(output_dir, f"debate_{timestamp}.md")
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# Log de Debate - CityVision AI\n")
        f.write(f"Data/Hora: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for msg in chat_history:
            sender = msg.get("name", "Unknown")
            content = msg.get("content", "")
            f.write(f"### **{sender}**\n")
            f.write(f"{content}\n\n")
            f.write("---\n\n")
            
    # Salvar cópia também na pasta 'evidencias/execucoes'
    evidencias_dir = os.path.join(project_root, "evidencias", "execucoes")
    os.makedirs(evidencias_dir, exist_ok=True)
    evidencias_file = os.path.join(evidencias_dir, f"debate_{timestamp}.md")
    try:
        import shutil
        shutil.copy2(log_file, evidencias_file)
        print(f"Log do debate salvo em:\n - {log_file}\n - {evidencias_file}")
    except Exception as e:
        print(f"Erro ao salvar cópia em evidencias: {e}")
        
    return log_file
