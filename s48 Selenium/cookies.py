from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = '/Users/vitorbutkusaguiar/Applications/Chrome Driver/chromedriver'

url = 'https://orteil.dashnet.org/experiments/cookie/'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) # prevent browser to close
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(url)

cookie = driver.find_element(By.ID, 'cookie')

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items[:-1]]

timeout = time.time() + 5
five_min = time.time() + 60*5 #5 minutes

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:
        # get all upgrade <b> tags prices
        all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        all_prices_list = [int(item.text.split(' - ')[1].replace(',', '')) for item in all_prices[:-1]]
        # print(all_prices_list)
        # print(item_ids)
        
        # create dict of store items and prices
        cookie_upgrades = {item_id: all_prices_list[index] for index, item_id in enumerate(item_ids)}
        # print(cookie_upgrades)

        # my_cookies now
        my_cookies = driver.find_element(By.ID, 'money').text
        if ',' in my_cookies:
            my_cookies = my_cookies.replace(',', '')
        my_cookies = int(my_cookies)

        #find upgrades that we can currently afford
        affordable_upgrades = {id: cost for id, cost in cookie_upgrades.items() if my_cookies > cost}
        # print(affordable_upgrades)

        #purchase the most expensive upgrade:
        most_expensive = {max(affordable_upgrades, key=lambda k: affordable_upgrades[k]): max(affordable_upgrades.values())}
        # print(most_expensive.)

        most_expensive_div = driver.find_element(By.ID, next(iter(most_expensive)))
        most_expensive_div.click()

        # add 5 sec till the next check
        timeout = time.time() + 5
    
    #after 5 min stop the bot and check cookies/min
    if time.time() > five_min:
        cookies_per_s = driver.find_element(By.ID, 'cps').text
        print(cookies_per_s)
        break
