from bs4 import BeautifulSoup

def oulunlippo_3_html(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    
    data = {}
    
    menu_items = soup.find_all('li', class_='menu-item')
    for item in menu_items:
        link = item.find('a')['href']
        data[item['id']] = link
    
    return data

