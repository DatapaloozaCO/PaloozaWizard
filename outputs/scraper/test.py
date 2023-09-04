class Scraper:
    def __init__(self):
        pass

    def get_stats(self, soup):
        data = {}
        divs = soup.find_all('div', class_='s-list-info__item')
        for div in divs:
            label = div.find('div', class_='s-list-info__label').text.strip()
            value = div.find('div', class_='s-list-info__value').text.strip()
            data[label] = value
        return data

    def get_top(self, soup):
        data = {}

        # Extract reliability
        reliability = soup.find('div', class_='s-indicators__item-wrapper s-indicators__item-wrapper_risk').get_text(strip=True)
        data['Reliability'] = reliability

        # Extract weeks
        weeks = soup.find('span', class_='s-indicators__item-desc s-indicators__item-desc_weeks').get_text(strip=True)
        data['Weeks'] = weeks

        # Extract number of active subscriptions
        subscriptions = soup.find('span', class_='s-subscribers-icon__count').get_text(strip=True)
        data['Subscriptions'] = subscriptions

        # Extract total funds
        funds = soup.find('div', class_='s-indicators__item-wrapper s-indicators__item-wrapper_subscribers').find_all('div')[1].get_text(strip=True)
        data['Funds'] = funds

        return data

    def extract_data(self, soup, url):
        data = {}
        data['Stats'] = self.get_stats(soup)
        data['Top'] = self.get_top(soup)
        return data