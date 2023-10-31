
from bs4 import BeautifulSoup

def function_1(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    data = {}

    # Extracting the text from the paragraphs
    paragraphs = soup.find_all('p')
    data['paragraphs'] = [p.text for p in paragraphs]

    # Extracting the text from the headings
    headings = soup.find_all('h2')
    data['headings'] = [h.text for h in headings]

    # Extracting the text from the list items
    list_items = soup.find_all('li')
    data['list_items'] = [li.text for li in list_items]

    return data


