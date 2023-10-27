from bs4 import BeautifulSoup

def rubmaps_21_html(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    select_tag = soup.find('select', {'name': 'state'})
    options = select_tag.find_all('option')
    
    data = {}
    for option in options:
        value = option['value']
        state = option.text
        data[value] = state
    
    return data

