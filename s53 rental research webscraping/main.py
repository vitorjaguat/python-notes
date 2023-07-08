from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_driver_path = '/Users/vitorbutkusaguiar/Applications/Chrome Driver/chromedriver'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) # prevent browser to close

WEBSITE_5ANDAR = 'https://www.quintoandar.com.br/'
FORM_URL = 'https://forms.gle/oyJUgJSbmsiX4Ht8A'



class RentalResearch:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))

    def search_properties(self):
        self.driver.get(WEBSITE_5ANDAR)
        time.sleep(3)
        accept_cookies_btn = self.driver.find_element(By.ID, 'qa-cookie-banner-button')
        accept_cookies_btn.click()
        input_city = self.driver.find_element(By.NAME, 'landing-city-input')
        input_city.send_keys('Rio de Janeiro')
        input_bairro = self.driver.find_element(By.NAME, 'landing-neighborhood-input')
        input_bairro.send_keys('Botafogo')
        time.sleep(3)
        # input_valor = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[2]/div/form/div[4]/div[1]/svg')
        # input_valor.click()
        # input_5000 = self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="5000"]')
        # input_5000.click()
        btn_submit = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[2]/div/form/button')
        btn_submit.click()
        time.sleep(3)
        btn_pular = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/button/span/span')
        btn_pular.click()
        time.sleep(3)

        addresses_tags = self.driver.find_elements(By.CSS_SELECTOR, 'span[data-testid="house-card-address"]')
        addresses_list = [tag.text for tag in addresses_tags]
        print(addresses_list)
        prices_tags = self.driver.find_elements(By.XPATH, "//*[starts-with(normalize-space(text()), 'Total')]")
        prices_list = [tag.text.replace('Total', '') for tag in prices_tags]
        print(prices_list)
        links_tags = self.driver.find_elements(By.CSS_SELECTOR, ".sc-isijxy-0.guYZVu")
        links_list = [tag.get_attribute('href') for tag in links_tags]
        print(links_list)
        data = []
        for n in range(len(links_list)):
            data.append({
                "address": addresses_list[n],
                "price": prices_list[n],
                "link": links_list[n]
            })
        print(data)
        self.fill_form(data)

        # self.fill_form(addresses_list)
    
    def fill_form(self, data):
        self.driver.get(FORM_URL)
        time.sleep(3)
        for item in data:
            # input_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # input_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # input_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
            inputs_list = [tag for tag in inputs]
            # print(inputs_list)
            inputs_list[0].send_keys(item["address"])
            inputs_list[1].send_keys(item["price"])
            inputs_list[2].send_keys(item["link"])
            btn_submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            btn_submit.click()
            self.driver.get(FORM_URL)
            time.sleep(3)

        




rental_research = RentalResearch()
rental_research.search_properties()