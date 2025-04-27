from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div[1]/div/form/div[3]/div[1]/button")

class InventoryTiresPage:

    def __init__(self, driver):
        self.driver = driver
        self.inventory_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[7]/a")
        self.tires_button = (By.XPATH, "//*[@id='root']/div/div/div/div/ul/li[7]/ul/li/a")
        self.add_tire_button = (By.XPATH, "//*[@id='root']/div/div/main/div/div/div[2]/div/div/div/div[1]/div[1]/button")
#Brand Dropdown.
        self.brand_dropdown = (By.ID, "TireMark")
        self.select_brand = (By.TAG_NAME, "Michelin")
#--------------
        self.model_textfield = (By.ID, "Model")
        self.part_no_textfield = (By.ID, "PartNumber")
        self.width_textfield = (By.ID, "Width")
        self.height_textfield = (By.ID, "Height")
        self.depth_textfield = (By.ID, "Depth")
#Tire Application Dropdown.
        self.app_dropdown = (By.ID, "TireApplication")
        self.select_app = (By.TAG_NAME, "Tracción")
#--------------
        self.rim_textfield = (By.ID, "RimSize")
        self.max_weight_textfield = (By.ID, "WeightCapacity")
        self.cam_type_textfield = (By.ID, "TypeCamera")
        self.range_textfield = (By.ID, "SpeedRange")
        self.add_button = (By.XPATH, "//*[@id='ModalTire']/div/div[3]/button[1]")

# Log In.
    def open_page(self, url):
            self.driver.get(url)

    def enter_username(self, username):
            self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
            self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
            self.driver.find_element(*self.login_button).click()

#Tires
    def click_inventory(self):
        self.driver.find_element(*self.inventory_button).click()

    def click_tires(self):
        self.driver.find_element(*self.tires_button).click()

    def click_add_tire(self):
        self.driver.find_element(*self.add_tire_button).click()

#Brand Dropdown.
    def click_brand(self):
        self.driver.find_element(*self.brand_dropdown).click()

    def pick_brand(self, brand):
        dropdown = Select(self.driver.find_element(*self.brand_dropdown))
        dropdown.select_by_visible_text(brand)
        self.driver.find_element(*self.brand_dropdown).click()
#--------------
    def enter_model(self, model):
        self.driver.find_element(*self.model_textfield).send_keys(model)

    def enter_part_no(self, part):
        self.driver.find_element(*self.part_no_textfield).send_keys(part)

    def enter_width(self, width):
        self.driver.find_element(*self.width_textfield).send_keys(width)

    def enter_height(self, height):
        self.driver.find_element(*self.height_textfield).send_keys(height)

    def enter_depth(self, depth):
        self.driver.find_element(*self.depth_textfield).send_keys(depth)

#Tire Application Dropdown.
    def click_app(self):
        self.driver.find_element(*self.app_dropdown).click()

    def pick_app(self, tireapp):
        dropdown = Select(self.driver.find_element(*self.app_dropdown))
        dropdown.select_by_visible_text(tireapp)
        self.driver.find_element(*self.brand_dropdown).click()
#--------------
    def enter_rim(self, rim):
        self.driver.find_element(*self.rim_textfield).send_keys(rim)

    def enter_weight(self, weight):
        self.driver.find_element(*self.max_weight_textfield).send_keys(weight)

    def enter_type(self, type):
        self.driver.find_element(*self.cam_type_textfield).send_keys(type)

    def enter_range(self, range):
        self.driver.find_element(*self.range_textfield).send_keys(range)

    def click_add(self):
        self.driver.find_element(*self.add_button).click()