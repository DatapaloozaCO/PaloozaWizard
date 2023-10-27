from bs4 import BeautifulSoup

def oulunlippo_23_html(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    menu_items = soup.find_all('li', class_='menu-item')
    
    data = {}
    for item in menu_items:
        menu_id = item.get('id')
        menu_title = item.find('a').get('title')
        menu_link = item.find('a').get('href')
        data[menu_id] = {'title': menu_title, 'link': menu_link}
    
    return data

