import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

#Set_location_of_Chrome_Driver
s = Service('/usr/local/bin/chromedriver')

#Set_some_selenium_chrome_options
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True) #KeepBrowserOpen
chromeOptions.headless = True
driver = webdriver.Chrome(service=s, options=chromeOptions)

#Opens browser and maximizes window.
driver.maximize_window()
driver.get('https://practicesoftwaretesting.com/')
time.sleep(2)

find_category = \
driver.find_element(by=By.CSS_SELECTOR, value="nav-link dropdown-toggle show")
find_category = Select(find_category)
find_category.select_by_visible_text("Other")
time.sleep(2)

