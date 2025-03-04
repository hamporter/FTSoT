from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from POMDemo.pages.company_page import CompanyPage
import time


s = Service('/usr/local/bin/chromedriver')

#Set_some_selenium_chrome_options
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)  #KeepBrowserOpen
chromeOptions.headless = False
driver = webdriver.Chrome(service=s, options=chromeOptions)

def test_company(driver):
    company_page = CompanyPage(driver)
    driver.maximize_window()
    driver.get("https://truqy.fly.dev/login")
    time.sleep(1)  # Allow page to load
    company_page.enter_username('user@email.com')
    company_page.enter_password('123456')
    company_page.click_login()
    time.sleep(5)
    company_page.click_company()
    company_page.clear_address()
    time.sleep(3)
    company_page.enter_address('Test St.')
    company_page.click_edit()

    time.sleep(6)  # Wait for login to complete
    driver.quit()  # Quit the driver once


test_company(driver)  # Call the function