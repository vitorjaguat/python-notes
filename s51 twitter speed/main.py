from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USER = os.environ.get('TW_1')
TWITTER_PW = os.environ.get('TW_2')

chrome_driver_path = '/Users/vitorbutkusaguiar/Applications/Chrome Driver/chromedriver'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) # prevent browser to close


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.pw = os.environ.get('TW_2')
        # self.pw = ''
        self.tweet_message = ''

    def has_digits(self, inputString):
        """check if the selector's text has digits"""
        return any(char.isdigit() and char != '0' for char in inputString)

    def get_internet_speed(self):
        # self.driver.get('https://www.speedtest.net/')
        self.driver.get('https://www.brasilbandalarga.com.br/')
        time.sleep(3)
         # Depending on your location, you might need to accept the GDPR pop-up.
        accept_button = self.driver.find_element(By.XPATH, '//*[@id="card0"]/div/div[2]/button[2]')
        accept_button.click()
        go_button = self.driver.find_element(By.ID, 'btnIniciar')
        go_button.click()
        result_down = str('')
        result_up = str('')
        time.sleep(60)
        # while not self.has_digits(result_down) or not self.has_digits(result_up):
        result_down = self.driver.find_element(By.XPATH, '//*[@id="medicao"]/div/div[2]/div[1]/div/div[1]/div[2]').text
        result_up = self.driver.find_element(By.XPATH, '//*[@id="medicao"]/div/div[2]/div[1]/div/div[2]/div[2]').text 
        
        print(result_down)
        print(result_up)

        if float(result_down) < float(PROMISED_DOWN):
            self.tweet_message = f'Dona @ClaroBrasil, por que minha velocidade de download está em {result_down} se eu paguei por {PROMISED_DOWN}???'
            self.tweet_at_provider(self.tweet_message)
        



    def tweet_at_provider(self, message):
        self.driver.get('https://www.twitter.com')
        time.sleep(10)
        username_input = self.driver.find_element(By.NAME, 'text')
        username_input.send_keys('uintstudio')
        username_input.send_keys(Keys.ENTER)
        time.sleep(5)
        pw_input = self.driver.find_element(By.NAME, 'password')
        pw_input.send_keys(self.pw)

        pw_input.send_keys(Keys.ENTER)
        time.sleep(5)
        draft_input = self.driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        draft_input.send_keys(message)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span')
        tweet_btn.click()
        time.sleep(3)



speed_bot = InternetSpeedTwitterBot(chrome_driver_path=chrome_driver_path)
speed_bot.get_internet_speed()




