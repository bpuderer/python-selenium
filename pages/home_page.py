from selenium.webdriver.common.by import By
from pages.drag_and_drop_page import DragAndDropPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_loading_page import DynamicLoadingPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def click_drag_and_drop(self):
        self.click_link("Drag and Drop");
        return DragAndDropPage(self.driver);

    def click_dropdown(self):
        self.click_link("Dropdown");
        return DropdownPage(self.driver);

    def click_dynamic_loading(self):
        self.click_link("Dynamic Loading")
        return DynamicLoadingPage(self.driver)

    def click_link(self, link_text):
        self.driver.find_element(By.LINK_TEXT, link_text).click();
