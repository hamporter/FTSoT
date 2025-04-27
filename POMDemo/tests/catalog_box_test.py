from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.catalog_box_page import CatalogBoxPage
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

def test_catalog_box(driver):
    box_catalog_form = CatalogBoxPage(driver)
    box_catalog_form.click_catalog()
    time.sleep(2)
    box_catalog_form.click_boxes()
    time.sleep(1)
    box_catalog_form.click_add_box()
    time.sleep(1)
    box_catalog_form.enter_e_number("123456789")
    time.sleep(1)
    box_catalog_form.enter_vin("00000000000000003")
    time.sleep(1)
    box_catalog_form.click_box_kind()
    time.sleep(2)
    box_catalog_form.pick_box_kind("Power only")
    time.sleep(2)
    box_catalog_form.click_brand()
    time.sleep(1)
    box_catalog_form.pick_brand("International")
    time.sleep(1)
    box_catalog_form.click_year()
    time.sleep(1)
    box_catalog_form.pick_year("1992")
    time.sleep(1)
    box_catalog_form.enter_radio("33")
    time.sleep(2)
    box_catalog_form.enter_min_weight("1500")
    time.sleep(1)
    box_catalog_form.enter_max_weight("3500")
    time.sleep(1)
    box_catalog_form.click_tire_kind()
    time.sleep(1)
    box_catalog_form.pick_tire_kind("Traccion")
    time.sleep(1)
    box_catalog_form.enter_tire_size("35")
    time.sleep(1)
    box_catalog_form.enter_rim("34")
    time.sleep(1)
    box_catalog_form.enter_date("22-05-2024")
    time.sleep(2)
    box_catalog_form.click_refri()
    time.sleep(1)
    box_catalog_form.enter_price("1500000")
    time.sleep(2)
    box_catalog_form.click_mxus()
    time.sleep(1)
    box_catalog_form.pick_mxus("MX")
    time.sleep(2)
    box_catalog_form.click_add()
    time.sleep(1)


test_login(driver)  # Call the function
test_catalog_box(driver)

driver.quit()