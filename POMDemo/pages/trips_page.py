from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

class TripsPage:

    def __init__(self, driver):
        self.driver = driver
        self.trips_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[8]/a")
        self.add_trip_button = (By.ID, "addTravel")
#Client Dropdown.
        self.client_dropdown = (By.ID, "clientID")
        self.select_client = (By.TAG_NAME, "Sociedad Tronca")
#Route Dropdown.
        self.route_dropdown = (By.ID, "routeID")
        self.select_route = (By.ID, "TEST")
#--------------
        self.start_textfield = (By.ID, "startDate")
        self.end_textfield = (By.ID, "endDate")
#Service Dropdown.
        self.service_dropdown = (By.ID, "typeOfService")
        self.select_service = (By.TAG_NAME, "Exportacion")
#Vehicle Dropdown.
        self.vehicle_dropdown = (By.ID, "typeOfVehicle")
        self.select_vehicle = (By.TAG_NAME, "Vehiculo")
#--------------
        self.hazmat_slider = (By.XPATH, "//*[@id='formTravel']/div[3]/div/div/label[2]/span")
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

#Trips
    def click_trips(self):
        self.driver.find_element(*self.trips_button).click()

    def click_add_trip(self):
        self.driver.find_element(*self.add_trip_button).click()
#Client Dropdown.
    def click_client(self):
        self.driver.find_element(*self.client_dropdown).click()

    def pick_client(self, client):
        dropdown = Select(self.driver.find_element(*self.client_dropdown))
        dropdown.select_by_visible_text(client)
        self.driver.find_element(*self.client_dropdown).click()
#--------------
#Route Dropdown.
    def click_route(self):
        self.driver.find_element(*self.route_dropdown).click()

    def pick_route(self, route):
        dropdown = Select(self.driver.find_element(*self.route_dropdown))
        dropdown.select_by_visible_text(route)
        self.driver.find_element(*self.route_dropdown).click()
#--------------
    def enter_start(self, start):
        self.driver.find_element(*self.start_textfield).send_keys(start)

    def enter_end(self, end):
        self.driver.find_element(*self.end_textfield).send_keys(end)

#Service Dropdown.
    def click_service(self):
        self.driver.find_element(*self.service_dropdown).click()

    def pick_service(self, service):
        dropdown = Select(self.driver.find_element(*self.service_dropdown))
        dropdown.select_by_visible_text(service)
        self.driver.find_element(*self.service_dropdown).click()

#Vehicle Dropdown.
    def click_vehicle(self):
        self.driver.find_element(*self.vehicle_dropdown).click()

    def pick_vehicle(self, vehicle):
        dropdown = Select(self.driver.find_element(*self.vehicle_dropdown))
        dropdown.select_by_visible_text(vehicle)
        self.driver.find_element(*self.vehicle_dropdown).click()

    def click_add(self):
        self.driver.find_element(*self.add_button).click()


