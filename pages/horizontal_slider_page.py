from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HorizontalSliderPage():

    HORIZONTAL_SLIDER = (By.CSS_SELECTOR, "div.sliderContainer input")
    SLIDER_RANGE = (By.ID, "range")

    def __init__(self, driver):
        self.driver = driver

    def send_right_arrow_key_to_slider(self):
        self.driver.find_element(*HorizontalSliderPage.HORIZONTAL_SLIDER).send_keys(Keys.ARROW_RIGHT)

    def get_range(self):
        return self.driver.find_element(*HorizontalSliderPage.SLIDER_RANGE).text
