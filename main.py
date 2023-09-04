from utils.download import download_html
from utils.build_functions import get_scraper_functions
from utils.build_scraper import get_scraper_code
from bs4 import BeautifulSoup
import constants as ct

file_path = ct.DOWNLOAD_OUTPUT_FOLDER + "mercado_libre.html"

# Download HTML file.
soup: BeautifulSoup = download_html(
    "https://articulo.mercadolibre.com.co/MCO-576136391-torre-cpu-gamer-athlon-3000g-vega-3-240sdd-8gb-pc-_JM#reco_item_pos=3&reco_backend=best-seller&reco_backend_type=low_level&reco_client=highlights-rankings&reco_id=8290acbf-a3e7-466a-aa7b-d55ad60ac3d7#trends_tracking_id=14ada507-a06a-4c2f-ac93-4140286e2a79&component_id=BEST_SELLER",
    save_html = False, 
    file_path = file_path
)

with open(file_path, "r") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")

#tasks = [
#    {"element": {"tag": "div", "attribute": "class", "value": "s-list-info__item"}, "function_name": "get_stats"},
#    {"element": {"tag": "div", "attribute": "class", "value": "s-top-info__right-part"}, "function_name": "get_top"},
#]

#soup = soup.find("ol", attrs = {"class": "artdeco-list"})
#soup = soup.find_all("li", attrs = {"class": "artdeco-list__item"})[0:3]
#soup = BeautifulSoup('<br/>'.join([str(tag) for tag in soup]), "html.parser")

tasks = [
    {"element": {"tag": "li", "attribute": "class", "value": "artdeco-list__item"}, "function_name": "get_profile"}
    #{"element": {"tag": "div", "attribute": "class", "value": "s-top-info__right-part"}, "function_name": "get_top"},
]

file_name = "test_linkedin.py"
#get_scraper_functions(soup = soup, tasks = tasks, file_name = file_name)
get_scraper_code(file_name=file_name)
