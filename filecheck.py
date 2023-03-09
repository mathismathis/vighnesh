from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.google.com/')

time.sleep(10)
print('hi')