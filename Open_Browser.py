import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

print(time.time())
s = Service('/usr/local/bin/chromedriver')

chromeOptions = Options()
chromeOptions.headless = True

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(service=s, options=chromeOptions)

driver.get('https://www.google.com')
time.sleep(1)
