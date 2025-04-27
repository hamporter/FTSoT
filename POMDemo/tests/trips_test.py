from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.trips_page import TripsPage
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

def test_trips(driver):
    trips_page = TripsPage(driver)
    trips_page.click_trips()
    time.sleep(1)
    trips_page.click_add_trip()
    time.sleep(1)
    trips_page.click_client()
    time.sleep(2)
    trips_page.pick_client("Sociedad Tronca")
    time.sleep(1)
    trips_page.click_route()
    time.sleep(1)
    trips_page.pick_route("TEST")
    time.sleep(1)
    trips_page.enter_start("22-05-2025, 12-59")
    time.sleep(1)
    trips_page.enter_end("25-09-2025, 6-33")
    time.sleep(1)
    trips_page.click_service()
    time.sleep(1)
    trips_page.pick_service("Exportacion")
    time.sleep(1)
    trips_page.click_vehicle()
    time.sleep(1)
    trips_page.pick_vehicle("Vehículo")
    time.sleep(1)
    trips_page.click_add()
    time.sleep(3)

test_login(driver)
test_trips(driver)

driver.quit()


CV