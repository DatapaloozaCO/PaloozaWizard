from bs4 import BeautifulSoup
import palooza_wizard.chatgpt as pwc
import palooza_wizard.constants as ct
from typing import List
import os 

def get_agent_code(file_name: str):
    python_code = load_code_string(file_name = file_name)
    system_message = pwc.get_system_message_for_agent()
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": python_code},
    ]
    agent_code = pwc.get_completion_from_messages(messages)
    agent_code = pwc.format_python_completion(agent_code)
    with open(f"./{file_name}", "w") as f:
        f.write(agent_code)

def get_element_metadata(task: dict) -> tuple:
    data = task["element"]
    tag, attribute, value = data["tag"], data["attribute"], data["value"]
    return tag, attribute, value

def get_agent_function(file_path: str) -> str:
    with open(f'{ct.IMPORTANCE_OUTPUT_FOLDER}/{file_path}', "r", encoding='windows-1252') as f:
        user_message = f.read()
    function_name = file_path
    messages = pwc.get_messages_for_function(user_message = user_message, function_name = function_name)
    completion = pwc.get_completion_from_messages(messages = messages)
    return completion

def save_completion(completion: str, file_name: str) -> None:
    file_name = file_name.replace(".html", ".py")
    with open(f"{ct.AGENT_OUTPUT_FOLDER}/{file_name}", "a") as f:
        f.write(completion)
        f.write("\n\n")

def get_agent_functions() -> None:
    """Get agent functions

    Args:
        - soup (BeautifulSoup)
        - tasks (List[dict]): [{"element": {"tag": "div", "attribute": "class", "value": "example-class"}, "function_name": "example_name"}]
        - file_name (str)
    Return:
        - None
    """
    #try:
    #    #os.remove(f"{ct.FUNCTIONS_OUTPUT_FOLDER}/{file_name}")
    #    os.remove(file_name)
    #except:
    #    pass
    
    file_paths = os.listdir(ct.IMPORTANCE_OUTPUT_FOLDER)
    #file_paths = [file_paths[index] for index in indexes]

    for file_path in file_paths:
        completion = get_agent_function(file_path)
        completion = pwc.format_python_completion(completion = completion)
        save_completion(completion = completion, file_name = file_path)

def load_code_string(file_name: str):
    #{ct.FUNCTIONS_OUTPUT_FOLDER}
    with open(f"./{file_name}", "r") as f:
         python_code = f.read()
         print(python_code)
    return python_code
