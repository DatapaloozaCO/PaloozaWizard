
from bs4 import BeautifulSoup

def function_2(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    data = {}
    articles = soup.find_all('li', class_='mkb-widget-content-tree__article')
    for article in articles:
        title = article.find('span', class_='mkb-widget-content-tree__article-title').text.strip()
        link = article.find('a')['href']
        data[title] = link
    return data


