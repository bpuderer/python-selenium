import os

from selenium import webdriver

from framework.config import settings
from pages.home_page import HomePage
from tests.base_test import BaseTestCase


class BaseUiTestCase(BaseTestCase):

    def setUp(self):
        if settings['browser'].lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif settings['browser'].lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif settings['browser'].lower() == 'headless chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('headless')
            self.driver = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'Browser {settings["browser"]} is not supported')

        self.driver.get(settings['url'])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(os.path.join('screenshots', filename))
