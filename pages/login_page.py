from selenium.webdriver.common.by import By
from pages.secure_area_page import SecureAreaPage



class LoginPage():

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login button")
    FLASH_ERROR = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(*LoginPage.USERNAME_FIELD).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        return SecureAreaPage(self.driver)

    def get_flash_error_text(self):
        return self.driver.find_element(*LoginPage.FLASH_ERROR).text
