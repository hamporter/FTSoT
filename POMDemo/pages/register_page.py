from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self,driver):
        self.driver = driver
        self.reg_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[2]/button")
        self.rfc_textbox = (By.ID, "RfcOrDot")
        self.reason_textbox = (By.ID, "legalNameCompany")
        self.tel_textbox = (By.ID, "officePhoneNumber")
        self.name_textbox = (By.ID, "name")
        self.lastname_textbox = (By.ID, "lastname")
        self.email_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.confirm_textbox = (By.ID, "repeatPassword")
        self.crea_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div/form/div[6]/div[2]/button")


    def open_page(self, url):
            self.driver.get(url)

    def click_register(self):
        self.driver.find_element(*self.reg_button).click()

    def enter_rfc(self, rfc):
        self.driver.find_element(*self.rfc_textbox).send_keys(rfc)

    def enter_reason(self, reason):
        self.driver.find_element(*self.reason_textbox).send_keys(reason)

    def enter_tel(self, tel):
        self.driver.find_element(*self.tel_textbox).send_keys(tel)

    def enter_name(self, name):
        self.driver.find_element(*self.name_textbox).send_keys(name)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_textbox).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_confirm(self, confirm):
        self.driver.find_element(*self.confirm_textbox).send_keys(confirm)

    def click_create(self):
        self.driver.find_element(*self.crea_button).click()