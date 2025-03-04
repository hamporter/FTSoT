import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

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
driver.get('https://practicesoftwaretesting.com/')

#Looks for element to drag and click it.
source_element = driver.find_element(by=By.XPATH, value="//*[@id='filters']/div[1]/ngx-slider/span[6]")
source_element.click()

#Looks for target element.
target_element = driver.find_element(by=By.XPATH, value="//*[@id='filters']/div[1]/ngx-slider/span[5]")

actions = ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()

 