from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DynamicLoadingExample1Page():

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_INDICATOR = (By.ID, "loading")
    LOADED_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def __init__(self, driver):
        self.driver = driver

    def click_start(self):
        self.driver.find_element(*DynamicLoadingExample1Page.START_BUTTON).click()
        # don't give control back until text visible
        wait = WebDriverWait(self.driver, timeout=10)
        # some options on the expected_conditions
        #wait.until(EC.invisibility_of_element(self.driver.find_element(*DynamicLoadingExample1Page.LOADING_INDICATOR)))
        #wait.until(EC.invisibility_of_element(DynamicLoadingExample1Page.LOADING_INDICATOR))
        wait.until(EC.invisibility_of_element_located(DynamicLoadingExample1Page.LOADING_INDICATOR))

    def get_loaded_text(self):
        return self.driver.find_element(*DynamicLoadingExample1Page.LOADED_TEXT).text
