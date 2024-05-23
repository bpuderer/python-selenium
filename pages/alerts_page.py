from selenium.webdriver.common.by import By


class AlertsPage():

    TRIGGER_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    TRIGGER_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    TRIGGER_PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT = (By.ID, "result")


    def __init__(self, driver):
        self.driver = driver

    def trigger_alert(self):
        self.driver.find_element(*AlertsPage.TRIGGER_ALERT_BUTTON).click()

    def trigger_confirm(self):
        self.driver.find_element(*AlertsPage.TRIGGER_CONFIRM_BUTTON).click()

    def trigger_prompt(self):
        self.driver.find_element(*AlertsPage.TRIGGER_PROMPT_BUTTON).click()

    def alert_click_to_accept(self):
        self.driver.switch_to.alert.accept()

    def get_result(self):
        return self.driver.find_element(*AlertsPage.RESULT).text

    def alert_click_to_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def alert_get_text(self):
        return self.driver.switch_to.alert.text

    def alert_set_input(self, text):
        self.driver.switch_to.alert.send_keys(text)
