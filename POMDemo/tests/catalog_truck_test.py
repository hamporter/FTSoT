from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from POMDemo.pages.catalog_truck_page import CatalogTruckPage
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

def test_catalog_truck(driver):
    catalog_form = CatalogTruckPage(driver)
    catalog_form.click_catalog()
    time.sleep(2)
    catalog_form.click_trucks()
    time.sleep(2)
    catalog_form.click_add_truck()
    time.sleep(2)
    catalog_form.enter_e_number("123456789")
    time.sleep(2)
    catalog_form.enter_vin("1234567890987654")
    time.sleep(2)
    catalog_form.click_kind()
    time.sleep(1)
    catalog_form.pick_kind("Motocicleta")
    time.sleep(1)
    catalog_form.click_brand()
    time.sleep(1)
    catalog_form.pick_brand("Audi")
    time.sleep(1)
    catalog_form.click_model()
    time.sleep(1)
    catalog_form.pick_model("BMW")
    time.sleep(1)
    catalog_form.click_year()
    time.sleep(1)
    catalog_form.pick_year("2020")
    time.sleep(1)
    catalog_form.enter_tank_size("333")
    time.sleep(1)
    catalog_form.enter_weight("1500")
    time.sleep(1)
    catalog_form.enter_weight2("2500")
    time.sleep(1)
    catalog_form.click_fuel()
    time.sleep(1)
    catalog_form.pick_fuel("Diesel")
    time.sleep(1)
    catalog_form.enter_radio("33")
    time.sleep(1)
    catalog_form.enter_tire_size("55")
    time.sleep(1)
    catalog_form.enter_tire_qty("8")
    time.sleep(1)
    catalog_form.enter_date("22-5-1992")
    time.sleep(1)
    catalog_form.enter_price("1000000")
    time.sleep(1)
    catalog_form.enter_motor("1")
    time.sleep(1)
    catalog_form.enter_odometer("13")
    time.sleep(1)
    catalog_form.click_nation()
    time.sleep(1)
    catalog_form.pick_nation("BINACIONAL")
    time.sleep(1)
    catalog_form.click_transmission()
    time.sleep(1)
    catalog_form.pick_transmission("Estándar")
    time.sleep(1)
    catalog_form.click_hazmat()
    time.sleep(1)
    catalog_form.click_add()
    time.sleep(4)

test_login(driver)  # Call the function
test_catalog_truck(driver)

driver.quit()

