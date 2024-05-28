from selenium.webdriver.common.by import By


class AddRemoveElementsPage():

    ADD_ELEMENT = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "#elements button")

    def __init__(self, driver):
        self.driver = driver

    def click_add_element(self):
        self.driver.find_element(*AddRemoveElementsPage.ADD_ELEMENT).click()

    def get_delete_button_count(self):
        return len(self.driver.find_elements(*AddRemoveElementsPage.DELETE_BUTTONS))

    def click_first_delete_button(self):
        if self.get_delete_button_count():
            self.driver.find_element(*AddRemoveElementsPage.DELETE_BUTTONS).click()
