from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


class RutePage:
    def __init__(self, driver):
        self.driver = driver
        self.route_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[4]/a")
        self.createRute_button = (By.XPATH, "//*[@id='root']/div/div/main/div[2]/div/div/div/div/div/div[1]/button")
        self.ruteName_textbox = (By.ID, "name")
        self.millage_textbox = (By.ID, "millage")
        self.avgTime_textbox = (By.ID, "AvgTime")

        # Origin & Destination Buttons
        self.origin_button = (By.XPATH, "//*[@id='formRoute']/div[2]/div[2]/button")
        self.destination_button = (By.XPATH, "//*[@id='formRoute']/div[2]/div[4]/button")


        # Dropdowns for Origin & Destination
        self.country_dropdown = (By.ID, "Country")
        self.state_dropdown = (By.ID, "State")
        self.city_dropdown = (By.ID, "City")

        self.destination_country_dropdown = (By.XPATH, "//*[@id='Country']")  # Adjust if needed
        self.destination_state_dropdown = (By.XPATH, "//*[@id='State']")  # Adjust if needed
        self.destination_city_dropdown = (By.XPATH, "//*[@id='City']")  # Adjust if needed

        self.add_button = (By.XPATH, "//*[@id='ModalRoute']/div/div[3]/button[1]")

    def click_routes(self):
        self.driver.find_element(*self.route_button).click()

    def click_create_route(self):
        self.driver.find_element(*self.createRute_button).click()

    def enter_rute_name(self, ruteName):
        self.driver.find_element(*self.ruteName_textbox).send_keys(ruteName)

    def enter_millage(self, millage):
        self.driver.find_element(*self.millage_textbox).send_keys(millage)

    def enter_avgTime(self, avgTime):
        self.driver.find_element(*self.avgTime_textbox).send_keys(avgTime)

    # Fill Origin & Destination
    def click_origin(self):
        self.driver.find_element(*self.origin_button).click()

    def click_destination(self):
        wait = WebDriverWait(self.driver, 10)

        # Ensure button is clickable before clicking
        element = wait.until(EC.element_to_be_clickable(self.destination_button))
        element.click()

    def select_country(self, country_name, is_destination=False):
        locator = self.destination_country_dropdown if is_destination else self.country_dropdown
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(country_name)
        self.driver.find_element(*locator).send_keys(Keys.RETURN)

    def select_state(self, state_name, is_destination=False):
        locator = self.destination_state_dropdown if is_destination else self.state_dropdown
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(state_name)
        self.driver.find_element(*locator).send_keys(Keys.RETURN)

    def select_city(self, city_name, is_destination=False):
        locator = self.destination_city_dropdown if is_destination else self.city_dropdown
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))  # ✅ Wait for element
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(city_name)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, city_name))  # ✅ Wait for value to be selected

    def click_add(self):
        self.driver.find_element(*self.add_button).click()
