from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropdownPage():

    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def find_dropdown_webelement(self):
        return self.driver.find_element(*DropdownPage.DROPDOWN)

    def find_dropdown_element(self):
        return Select(self.find_dropdown_webelement())

    def select_from_dropdown(self, option):
        self.find_dropdown_element().select_by_visible_text(option)

    def get_selected_options(self):
        selected = self.find_dropdown_element().all_selected_options
        return [selection.text for selection in selected]

    def enable_multi_select(self):
        # demo of running JS only!
        script = "arguments[0].setAttribute('multiple', '')"
        self.driver.execute_script(script, self.find_dropdown_webelement())
