class Scraper:
    def __init__(self):
        pass

    def get_players(self, soup):
        players = soup.find_all('div', class_='pelaaja')
        players_data = {}
        for player in players:
            name = player.find('h3').text
            img_url = player.find('img')['data-src']
            players_data[name] = img_url
        return players_data

    def extract_data(self, soup, url):
        data = {
            'players': self.get_players(soup),
            'url': url
        }
        return data