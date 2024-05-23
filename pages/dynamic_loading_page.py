from selenium.webdriver.common.by import By
from pages.dynamic_loading_example1_page import DynamicLoadingExample1Page
from pages.dynamic_loading_example2_page import DynamicLoadingExample2Page


class DynamicLoadingPage():

    EXAMPLE1_LINK = (By.LINK_TEXT, "Example 1: Element on page that is hidden")
    EXAMPLE2_LINK = (By.LINK_TEXT, "Example 2: Element rendered after the fact")

    def __init__(self, driver):
        self.driver = driver

    def click_example1(self):
        self.driver.find_element(*DynamicLoadingPage.EXAMPLE1_LINK).click()
        return DynamicLoadingExample1Page(self.driver)

    def click_example2(self):
        self.driver.find_element(*DynamicLoadingPage.EXAMPLE2_LINK).click()
        return DynamicLoadingExample2Page(self.driver)
