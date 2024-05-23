from selenium.webdriver.common.by import By
from pages.nested_frames_page import NestedFramesPage

class FramesPage():

    NESTED_FRAMES_LINK = (By.LINK_TEXT, "Nested Frames")

    def __init__(self, driver):
        self.driver = driver

    def click_nested_frames(self):
        self.driver.find_element(*FramesPage.NESTED_FRAMES_LINK).click()
        return NestedFramesPage(self.driver)
