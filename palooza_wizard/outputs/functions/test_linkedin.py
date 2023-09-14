
from bs4 import BeautifulSoup

def get_profile(html):
    soup = BeautifulSoup(html, 'html.parser')
    profile = {}
    profile['name'] = soup.find('span', {'data-anonymize': 'person-name'}).text
    profile['title'] = soup.find('span', {'data-anonymize': 'title'}).text
    profile['company'] = soup.find('a', {'data-anonymize': 'company-name'}).text.strip()
    profile['location'] = soup.find('span', {'data-anonymize': 'location'}).text
    profile['job_duration'] = soup.find('div', {'data-anonymize': 'job-title'}).text.strip()
    profile['image_url'] = soup.find('img', {'data-anonymize': 'headshot-photo'})['src']
    return profile


