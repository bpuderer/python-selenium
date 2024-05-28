from http import HTTPStatus
import requests
from selenium.webdriver.common.by import By

import logging


log = logging.getLogger(__name__)

class BrokenImagesPage():

    IMAGES = (By.TAG_NAME, "img")

    def __init__(self, driver):
        self.driver = driver

    def any_broken_images(self):
        images = self.driver.find_elements(*BrokenImagesPage.IMAGES)
        for image in images:
            url = image.get_attribute('src')
            resp = requests.head(url)
            if resp.status_code != HTTPStatus.OK:
                log.debug(f'Broken image: {url}')
                return True
        return False
