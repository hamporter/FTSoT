from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.clients_page import ClientsPage
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

def test_add_client(driver):
    add_client_page = ClientsPage(driver)
    add_client_page.click_clients()
    time.sleep(2)
    add_client_page.click_add_client()
    time.sleep(2)
    add_client_page.enter_legal_name("Sociedad Tronca")
    time.sleep(2)
    add_client_page.enter_commercial_name("Muebles Troncozo")
    time.sleep(2)
    add_client_page.enter_rfc("LOLS861012P92")
    time.sleep(2)
    add_client_page.enter_email("mueblestroncozo@hotmail.com")
    time.sleep(2)
    add_client_page.enter_phone("6143950582")
    time.sleep(2)
    add_client_page.click_country()
    time.sleep(2)
    add_client_page.pick_country("México")
    time.sleep(2)
    add_client_page.click_state()
    time.sleep(2)
    add_client_page.pick_state("Baja California")
    time.sleep(2)
    add_client_page.click_city()
    time.sleep(2)
    add_client_page.pick_city("Tecate")
    time.sleep(2)
    add_client_page.click_zc()
    time.sleep(2)
    add_client_page.pick_zc("21550")
    time.sleep(2)
    add_client_page.enter_address("Beverly Hills 90210")
    time.sleep(2)
    add_client_page.click_add()
    time.sleep(2)

test_login(driver)  # Call the function
test_add_client(driver)

driver.quit()