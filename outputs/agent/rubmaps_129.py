from bs4 import BeautifulSoup

def rubmaps_129(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    options = soup.find_all('option')
    
    data = {}
    for option in options:
        value = option['value']
        text = option.text
        if value and text:
            data[value] = text
    
    return data

