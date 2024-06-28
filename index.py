from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X ' + 
                         '10_10_1) AppleWebKit/537.36 (KHTML, like ' + 
                         'Gecko) Chrome/39.0.2171.95 Safari/537.36'}


page = requests.get('https://www.citilink.ru/product/' + 
                    'po-kaspersky-kis-ru-2-dvc-1y-bs' + 
                    '-box-kl1939rbbfs-1402775/',
                    headers=headers)

soup = BeautifulSoup(page.text, "html.parser")

print(soup.findAll('span',
                   class_='ProductPagePriceSection__' + 
                   'default-price_current-price')[0].text.strip())
