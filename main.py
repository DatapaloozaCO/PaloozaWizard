from utils.download import download_html
from utils.build_functions import get_scraper_functions
from utils.build_scraper import get_scraper_code
from bs4 import BeautifulSoup
import constants as ct

file_path = ct.DOWNLOAD_OUTPUT_FOLDER + "oulunlippo.html"

# Download HTML file.
soup: BeautifulSoup = download_html(
    "https://www.oulunlippo.fi/joukkue/",
    save_html = True, 
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

#tasks = [
#    {"element": {"tag": "li", "attribute": "class", "value": "artdeco-list__item"}, "function_name": "get_profile"}
    #{"element": {"tag": "div", "attribute": "class", "value": "s-top-info__right-part"}, "function_name": "get_top"},
#]

#file_name = "test_linkedin.py"
#get_scraper_functions(soup = soup, tasks = tasks, file_name = file_name)
#get_scraper_code(file_name=file_name)
