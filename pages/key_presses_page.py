from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KeyPressesPage():

    INPUT_FIELD = (By.ID, "target")
    RESULT = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver

    def send_letter(self, letter):
        self.driver.find_element(*KeyPressesPage.INPUT_FIELD).send_keys(letter)

    def send_page_down(self):
        self.driver.find_element(*KeyPressesPage.INPUT_FIELD).send_keys(Keys.PAGE_DOWN)

    def get_result_text(self):
        return self.driver.find_element(*KeyPressesPage.RESULT).text
