import openai
from typing import List
from dotenv import dotenv_values
import palooza_wizard.constants as ct
import palooza_wizard.chatgpt as chatgpt
import tiktoken
import logging

openai.api_key = ct.OPEN_AI_API_KEY


def get_completion_from_messages(
    messages, model="gpt-4", temperature=0, max_tokens=500
):  # gpt-4
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


def get_system_message_for_function(function_name: str) -> str:
    system_message = f"""
    Create a Python function with a proper name starting with '{function_name}' that extracts all relevant data from
    the provided HTML code by the user and returns the data as a dictionary. The keys of the dictionaries should be as
    few as possible. Utilize Beautiful Soup (beautifulsoup4) to implement this Python function. The output should
    consist solely of Python code without any English words.
    """
    return system_message


def get_system_message_for_agent() -> str:
    system_message = f"""
    Create a python class called 'agent' which implements as methods the defined functions passed by the user in the prompt.
    In addition, include a new method called 'extract_data' that accepts as argument a beautifulsoup object and a url and which uses all the methods of the class and returns a dictionary with the result
    of each method. Constructor method must not recieve any parameter, instead, each method within the class must accept as parameter a BeautifulSoup object
    """
    return system_message


def get_messages_for_function(
    user_message: str, function_name: str
) -> List[str]:
    system_message = get_system_message_for_function(function_name)
    num_tokens = chatgpt.num_tokens_for_model(
        system_message + user_message
    )
    print("Number of tokens to be sent: ", num_tokens)
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    return messages


def format_python_completion(completion: str) -> str:
    if completion.find("```python") != -1:
        a, b = completion.find("```python"), completion.find(
            "```", len("```python") + 1, len(completion)
        )
        return completion[a + len("```python") : b]
    return completion
