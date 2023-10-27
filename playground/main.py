from bs4 import BeautifulSoup
import palooza_wizard.constants as ct
import os
from palooza_wizard.utils.files import 

file_path = "./oulunlippo.html"
file_name = "./oulunlippo.py"

if not os.path.isfile(file_path):
    soup: BeautifulSoup = download_html(
        "https://www.oulunlippo.fi/joukkue/",
        save_html = True, 
        file_path = file_path
    )

soup = load_html(file_path)
tasks = [
    {
        "element": {"tag": "section", "attribute": "class", "value": "pelaajat"},
        "function_name": "get_players", 
        "function_description": ""
    }
]
#get_scraper_functions(soup = soup, tasks = tasks, file_name = file_name)
get_scraper_code(file_name=file_name)




#tasks = [
#    {"element": {"tag": "div", "attribute": "class", "value": "s-list-info__item"}, "function_name": "get_stats"},
#    {"element": {"tag": "div", "attribute": "class", "value": "s-top-info__right-part"}, "function_name": "get_top"},
#]

#soup = soup.find("ol", attrs = {"class": "artdeco-list"})
#soup = soup.find_all("li", attrs = {"class": "artdeco-list__item"})[0:3]
#soup = BeautifulSoup('<br/>'.join([str(tag) for tag in soup]), "html.parser")

#tasks = [
#    {"element": {"tag": "li", "attribute": "class", "value": "artdeco-list__item"}, "function_name": "get_profile"}
    #{"element": {"tag": "div", "attribute": "class", "value": "s-top-info__right-part"}, "function_name": "get_top"},
#]

#file_name = "test_linkedin.py"
#get_scraper_functions(soup = soup, tasks = tasks, file_name = file_name)
#get_scraper_code(file_name=file_name)
