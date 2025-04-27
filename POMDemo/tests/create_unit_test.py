from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.create_unit_page import CreateUnitPage
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

def test_create_unit(driver):
    create_form = CreateUnitPage(driver)
    create_form.click_create()
    time.sleep(1)
    create_form.enter_name('Test Unit')
    time.sleep(1)
    create_form.enter_rfc('test930711')
    time.sleep(1)
    create_form.enter_phone('6143590738')
    time.sleep(3)
    create_form.click_country()
    time.sleep(2)
    create_form.select_country('USA')
    time.sleep(2)
    create_form.select_state('Alaska')
    time.sleep(2)
    create_form.select_city('Hoonah')
    time.sleep(2)
    create_form.select_zc('99829')
    time.sleep(2)
    create_form.enter_responsible('Test User Resp')
    time.sleep(2)
    create_form.enter_address('Test Dr.')
    time.sleep(2)
    create_form.select_type('US')
    time.sleep(2)
    create_form.select_unitType('BINACIONAL')
    time.sleep(2)
    create_form.click_create()
    time.sleep(5)
    driver.quit()

test_login(driver)  # Call the function
test_create_unit(driver)