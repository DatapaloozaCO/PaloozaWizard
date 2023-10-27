from bs4 import BeautifulSoup

def rubmaps_106(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    data = {}
    ul = soup.find('ul', class_='left_other_amps')
    if ul:
        li_list = ul.find_all('li')
        for li in li_list:
            a = li.find('a')
            if a:
                data[a.text] = a['href']
    return data

