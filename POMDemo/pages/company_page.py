from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CompanyPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")
        self.company_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[1]/a")
        self.address_textbox = (By.ID, "Address")
        self.submit_button = (By.XPATH, "//*[@id='CompanyMxForm']/div[8]/div/button")
        self.edit_button = (By.XPATH, "//*[@id='CompanyMxForm']/div[8]/div/button")


    def open_page(self, url):
            self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_company(self):
        self.driver.find_element(*self.company_button).click()

    def enter_address(self, address):
        self.driver.find_element(*self.address_textbox).send_keys(address)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def clear_address(self):
        # Wait until the address field is visible
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.address_textbox)
        )

        field.clear()

        # Backup: Use Keys if needed
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.BACKSPACE)

    def click_edit(self):
        self.driver.find_element(*self.edit_button).click()
