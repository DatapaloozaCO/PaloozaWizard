
from bs4 import BeautifulSoup

def get_amazon(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    data = {}

    # Extract product title
    title = soup.find("span", {"id":'productTitle'})
    if title:
        data['title'] = title.string.strip()

    # Extract product price
    price = soup.find("span", {'class':'a-offscreen'})
    if price:
        data['price'] = price.string.strip()

    # Extract product rating
    rating = soup.find("span", {'class':'a-icon-alt'})
    if rating:
        data['rating'] = rating.string.strip()

    # Extract number of product reviews
    reviews = soup.find("span", {'id':'acrCustomerReviewText'})
    if reviews:
        data['reviews'] = reviews.string.strip()

    return data


