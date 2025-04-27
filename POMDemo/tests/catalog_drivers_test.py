from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.catalog_drivers_page import CatalogDriversPage
from POMDemo.pages.login_page import LoginPage

import time

s = Service('/usr/local/bin/chromedriver')

#Set_some_selenium_chrome_options
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)  #KeepBrowserOpen
chromeOptions.headless = False
driver = webdriver.Chrome(service=s, options=chromeOptions)

def test_login(driver):
    login_page = LoginPage(driver)
    driver.maximize_window()
    driver.get("https://truqy.fly.dev/login")
    time.sleep(3)  # Allow page to load
    login_page.enter_username('user@email.com')
    time.sleep(1)
    login_page.enter_password('123456')
    time.sleep(1)
    login_page.click_login()
    time.sleep(5)

def test_catalog_drivers(driver):
    drivers_form = CatalogDriversPage(driver)
    drivers_form.click_catalog()
    time.sleep(1)
    drivers_form.click_drivers()
    time.sleep(1)
    drivers_form.click_add_driver()
    time.sleep(1)
    drivers_form.enter_name("Hamilton")
    time.sleep(1)
    drivers_form.enter_lastname("Porter")
    time.sleep(1)
    drivers_form.enter_rfc("HPLC920522SP 9")
    time.sleep(1)
    drivers_form.enter_phone("6143090704")
    time.sleep(1)
    drivers_form.enter_emp_num("333")
    time.sleep(1)
#Country Dropdown.
    drivers_form.click_country()
    time.sleep(1)
    drivers_form.pick_country("México")
    time.sleep(1)
#State Dropdown.
    drivers_form.click_state()
    time.sleep(1)
    drivers_form.pick_state("Aguascalientes")
    time.sleep(1)
#City Dropdown.
    drivers_form.click_city()
    time.sleep(1)
    drivers_form.pick_city("El Llano")
    time.sleep(1)
#-------------
    drivers_form.enter_email("elbambino@hotmail.com")
    time.sleep(1)
    drivers_form.enter_new_password("bestcatcher33")
    time.sleep(1)
    drivers_form.enter_conf_password("bestcatcher33")
    time.sleep(2)
    drivers_form.click_add()
    time.sleep(3)


test_login(driver)  # Call the function
test_catalog_drivers(driver)

driver.quit()
