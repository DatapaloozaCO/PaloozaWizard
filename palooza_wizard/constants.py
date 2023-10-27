from dotenv import dotenv_values

# Load environment variables
config = dotenv_values(".env")
OPEN_AI_API_KEY = config["OPEN_AI_API_KEY"]

# Folder for saving intermediary results.
HTML_OUTPUT_FOLDER = "./outputs/html/"
PYTHON_OUTPUT_FOLDER = "./outputs/python/"
AGENT_OUTPUT_FOLDER = "./outputs/agent/"
IMPORTANCE_OUTPUT_FOLDER = "./outputs/importance/"

FOLDERS = [
    HTML_OUTPUT_FOLDER, 
    PYTHON_OUTPUT_FOLDER, 
    AGENT_OUTPUT_FOLDER,
    IMPORTANCE_OUTPUT_FOLDER
]

# Proxies data
PROXIES = {"http": config["PROXY_HOST"]}
PROXY_USERNAME = config["USERNAME"]
PROXY_PASSWORD = config["PASSWORD"]

FAKE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'
REQUEST_TIMEOUT = 10

# Selector label
SELECTOR_LABEL = "selector"
ROOT_LABEL = "root"