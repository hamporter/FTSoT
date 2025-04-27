from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

class CatalogTruckPage:

    def __init__(self, driver):
        self.driver = driver
        self.catalog_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[6]/a")
        self.trucks_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[6]/ul/li[1]/a")
        self.add_truck_button = (By.XPATH, "//*[@id='root']/div/div/main/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        self.e_number_textbox = (By.ID, "TrackNumber")
        self.vin_textbox = (By.ID, "Vin")
        #Tipo de camión
        self.kind_dropdown = (By.ID, "KindUnit")
        self.select_kind = (By.TAG_NAME, "Motocicleta")
        #Marca
        self.brand_dropdown = (By.ID, "Brand")
        self.select_brand = (By.TAG_NAME, "Audi")
        #Modelo
        self.model_dropdown = (By.ID, "Model")
        self.select_model = (By.TAG_NAME, "BMW")
        #Año
        self.year_dropdown = (By.ID, "Year")
        self.select_year = (By.TAG_NAME, "2020")

        self.tank_size_textbox = (By.ID, "tankSize")
        self.weight_textbox = (By.ID, "Lbgvm")
        self.weight2_textbox = (By.ID, "LbgcmMax")
        #Tipo de combustible
        self.fuel_dropdown = (By.ID, "FuelType")
        self.select_fuel = (By.TAG_NAME, "Diesel")

        self.radio_textbox = (By.ID, "Radio")
        self.tire_textbox = (By.ID, "RimMeasure")
        self.tire_qty_textbox = (By.ID, "QuantityTires")
        self.date_textbox = (By.ID, "PurchaseDate")
        self.price_textbox = (By.ID, "Cost")
        self.motor_textbox = (By.ID, "Engine")
        self.odometer_textbox = (By.ID, "Miles")
        #MxUs
        self.nation_dropdown = (By.ID, "MxUs")
        self.select_nation = (By.TAG_NAME, "BINACIONAL")
        #Tipo transmisión
        self.transmission_dropdown = (By.ID, "typeTransmission")
        self.select_transmission = (By.TAG_NAME, "Estándar")

        self.hazmat_slider = (By.XPATH, "//*[@id='formTruckPost']/div[7]/div[2]/div/label[2]")
        self.add_button = (By.XPATH, "//*[@id='ModalTruck']/div/div[3]/button[1]")


#Log In.
    def open_page(self, url):
            self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

#Truck Form.
    def click_catalog(self):
        self.driver.find_element(*self.catalog_button).click()

    def click_trucks(self):
        self.driver.find_element(*self.trucks_button).click()

    def click_add_truck(self):
        self.driver.find_element(*self.add_truck_button).click()

    def enter_e_number(self, e_number):
        self.driver.find_element(*self.e_number_textbox).send_keys(e_number)

    def enter_vin(self, vin):
        self.driver.find_element(*self.vin_textbox).send_keys(vin)

#kind
    def click_kind(self):
        self.driver.find_element(*self.kind_dropdown).click()

    def pick_kind(self, kind):
        dropdown = Select(self.driver.find_element(*self.kind_dropdown))
        dropdown.select_by_visible_text(kind)
        self.driver.find_element(*self.kind_dropdown).click()

#Brand
    def click_brand(self):
        self.driver.find_element(*self.brand_dropdown).click()

    def pick_brand(self, brand_name):
        dropdown = Select(self.driver.find_element(*self.brand_dropdown))
        dropdown.select_by_visible_text(brand_name)
        self.driver.find_element(*self.brand_dropdown).click()

#Model
    def click_model(self):
        self.driver.find_element(*self.model_dropdown).click()

    def pick_model(self, model):
        dropdown = Select(self.driver.find_element(*self.model_dropdown))
        dropdown.select_by_visible_text(model)
        self.driver.find_element(*self.model_dropdown).click()

#Year
    def click_year(self):
        self.driver.find_element(*self.year_dropdown).click()

    def pick_year(self, year):
        dropdown = Select(self.driver.find_element(*self.year_dropdown))
        dropdown.select_by_visible_text(year)
        self.driver.find_element(*self.year_dropdown).click()

    def enter_tank_size(self, tank_size):
        self.driver.find_element(*self.tank_size_textbox).send_keys(tank_size)

    def enter_weight(self, weight):
        self.driver.find_element(*self.weight_textbox).send_keys(weight)

    def enter_weight2(self, weight2):
        self.driver.find_element(*self.weight2_textbox).send_keys(weight2)

#Fuel
    def click_fuel(self):
        self.driver.find_element(*self.fuel_dropdown).click()

    def pick_fuel(self, fuel):
        dropdown = Select(self.driver.find_element(*self.fuel_dropdown))
        dropdown.select_by_visible_text(fuel)
        self.driver.find_element(*self.fuel_dropdown).click()

    def enter_radio(self, radio):
        self.driver.find_element(*self.radio_textbox).send_keys(radio)

    def enter_tire_size(self, tire_size):
        self.driver.find_element(*self.tire_textbox).send_keys(tire_size)

    def enter_tire_qty(self, tire_qty):
        self.driver.find_element(*self.tire_qty_textbox).send_keys(tire_qty)

    def enter_date(self, date):
        self.driver.find_element(*self.date_textbox).send_keys(date)

    def enter_price(self, price):
        self.driver.find_element(*self.price_textbox).send_keys(price)

    def enter_motor(self, motor):
        self.driver.find_element(*self.motor_textbox).send_keys(motor)

    def enter_odometer(self, odometer):
        self.driver.find_element(*self.odometer_textbox).send_keys(odometer)

#MxUs
    def click_nation(self):
        self.driver.find_element(*self.nation_dropdown).click()

    def pick_nation(self, nation):
        dropdown = Select(self.driver.find_element(*self.nation_dropdown))
        dropdown.select_by_visible_text(nation)
        self.driver.find_element(*self.nation_dropdown).click()

#Transmission
    def click_transmission(self):
        self.driver.find_element(*self.transmission_dropdown).click()

    def pick_transmission(self, transmission):
        dropdown = Select(self.driver.find_element(*self.transmission_dropdown))
        dropdown.select_by_visible_text(transmission)
        self.driver.find_element(*self.transmission_dropdown).click()

    def click_hazmat(self):
        self.driver.find_element(*self.hazmat_slider).click()

    def click_add(self):
        self.driver.find_element(*self.add_button).click()
