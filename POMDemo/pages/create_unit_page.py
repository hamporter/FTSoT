from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

#Log In.
    def open_page(self, url):
            self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


class CreateUnitPage:

    def __init__(self,driver):
        self.driver = driver
        self.create_button = (By.XPATH, "//*[@id='root']/div/div/main/div[2]/div/div/div/div/div/div[1]/button")
        self.name_textbox = (By.ID, "name")
        self.rfc_textbox = (By.ID, "rfc")
        self.phone_textbox = (By.ID, "phone")
        self.country_dropdown = (By.ID, "Country")
        self.select_dropdown = (By.TAG_NAME, "USA")
        self.state_dropdown = (By.ID, "State")
        self.select_dropdown2 = (By.TAG_NAME, "Alaska")
        self.city_dropdown = (By.ID, "City")
        self.select_dropdown3 = (By.TAG_NAME, "Hoonah")
        self.zc_dropdown = (By.ID, "ZipCodeID")
        self.select_dropdown4 = (By.TAG_NAME, "99829")
        self.responsible_textbox = (By.ID, "responsable")
        self.address_textbox = (By.ID, "address")
        self.type_dropdown = (By.ID, "typeCompany")
        self.select_dropdown5 = (By.TAG_NAME, "US")
        self.unitType_dropdown = (By.ID, "type")
        self.select_dropdown6 = (By.TAG_NAME, "BINACIONAL")
        self.add_button = (By.XPATH, "//*[@id='ModalBU']/div/div[3]/button[1]")

#Click and fill form.
    def click_create(self):
        self.driver.find_element(*self.create_button).click()

    def enter_name(self, name):
        self.driver.find_element(*self.name_textbox).send_keys(name)

    def enter_rfc(self, rfc):
        self.driver.find_element(*self.rfc_textbox).send_keys(rfc)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def click_country(self):
        self.driver.find_element(*self.country_dropdown).click()

    def select_country(self, country_name):
        dropdown = Select(self.driver.find_element(*self.country_dropdown))
        dropdown.select_by_visible_text(country_name)
        self.driver.find_element(*self.country_dropdown).send_keys(Keys.RETURN)

    def click_state(self):
        self.driver.find_element(*self.state_dropdown).click()

    def select_state(self, state_name):
        dropdown2 = Select(self.driver.find_element(*self.state_dropdown))
        dropdown2.select_by_visible_text(state_name)
        self.driver.find_element(*self.state_dropdown).send_keys(Keys.RETURN)

    def click_city(self):
        self.driver.find_element(*self.city_dropdown).click()

    def select_city(self, city_name):
        dropdown3 = Select(self.driver.find_element(*self.city_dropdown))
        dropdown3.select_by_visible_text(city_name)
        self.driver.find_element(*self.city_dropdown).send_keys(Keys.RETURN)

    def click_zc(self):
        self.driver.find_element(*self.zc_dropdown).click()

    def select_zc(self, zc_name):
        dropdown4 = Select(self.driver.find_element(*self.zc_dropdown))
        dropdown4.select_by_visible_text(zc_name)
        self.driver.find_element(*self.zc_dropdown).send_keys(Keys.RETURN)

    def enter_responsible(self, responsible):
        self.driver.find_element(*self.responsible_textbox).send_keys(responsible)

    def enter_address(self, address):
        self.driver.find_element(*self.address_textbox).send_keys(address)

    def click_type(self):
        self.driver.find_element(*self.type_dropdown).click()

    def select_type(self, type_name):
        dropdown5 = Select(self.driver.find_element(*self.type_dropdown))
        dropdown5.select_by_visible_text(type_name)
        self.driver.find_element(*self.type_dropdown).send_keys(Keys.RETURN)

    def click_unitType(self):
        self.driver.find_element(*self.unitType_dropdown).click()

    def select_unitType(self, unitType_name):
        dropdown6 = Select(self.driver.find_element(*self.unitType_dropdown))
        dropdown6.select_by_visible_text(unitType_name)
        self.driver.find_element(*self.unitType_dropdown).send_keys(Keys.RETURN)

    def click_add(self):
        self.driver.find_element(*self.add_button).click()