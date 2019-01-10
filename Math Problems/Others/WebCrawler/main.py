import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://bikroy.com/bn/ads/dhaka?page=2' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text

