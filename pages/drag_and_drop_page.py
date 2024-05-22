from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DragAndDropPage():

    LEFT_BOX = (By.ID, "column-a")
    RIGHT_BOX = (By.ID, "column-b")
    LEFT_BOX_TEXT = (By.CSS_SELECTOR, "#column-a header")
    RIGHT_BOX_TEXT = (By.CSS_SELECTOR, "#column-b header")

    def __init__(self, driver):
        self.driver = driver

    def get_left_box_text(self):
        return self.driver.find_element(*DragAndDropPage.LEFT_BOX_TEXT).text

    def get_right_box_text(self):
        return self.driver.find_element(*DragAndDropPage.RIGHT_BOX_TEXT).text

    def drag_left_to_right(self):
        ac = ActionChains(self.driver)
        ac.drag_and_drop(
            self.driver.find_element(*DragAndDropPage.LEFT_BOX),
            self.driver.find_element(*DragAndDropPage.RIGHT_BOX),
        ).perform()

    def drag_right_to_left(self):
        ac = ActionChains(self.driver)
        ac.drag_and_drop(
            self.driver.find_element(*DragAndDropPage.RIGHT_BOX),
            self.driver.find_element(*DragAndDropPage.LEFT_BOX),
        ).perform()
