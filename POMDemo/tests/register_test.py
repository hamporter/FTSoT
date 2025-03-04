from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.register_page import RegisterPage

import time

s = Service('/usr/local/bin/chromedriver')

#Set_some_selenium_chrome_options
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)  #KeepBrowserOpen
chromeOptions.headless = False
driver = webdriver.Chrome(service=s, options=chromeOptions)

def test_register(driver):
    register_page = RegisterPage(driver)
    driver.maximize_window()
    register_page.open_page("https://truqy.fly.dev/login")
    time.sleep(1)  # Allow page to load

    register_page.click_register()
    time.sleep(1)
    register_page.enter_rfc("TEST920521")
    time.sleep(1)
    register_page.enter_reason("TestingTest1")
    time.sleep(1)
    register_page.enter_tel("6141234561")
    time.sleep(1)
    register_page.enter_name("Ham")
    time.sleep(1)
    register_page.enter_lastname("Porter")
    time.sleep(1)
    register_page.enter_email("hamporter1@testmail.com")
    time.sleep(1)
    register_page.enter_password("password")
    time.sleep(1)
    register_page.enter_confirm("password")
    time.sleep(1)
    register_page.click_create()

    time.sleep(6)  # Wait for login to complete
    driver.quit()  # Quit the driver once

test_register(driver)

