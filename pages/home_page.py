from selenium.webdriver.common.by import By
from pages.drag_and_drop_page import DragAndDropPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.alerts_page import AlertsPage
from pages.context_menu_page import ContextMenuPage
from pages.entry_ad_page import EntryAdPage
from pages.frames_page import FramesPage
from pages.hovers_page import HoversPage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.login_page import LoginPage


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

    def click_javascript_alerts(self):
        self.click_link("JavaScript Alerts")
        return AlertsPage(self.driver)

    def click_context_menu(self):
        self.click_link("Context Menu")
        return ContextMenuPage(self.driver)

    def click_entry_ad(self):
        self.click_link("Entry Ad")
        return EntryAdPage(self.driver)

    def click_frames(self):
        self.click_link("Frames")
        return FramesPage(self.driver)

    def click_hovers(self):
        self.click_link("Hovers")
        return HoversPage(self.driver)

    def click_horizontal_slider(self):
        self.click_link("Horizontal Slider")
        return HorizontalSliderPage(self.driver)

    def click_form_authentication(self):
        self.click_link("Form Authentication")
        return LoginPage(self.driver)

    def click_link(self, link_text):
        self.driver.find_element(By.LINK_TEXT, link_text).click();
