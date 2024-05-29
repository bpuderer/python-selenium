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
from pages.infinite_scroll_page import InfiniteScrollPage
from pages.large_and_deep_dom_page import LargeAndDeepDomPage
from pages.checkboxes_page import CheckboxesPage
from pages.broken_images_page import BrokenImagesPage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.key_presses_page import KeyPressesPage
from pages.file_upload_page import FileUploadPage
from pages.basic_auth_page import BasicAuthPage


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

    def click_infinite_scroll(self):
        self.click_link("Infinite Scroll")
        return InfiniteScrollPage(self.driver)

    def click_large_and_deep_dom(self):
        self.click_link("Large & Deep DOM")
        return LargeAndDeepDomPage(self.driver)

    def click_checkboxes(self):
        self.click_link("Checkboxes")
        return CheckboxesPage(self.driver)

    def click_broken_images(self):
        self.click_link("Broken Images")
        return BrokenImagesPage(self.driver)

    def click_add_remove_elements(self):
        self.click_link("Add/Remove Elements")
        return AddRemoveElementsPage(self.driver)

    def click_key_presses(self):
        self.click_link("Key Presses")
        return KeyPressesPage(self.driver)

    def click_file_upload(self):
        self.click_link("File Upload")
        return FileUploadPage(self.driver)

    def click_basic_auth_plus_credentials(self, user, password):
        url = self.driver.find_element(By.XPATH, "//a[text()='Basic Auth']").get_attribute('href')
        self.driver.get(self.add_auth_to_url(url, user, password))
        return BasicAuthPage(self.driver)

    def add_auth_to_url(self, url, user, password):
        location_to_insert_auth = url.find('//') + 2
        return url[:location_to_insert_auth] + user + ':' + password + '@' + url[location_to_insert_auth:]

    def click_link(self, link_text):
        self.driver.find_element(By.LINK_TEXT, link_text).click();
