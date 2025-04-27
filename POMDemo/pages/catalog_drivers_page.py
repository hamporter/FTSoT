from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

class CatalogDriversPage:

    def __init__(self, driver):
        self.driver = driver
        self.catalog_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[6]/a")
        self.drivers_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[6]/ul/li[3]/a")
        self.add_driver_button = (By.XPATH, "//*[@id='root']/div/div/main/div/div/div/div/div/div/div[1]/div/button")
        self.name_textfield = (By.ID, "Name")
        self.lastname_textfield = (By.ID, "LastName")
        self.rfc_textfield = (By.ID, "rfc")
        self.tel_textfield = (By.ID, "phoneNumber")
        self.emp_num_textfield = (By.ID, "EmployeeNumber")
#Country Dropdown.
        self.country_dropdown = (By.ID, "Country")
        self.select_country = (By.TAG_NAME, "México")
#State Dropdown.
        self.state_dropdown = (By.ID, "State")
        self.select_state = (By.TAG_NAME, "Aguascalientes")
#City Dropdown.
        self.city_dropdown = (By.ID, "City")
        self.select_city = (By.TAG_NAME, "El Llano")
#--------------
        self.email_textfield = (By.ID, "email")
        self.password_textfield = (By.ID, "password")
        self.con_pass_textfield = (By.ID, "confirmPassword")
        self.add_button = (By.XPATH, "//*[@id='ModalCD']/div/div[3]/button[1]")


#Log In.
    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

#Drivers Form.

    def click_catalog(self):
        self.driver.find_element(*self.catalog_button).click()

    def click_drivers(self):
        self.driver.find_element(*self.drivers_button).click()

    def click_add_driver(self):
        self.driver.find_element(*self.add_driver_button).click()

    def enter_name(self, name):
        self.driver.find_element(*self.name_textfield).send_keys(name)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_textfield).send_keys(lastname)

    def enter_rfc(self, rfc):
        self.driver.find_element(*self.rfc_textfield).send_keys(rfc)

    def enter_phone(self, phone):
        self.driver.find_element(*self.tel_textfield).send_keys(phone)

    def enter_emp_num(self, employee):
        self.driver.find_element(*self.emp_num_textfield).send_keys(employee)

#Country Dropdown.
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

#--------------
    def enter_email(self, email):
        self.driver.find_element(*self.email_textfield).send_keys(email)

    def enter_new_password(self, newpassword):
        self.driver.find_element(*self.password_textfield).send_keys(newpassword)

    def enter_conf_password(self, confirm):
        self.driver.find_element(*self.con_pass_textfield).send_keys(confirm)

    def click_add(self):
        self.driver.find_element(*self.add_button).click()

