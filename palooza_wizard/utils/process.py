from bs4 import BeautifulSoup


def process_soup(soup: BeautifulSoup) -> BeautifulSoup:
    """Select HTML body and remove all script tags"""
    soup = soup.find("body")
    for s in soup.select("script"):
        s.extract()
    return soup
