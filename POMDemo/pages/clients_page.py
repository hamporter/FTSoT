from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

class ClientsPage:
    def __init__(self,driver):
        self.driver = driver
        self.clients_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[5]/a")
        self.add_client = (By.ID, "addUser")
        self.legal_name_textfield= (By.ID, "legalName")
        self.commercial_name_textfield = (By.ID, "tradename")
        self.email_textfield = (By.ID, "email")
        self.rfc_textfield = (By.ID, "rfc")
        self.telephone_textfield = (By.ID, "telephone")
        self.country_dropdown = (By.ID, "Country")
        self.select_country = (By.TAG_NAME, "México")
        self.state_dropdown = (By.ID, "State")
        self.select_state = (By.TAG_NAME, "Baja California")
        self.city_dropdown = (By.ID, "City")
        self.select_city = (By.TAG_NAME, "Tecate")
        self.zc_dropdown = (By.ID, "ZipCodeID")
        self.select_zc = (By.TAG_NAME, "21550")
        self.address_textfield = (By.ID, "address")
        self.add_button = (By.XPATH, "//*[@id='ModalCL']/div/div[3]/button[1]")


#Log In.
    def open_page(self, url):
            self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


#Clients Form.
    def click_clients(self):
        self.driver.find_element(*self.clients_button).click()

    def click_add_client(self):
        self.driver.find_element(*self.add_client).click()

    def enter_legal_name(self, legal_name):
        self.driver.find_element(*self.legal_name_textfield).send_keys(legal_name)

    def enter_commercial_name(self, commercial_name):
        self.driver.find_element(*self.commercial_name_textfield).send_keys(commercial_name)

    def enter_rfc(self, rfc):
        self.driver.find_element(*self.rfc_textfield).send_keys(rfc)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textfield).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.telephone_textfield).send_keys(phone)

# Country Dropdown.
    def click_country(self):
        self.driver.find_element(*self.country_dropdown).click()

    def pick_country(self, country):
        dropdown = Select(self.driver.find_element(*self.country_dropdown))
        dropdown.select_by_visible_text(country)
        self.driver.find_element(*self.country_dropdown).click()

#State Dropdown.
    def click_state(self):
        self.driver.find_element(*self.state_dropdown).click()

    def pick_state(self, state):
        dropdown = Select(self.driver.find_element(*self.state_dropdown))
        dropdown.select_by_visible_text(state)
        self.driver.find_element(*self.state_dropdown).click()

#City Dropdown.
    def click_city(self):
        self.driver.find_element(*self.city_dropdown).click()

    def pick_city(self, city):
        dropdown = Select(self.driver.find_element(*self.city_dropdown))
        dropdown.select_by_visible_text(city)
        self.driver.find_element(*self.city_dropdown).click()

#Zip Code Dropdown.
    def click_zc(self):
        self.driver.find_element(*self.zc_dropdown).click()

    def pick_zc(self, zipcode):
        dropdown = Select(self.driver.find_element(*self.zc_dropdown))
        dropdown.select_by_visible_text(zipcode)
        self.driver.find_element(*self.zc_dropdown).click()

    def enter_address(self, address):
        self.driver.find_element(*self.address_textfield).send_keys(address)

    def click_add(self):
        self.driver.find_element(*self.add_button).click()