from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ContextMenuPage():

    BOX = (By.ID, "hot-spot")

    def __init__(self, driver):
        self.driver = driver

    def send_context_click_in_box(self):
        box_element = self.driver.find_element(*ContextMenuPage.BOX)
        actions = ActionChains(self.driver)
        actions.context_click(box_element).perform()

    def clear_alert(self):
        self.driver.switch_to.alert.accept()

    def alert_get_text(self):
        return self.driver.switch_to.alert.text
