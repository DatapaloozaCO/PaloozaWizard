#from outputs.scraper.test_linkedin import Scraper
from bs4 import BeautifulSoup
import constants as ct

file_path = ct.DOWNLOAD_OUTPUT_FOLDER + "linkedin_search_page_0.html"
with open(file_path, "r") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
soup = soup.find("li", attrs = {"class": "artdeco-list__item"})

#scraper = Scraper()
#res = scraper.extract_data(soup.find("li", attrs = {"class": "artdeco-list__item"}), url = None)
def get_profile(soup):
    profile = {}
    profile['name'] = soup.find('span', {'data-anonymize': 'person-name'}).text
    profile['title'] = soup.find('span', {'data-anonymize': 'title'}).text
    profile['company'] = soup.find('a', {'data-anonymize': 'company-name'}).text.strip()
    profile['location'] = soup.find('span', {'data-anonymize': 'location'}).text
    profile['job_duration'] = soup.find('div', {'data-anonymize': 'job-title'}).text.strip()
    profile['image_url'] = soup.find('img', {'data-anonymize': 'headshot-photo'})['src']
    return profile

profile = get_profile(soup)


import json 
with open("result.json", "w") as f:
    f.write(json.dumps(profile))