from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DynamicLoadingExample2Page():

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADED_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def __init__(self, driver):
        self.driver = driver

    def click_start(self):
        self.driver.find_element(*DynamicLoadingExample2Page.START_BUTTON).click()
        # don't give control back until text loaded
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(DynamicLoadingExample2Page.LOADED_TEXT))

    def get_loaded_text(self):
        return self.driver.find_element(*DynamicLoadingExample2Page.LOADED_TEXT).text
