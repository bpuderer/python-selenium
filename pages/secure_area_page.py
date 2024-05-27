from selenium.webdriver.common.by import By


class SecureAreaPage():

    STATUS_ALERT = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def get_alert_text(self):
        return self.driver.find_element(*SecureAreaPage.STATUS_ALERT).text
