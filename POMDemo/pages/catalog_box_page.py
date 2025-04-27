from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

class CatalogBoxPage:

    def __init__(self,driver):
        self.driver = driver
        self.catalog_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[6]/a")
        self.boxes_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[6]/ul/li[2]/a")
        self.add_box_button = (By.XPATH, "//*[@id='root']/div/div/main/div/div/div/div/div/div/div[1]/div[1]/button")
        self.e_number_textfield = (By.ID, "TrackNumber")
        self.vin_textfield = (By.ID, "Vin")
#Box kind dropdown.
        self.box_kind_dropdown = (By.ID, "KindUnit")
        self.select_box_kind = (By.TAG_NAME, "Power Only")
#Brand dropdown.
        self.brand_dropdown = (By.ID, "Brand")
        self.select_brand = (By.TAG_NAME, "International")
#Year dropdown.
        self.year_dropdown = (By.ID, "Year")
        self.select_year = (By.TAG_NAME, "1992")

        self.radio_textfield = (By.ID, "Radio")
        self.weight_min_textfield = (By.ID, "minWeight")
        self.weight_max_textfield = (By.ID, "maxWeight")
#Tire kind dropdown.
        self.tire_kind_dropdown = (By.ID, "TireType")
        self.select_tire_kind = (By.TAG_NAME, "Traccion")

        self.tire_size_textfield = (By.ID, "TireSize")
        self.rim_textfield = (By.ID, "TireRin")
        self.date_textfield = (By.ID, "PurchaseDate")
        self.refri_slider = (By.XPATH, "//*[@id='formTrailerPost']/div[5]/div[1]/div/label[2]/span")
        self.price_textfield = (By.ID, "Price")
# MxUs dropdown.
        self.mxus_dropdown = (By.ID, "MxUs")
        self.select_mxus = (By.TAG_NAME, "MX")

        self.hazmat_slider = (By.XPATH, "//*[@id='formTrailerPost']/div[6]/div[1]/div/label[2]/span")
        self.owner_slider = (By.XPATH, "//*[@id='formTrailerPost']/div[6]/div[2]/div/label[2]/span")
        self.add_button = (By.XPATH, "//*[@id='ModalTrailer']/div/div[3]/button[1]")

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

    def click_boxes(self):
        self.driver.find_element(*self.boxes_button).click()

    def click_add_box(self):
        self.driver.find_element(*self.add_box_button).click()

    def enter_e_number(self, e_number):
        self.driver.find_element(*self.e_number_textfield).send_keys(e_number)

    def enter_vin(self, vin):
        self.driver.find_element(*self.vin_textfield).send_keys(vin)

#Box Kind Dropdown.
    def click_box_kind(self):
        self.driver.find_element(*self.box_kind_dropdown).click()

    def pick_box_kind(self, boxkind):
        dropdown = Select(self.driver.find_element(*self.box_kind_dropdown))
        dropdown.select_by_visible_text(boxkind)
        self.driver.find_element(*self.box_kind_dropdown).click()
#-------------

#Brand Dropdown.
    def click_brand(self):
        self.driver.find_element(*self.brand_dropdown).click()

    def pick_brand(self, brand):
        dropdown = Select(self.driver.find_element(*self.brand_dropdown))
        dropdown.select_by_visible_text(brand)
        self.driver.find_element(*self.brand_dropdown).click()
#-------------

#Year Dropdown.
    def click_year(self):
        self.driver.find_element(*self.year_dropdown).click()

    def pick_year(self, year):
        dropdown = Select(self.driver.find_element(*self.year_dropdown))
        dropdown.select_by_visible_text(year)
        self.driver.find_element(*self.year_dropdown).click()
#-------------
    def enter_radio(self, radio):
        self.driver.find_element(*self.radio_textfield).send_keys(radio)

    def enter_min_weight(self, min):
        self.driver.find_element(*self.weight_min_textfield).send_keys(min)

    def enter_max_weight(self, max):
        self.driver.find_element(*self.weight_max_textfield).send_keys(max)

#Tire Kind Dropdown.
    def click_tire_kind(self):
        self.driver.find_element(*self.tire_kind_dropdown).click()

    def pick_tire_kind(self, tirekind):
        dropdown = Select(self.driver.find_element(*self.tire_kind_dropdown))
        dropdown.select_by_visible_text(tirekind)
        self.driver.find_element(*self.tire_kind_dropdown).click()
#-------------
    def enter_tire_size(self, tiresize):
        self.driver.find_element(*self.tire_size_textfield).send_keys(tiresize)

    def enter_rim(self, rim):
        self.driver.find_element(*self.rim_textfield).send_keys(rim)

    def enter_date(self, date):
        self.driver.find_element(*self.date_textfield).send_keys(date)

    def click_refri(self):
        self.driver.find_element(*self.refri_slider).click()

    def enter_price(self, price):
        self.driver.find_element(*self.price_textfield).send_keys(price)

    def click_mxus(self):
        self.driver.find_element(*self.mxus_dropdown).click()

    def pick_mxus(self, nation):
        dropdown = Select(self.driver.find_element(*self.mxus_dropdown))
        dropdown.select_by_visible_text(nation)
        self.driver.find_element(*self.mxus_dropdown).click()

    def click_add(self):
        self.driver.find_element(*self.add_button).click()