import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page <= max_pages:
       url = 'https://pgcb.org.bd/PGCB/?a=pages/hourly_generation_loadshed_display.php&page=' + str(page)
       source_code = requests.get(url)
       plain_text = source_code.text
       soup = BeautifulSoup(plain_text, "html.parser")
       table = soup.find('table', {'class':'layout display responsive-table'})
       for data in table.findAll('td'):
           print(data.string)

spider(1)#ekhane page number dilei hobe maximum, empty rakhle shb page theke download hbe
         #line break and comma add korte hbe
