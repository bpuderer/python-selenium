from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EntryAdPage():

    MODAL = (By.ID, "modal")
    CLOSE_LINK = (By.CSS_SELECTOR, "div.modal-footer p")
    MODAL_TITLE = (By.CSS_SELECTOR, "div.modal-title h3")
    MODAL_TEXT = (By.CSS_SELECTOR, "div.modal-body p")

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.visibility_of_element_located(EntryAdPage.MODAL))

    def get_modal_text(self):
        return self.driver.find_element(*EntryAdPage.MODAL_TEXT).text

    def get_modal_title(self):
        return self.driver.find_element(*EntryAdPage.MODAL_TITLE).text

    def click_close_on_modal(self):
        self.driver.find_element(*EntryAdPage.CLOSE_LINK).click()
