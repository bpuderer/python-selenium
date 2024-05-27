import logging
import os

from selenium import webdriver

from framework.config import settings
from pages.home_page import HomePage
from tests.base_test import BaseTestCase


log = logging.getLogger(__name__)

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

    def get_window_titles(self):
        initial_handle = self.driver.current_window_handle

        titles = []
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            titles.append(self.driver.title)

        self.driver.switch_to.window(initial_handle)
        return titles

    def switch_to_window_by_index(self, index):
        # 1 based index
        if (index >= 1) and (index <= len(self.driver.window_handles)):
            self.driver.switch_to.window(self.driver.window_handles[index-1])

    def switch_to_window_by_title(self, title):
        # switches to first window that matches title in the handles
        try:
            self.switch_to_window_by_index(self.get_window_titles().index(title)+1)
        except ValueError:
            log.error(f'Cannot switch to window "{title}". No window with that title exists')
