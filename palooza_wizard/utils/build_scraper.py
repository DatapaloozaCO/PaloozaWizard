from chatgpt.utils import get_system_message_for_scraper, get_completion_from_messages, format_python_completion
import constants as ct

def load_code_string(file_name: str):
    with open(f"{ct.FUNCTIONS_OUTPUT_FOLDER}/{file_name}", "r") as f:
         python_code = f.read()
         print(python_code)
    return python_code

def get_scraper_code(file_name: str):
    python_code = load_code_string(file_name = file_name)
    system_message = get_system_message_for_scraper()
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": python_code},
    ]
    scraper_code = get_completion_from_messages(messages)
    scraper_code = format_python_completion(scraper_code)
    with open(f"{ct.SCRAPER_OUTPUT_FOLDER}/{file_name}", "w") as f:
        f.write(scraper_code)