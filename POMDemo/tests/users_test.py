from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from POMDemo.pages.users_page import UsersPage
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

def test_create_user(driver):
    users_form = UsersPage(driver)
    users_form.click_users()
    time.sleep(2)
    users_form.click_create_user()
    time.sleep(2)
    users_form.enter_name("Hamilton")
    time.sleep(2)
    users_form.enter_last_name("Porter")
    time.sleep(2)
    users_form.enter_email("hp@test.com")
    time.sleep(2)
    users_form.enter_new_password("123456")
    time.sleep(2)
    users_form.enter_new_password_confirm("123456")
    time.sleep(2)
    users_form.click_role()
    time.sleep(2)
    users_form.pick_role("Client")
    time.sleep(2)
    users_form.click_add()
    time.sleep(2)

test_login(driver)  # Call the function
test_create_user(driver)

driver.quit()