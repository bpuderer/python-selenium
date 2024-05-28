from selenium.webdriver.common.by import By


class CheckboxesPage():

    CHECKBOX_1 = (By.XPATH, "//input[1]")
    CHECKBOX_2 = (By.XPATH, "//input[2]")
    CHECKBOXES = (By.ID, "checkboxes")

    def __init__(self, driver):
        self.driver = driver

    def is_checkbox_1_checked(self):
        return self.driver.find_element(*CheckboxesPage.CHECKBOX_1).is_selected()

    def is_checkbox_2_checked(self):
        return self.driver.find_element(*CheckboxesPage.CHECKBOX_2).is_selected()

    def check_checkbox_1(self):
        self.driver.find_element(*CheckboxesPage.CHECKBOX_1).click()

    def check_checkbox_2(self):
        self.driver.find_element(*CheckboxesPage.CHECKBOX_2).click()

    def get_checkbox_labels(self):
        return self.driver.find_element(*CheckboxesPage.CHECKBOXES).text.split('\n')
