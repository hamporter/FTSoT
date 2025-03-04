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



#Abre browser y maximiza ventana.
driver.maximize_window()
driver.get('https://automationpanda.com/')

folder = driver.find_element(by=By.ID, value='menu-item-9')
folder.click()


