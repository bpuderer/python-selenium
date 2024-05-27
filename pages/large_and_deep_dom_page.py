from selenium.webdriver.common.by import By


class LargeAndDeepDomPage():

    TABLE = (By.ID, "large-table")

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_table(self):
        table_element = self.driver.find_element(*LargeAndDeepDomPage.TABLE)
        script = "arguments[0].scrollIntoView();"
        self.driver.execute_script(script, table_element)
