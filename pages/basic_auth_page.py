from selenium.webdriver.common.by import By


class BasicAuthPage():

    BODY_TEXT = (By.TAG_NAME, "p")

    def __init__(self, driver):
        self.driver = driver

    def get_body_text(self):
        return self.driver.find_element(*BasicAuthPage.BODY_TEXT).text
