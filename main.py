import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

service = Service('./../chromedriver')

service.start()

driver = webdriver.Remote(service.service_url)

###google search automation####

driver.get('http://www.google.com/');
driver.implicitly_wait(10)
search_box = element = driver.find_element(By.NAME, "q")

search_box.send_keys("T")
time.sleep(5)

search_box.send_keys(Keys.RETURN)
time.sleep(5)
element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("Twitter")
element.submit()

time.sleep(10)

driver.quit()

####Consent button click ####

# driver.get('https://www.geeksforgeeks.org/data-structures/');
# driver.implicitly_wait(10)
# driver.find_element(By.CLASS_NAME, "consent-btn").click()
# time.sleep(5)
# driver.quit()

### instagram login automation ###

# config = dotenv_values(".env")
# element=driver.get("https://www.instagram.com/?hl=en")
# driver.implicitly_wait(10)
# username = driver.find_element(By.NAME, "username")
# username.send_keys(config.get("USRNAME"))
# password = driver.find_element(By.NAME, "password")
# password.send_keys(dotenv_values('.env')['PASSWORD'])
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(10)
# driver.quit()
