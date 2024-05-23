from tests.base_test_ui import BaseUiTestCase


class WaitsTest(BaseUiTestCase):

    def test_wait_until_hidden(self):
        loading_page = self.home_page.click_dynamic_loading().click_example1()
        loading_page.click_start()
        self.assertEqual(loading_page.get_loaded_text(), "Hello World!")

    def test_wait_until_present(self):
        loading_page = self.home_page.click_dynamic_loading().click_example2()
        loading_page.click_start()
        self.assertEqual(loading_page.get_loaded_text(), "Hello World!")
