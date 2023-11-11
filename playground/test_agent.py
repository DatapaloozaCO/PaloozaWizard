#from outputs.agent.startupeable_1 import function_1
#from outputs.agent.startupeable_2 import function_2
import json 
import palooza_wizard.constants as ct
from outputs.agent.rubmaps_cleveland_1 import rubmaps_cleveland_1
from outputs.agent.rubmaps_cleveland_2 import rubmaps_cleveland_2_extract
from outputs.agent.rubmaps_cleveland_3 import rubmaps_cleveland_3
from outputs.agent.rubmaps_cleveland_4 import rubmaps_cleveland_4_html
from outputs.agent.rubmaps_cleveland_5 import rubmaps_cleveland_4

functions = [rubmaps_cleveland_1, rubmaps_cleveland_2_extract,
             rubmaps_cleveland_3, rubmaps_cleveland_4_html, rubmaps_cleveland_4]

website_name = "./rubmaps_cleveland.html"
with open(website_name, "r") as f:
    html_code = str(f.read())

for function in functions:
    try:
        data = function(html_code)
        with open(f"{ct.DATA_OUTPUT_FOLDER}/{function.__name__}.json", "w") as f:
            f.write(json.dumps(data))
    except Exception as e:
        print(str(e))
