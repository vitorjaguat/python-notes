from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/vitorbutkusaguiar/Applications/Chrome Driver/chromedriver'

url = 'https://www.amazon.com.br/BISCOITOS-SORTIDOS-MATILDE-VICENZI-MINIVOGLIE/dp/B00J7OD142/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=NGV4N59A14UM&keywords=matilde+vicenzi&qid=1688679024&sprefix=matilde+vicenz%2Caps%2C1365&sr=8-2&ufe=app_do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d'
url = 'https://www.python.org/'

driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get(url)

# price = driver.find_element(By.CSS_SELECTOR, '.a-price .a-price-whole')
# price_cents = driver.find_element(By.CSS_SELECTOR, '.a-price .a-price-fraction')
# print(f'{price.text},{price_cents.text}')

events_years = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li time span')
events_years_list = [el.text for el in events_years]
events_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li time')
events_dates_list = [el.text for el in events_dates]
print(events_dates_list)

events_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li a')
events_names_list = [el.text for el in events_names]
print(events_names_list)

events_dict = {events_names_list.index(event):{"name": event, "date": events_dates_list[events_names_list.index(event)]} for event in events_names_list}
events_dict = {index: {"name": event, "date": events_dates_list[index]} for index, event in  enumerate(events_names_list)} # enumerate return an indexed list [(0, val0), (1, val1), etc]
print(events_dict)



driver.close()