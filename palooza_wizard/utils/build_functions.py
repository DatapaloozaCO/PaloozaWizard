from bs4 import BeautifulSoup
from typing import List
from chatgpt.utils import get_messages_for_function, get_completion_from_messages, format_python_completion
import os
import constants as ct

def get_element_metadata(task: dict) -> tuple:
    data = task["element"]
    tag, attribute, value = data["tag"], data["attribute"], data["value"]
    return tag, attribute, value

def get_scraper_function(soup: BeautifulSoup, task: dict) -> str:
    tag, attribute, value = get_element_metadata(task)
    user_message = str(soup.find(tag, attrs = {attribute: value}))
    function_name = task["function_name"]
    messages = get_messages_for_function(user_message = user_message, function_name = function_name)
    completion = get_completion_from_messages(messages = messages)
    return completion

def save_completion(completion: str, file_name: str) -> None:
    with open(f"{ct.FUNCTIONS_OUTPUT_FOLDER}/{file_name}", "a") as f:
        f.write(completion)
        f.write("\n\n")

def get_scraper_functions(soup: BeautifulSoup, tasks: List[dict], file_name: str) -> None:
    """Get scraper functions

    Args:
        - soup (BeautifulSoup)
        - tasks (List[dict]): [{"element": {"tag": "div", "attribute": "class", "value": "example-class"}, "function_name": "example_name"}]
        - file_name (str)
    Return:
        - None
    """
    try:
        os.remove(f"{ct.FUNCTIONS_OUTPUT_FOLDER}/{file_name}")
    except:
        pass
    for task in tasks:
        completion = get_scraper_function(soup, task)
        completion = format_python_completion(completion = completion)
        save_completion(completion = completion, file_name = file_name)