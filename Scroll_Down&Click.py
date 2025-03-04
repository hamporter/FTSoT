import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#Set_location_of_Chrome_Driver
s = Service('/usr/local/bin/chromedriver')

#Set_some_selenium_chrome_options
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True) #KeepBrowserOpen
chromeOptions.headless = True
driver = webdriver.Chrome(service=s, options=chromeOptions)


#Opens browser and maximizes window.
driver.maximize_window()
driver.get('https://automationpanda.com/')

#Scroll down two times.
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

#Looks for XPATH and click it.
#folder = driver.find_element(by=By.XPATH, value="//*[@id='post-20333']/footer/a[4]")
folder = driver.find_element(by=By.XPATH, value="//*[@id='post-20333']/div/p[3]/a")
folder.click()
