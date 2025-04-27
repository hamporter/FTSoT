from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.login_page import LoginPage
from POMDemo.pages.rute_page import RutePage

import time

# Set up Selenium WebDriver
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

def test_create_rute(driver):
    create_form = RutePage(driver)
    create_form.click_routes()
    time.sleep(2)
    create_form.click_create_route()
    time.sleep(1)
    create_form.enter_rute_name('Test Rute')
    time.sleep(1)
    create_form.enter_millage('33')
    time.sleep(1)
    create_form.enter_avgTime('9')
    time.sleep(1)

    # Select Origin
    create_form.click_origin()
    time.sleep(1)
    create_form.select_country('USA')
    time.sleep(1)
    create_form.select_state('Alaska')
    time.sleep(1)
    create_form.select_city('Hoonah')
    time.sleep(4)

    # Select Destination
    create_form.click_destination()
    time.sleep(2)
    create_form.select_country('Mexico', is_destination=True)
    time.sleep(1)
    create_form.select_state('Aguascalientes', is_destination=True)
    time.sleep(1)
    create_form.select_city('El Llano', is_destination=True)
    time.sleep(3)

    create_form.click_add()
    time.sleep(2)


test_login(driver)  # Call the function
test_create_rute(driver)

driver.quit()


