from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")


class UsersPage:
    def __init__(self, driver):
        self.driver = driver
        self.users_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[3]/a")
        self.create_user_button = (By.XPATH, "//*[@id='createUser']")
        self.name_textfield = (By.ID, "name")
        self.lastname_textfield = (By.ID, "lastName")
        self.email_textfield = (By.ID, "email")
        self.password_textfield = (By.ID, "password")
        self.confirm_p_textfield = (By.ID, "confirmPassword")
        self.role_dropdown = (By.ID, "role")
        self.select_role = (By.TAG_NAME, "Client")
        self.add_button = (By.XPATH, "//*[@id='ModalBU']/div/div[3]/button[1]")

#Log In.
    def open_page(self, url):
            self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

#Users.
    def click_users(self):
        self.driver.find_element(*self.users_button).click()

    def click_create_user(self):
        self.driver.find_element(*self.create_user_button).click()

    def enter_name(self, name):
        self.driver.find_element(*self.name_textfield).send_keys(name)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.lastname_textfield).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textfield).send_keys(email)

    def enter_new_password(self, password):
        self.driver.find_element(*self.password_textfield).send_keys(password)

    def enter_new_password_confirm(self, confirm):
        self.driver.find_element(*self.confirm_p_textfield).send_keys(confirm)

    def click_role(self):
        self.driver.find_element(*self.role_dropdown).click()

    def pick_role(self, role_name):
        dropdown = Select(self.driver.find_element(*self.role_dropdown))
        dropdown.select_by_visible_text(role_name)
        self.driver.find_element(*self.role_dropdown).click()

    def click_add(self):
        self.driver.find_element(*self.add_button).click()



