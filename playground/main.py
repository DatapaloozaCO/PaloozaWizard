from palooza_wizard.utils.files import download_or_load_soup
from palooza_wizard.utils.process import process_soup
from palooza_wizard.agent import get_agent_functions
from palooza_wizard.chatgpt import num_tokens_from_string 
from bs4 import BeautifulSoup
# Download or load soup
#url = "https://www.amazon.com/Molblly-Shredded-Standard-Adjustable-Hypoallergenic/dp/B08X4TQJTL/?_encoding=UTF8&pd_rd_w=ABAfK&content-id=amzn1.sym.952cfb50-b01e-485f-be6e-00434541418b%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=952cfb50-b01e-485f-be6e-00434541418b&pf_rd_r=DNTYSCCM3CE36ZBNPB9Q&pd_rd_wg=vsfzz&pd_rd_r=a7259352-0e85-4361-934b-108279598eb3&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
#soup = download_or_load_soup(url, file_path="outputs/html/test.html")

url = "https://www.amazon.com/"
soup = download_or_load_soup(url, file_path="outputs/html/amazon.html")
#minified = minify_html.minify(str(soup), minify_js=True, remove_processing_instructions=True)
#with open(f"minified.html", "w") as f:
#    f.write(minified)
#soup = BeautifulSoup(minified, "html.parser")


soup = process_soup(soup) 
# quitar atributos inutiles
# prune a las clases


tasks = [ ## output del proceso anterior
    #{"element": {"tag": "div", "attribute": "class", "value": "vipEscortsArea"}, "function_name": "get_escorts_info"},
    {"element": {"tag": "div", "attribute": "class", "value": "a-section a-spacing-large"}, "function_name": "get_amazon"}
]
file_name = "outputs/agent/amazon.py"

string = str(soup.find("div", attrs = {"class": "a-section"}))

print("Num tokens in string: ", num_tokens_from_string(string, "cl100k_base"))
#get_agent_functions(soup, tasks, file_name)
