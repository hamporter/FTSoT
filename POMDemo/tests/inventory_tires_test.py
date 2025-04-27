from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.inventory_tires_page import InventoryTiresPage
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

def test_tire_inventory(driver):
    test_tire_form = InventoryTiresPage(driver)
    test_tire_form.click_inventory()
    time.sleep(2)
    test_tire_form.click_tires()
    time.sleep(1)
    test_tire_form.click_add_tire()
    time.sleep(1)
    test_tire_form.click_brand()
    time.sleep(1)
    test_tire_form.pick_brand("Michelin")
    time.sleep(1)
    test_tire_form.enter_model("33")
    time.sleep(1)
    test_tire_form.enter_part_no("333")
    time.sleep(1)
    test_tire_form.enter_width("35")
    time.sleep(1)
    test_tire_form.enter_height("36")
    time.sleep(1)
    test_tire_form.enter_depth("250")
    time.sleep(1)
    test_tire_form.click_app()
    time.sleep(2)
    test_tire_form.pick_app("Mixto")
    time.sleep(1)
    test_tire_form.enter_rim("40")
    time.sleep(1)
    test_tire_form.enter_weight("2500")
    time.sleep(1)
    test_tire_form.enter_type("si")
    time.sleep(1)
    test_tire_form.enter_range("333")
    time.sleep(1)
    test_tire_form.click_add()
    time.sleep(4)


test_login(driver)  # Call the function
test_tire_inventory(driver)

driver.quit()