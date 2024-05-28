from tests.base_test_ui import BaseUiTestCase


class AddRemoveElementsTests(BaseUiTestCase):

    def test_add_remove_elements(self):
        add_remove_page = self.home_page.click_add_remove_elements()
        self.assertEqual(add_remove_page.get_delete_button_count(), 0)
        add_remove_page.click_add_element()
        add_remove_page.click_add_element()
        add_remove_page.click_add_element()
        self.assertEqual(add_remove_page.get_delete_button_count(), 3)
        add_remove_page.click_first_delete_button()
        self.assertEqual(add_remove_page.get_delete_button_count(), 2)
