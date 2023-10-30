from palooza_wizard.graph import PaloozaGraph
from palooza_wizard.algorithms.degree_importance import degree_importance, get_soup_nodes
from palooza_wizard.agent import get_agent_functions
import sys 
import requests
from bs4 import BeautifulSoup
import palooza_wizard.utils.files as files
import palooza_wizard.utils.process as process
import palooza_wizard.constants as ct
import outputs.agent.rubmaps_106
import outputs.agent.rubmaps_129
import outputs.agent.rubmaps_21
import json

#website_name = "oulunlippo"
#url = "https://www.oulunlippo.fi/"

website_name = "rubmaps"
url = "https://www.rubmaps.ch/erotic-massage-chinese-goose-massage-cincinnati-oh-33075#rubmaps"
    
soup = files.get_soup_from_url(url)
soup = process.process_soup(soup)

html_code = str(soup)
datas = list()
datas.append(outputs.agent.rubmaps_106.rubmaps_106(html_code))
datas.append(outputs.agent.rubmaps_129.rubmaps_129(html_code))
datas.append(outputs.agent.rubmaps_21.rubmaps_21_html(html_code))

JSONS_OUTPUT = "./outputs/jsons"
counter = 1
for data in datas: 
    with open(f"{JSONS_OUTPUT}/data{counter}.json", "w") as f:
        f.write(json.dumps(data))
    counter += 1