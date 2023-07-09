from bs4 import BeautifulSoup
import requests


product_url = 'https://www.amazon.com.br/BISCOITOS-SORTIDOS-MATILDE-VICENZI-MINIVOGLIE/dp/B00J7OD142/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=NGV4N59A14UM&keywords=matilde+vicenzi&qid=1688679024&sprefix=matilde+vicenz%2Caps%2C1365&sr=8-2&ufe=app_do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

response = requests.get(product_url, headers=headers)
product_webpage = response.text
print(product_webpage)