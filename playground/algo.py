from bs4 import BeautifulSoup
import networkx as nx
import requests

def get_soup(url: str) -> BeautifulSoup:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f'Error: No se pudo descargar la página. Código de estado: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

def get_toy_graph():
    url = 'https://www.citytourgirls.com/'
    soup = get_soup(url)