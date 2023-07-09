from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/vitorbutkusaguiar/Applications/Chrome Driver/chromedriver'

# url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'
url = 'http://secure-retreat-92358.herokuapp.com/'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) # prevent browser to close
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.get(url)

# # find element by XPATH
# expath_articles = '//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/b[1]'
# articles = driver.find_element(By.XPATH, expath_articles).text
# print(articles)

# # find element by link text (and click it)
# all_portals = driver.find_element(By.LINK_TEXT, 'Biografias')
# all_portals.click()

# # find element by name (input)
# search_input = driver.find_element(By.NAME, 'search')
# search_input.send_keys('Python')
# search_input.send_keys(Keys.ENTER)

# login 
firstname_input = driver.find_element(By.NAME, 'fName')
firstname_input.send_keys('Vitor')
lastname_input = driver.find_element(By.NAME, 'lName')
lastname_input.send_keys('Butkus')
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('jaguattt@gamil.com')
button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()




# driver.close()