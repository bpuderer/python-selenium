from tests.base_test_ui import BaseUiTestCase


class Checkboxes(BaseUiTestCase):

    def test_checkboxes_initial_state(self):
        checkboxes_page = self.home_page.click_checkboxes()
        self.assertFalse(checkboxes_page.is_checkbox_1_checked())
        self.assertTrue(checkboxes_page.is_checkbox_2_checked())

    def test_checkboxes(self):
        checkboxes_page = self.home_page.click_checkboxes()
        checkboxes_page.check_checkbox_1()
        checkboxes_page.check_checkbox_2()
        self.assertTrue(checkboxes_page.is_checkbox_1_checked())
        self.assertFalse(checkboxes_page.is_checkbox_2_checked())
        checkboxes_page.check_checkbox_1()
        checkboxes_page.check_checkbox_2()
        self.assertFalse(checkboxes_page.is_checkbox_1_checked())
        self.assertTrue(checkboxes_page.is_checkbox_2_checked())
