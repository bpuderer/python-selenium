from tests.base_test_ui import BaseUiTestCase


class KeyPressTests(BaseUiTestCase):

    def test_key_press_letter(self):
        key_press = self.home_page.click_key_presses()
        key_press.send_letter('Q')
        self.assertEqual(key_press.get_result_text(), 'You entered: Q')
        #site does not distinguish between upper and lower case
        #key_press.send_letter('q')
        #self.assertEqual(key_press.get_result_text(), 'You entered: q')

    def test_key_press_editing_key(self):
        key_press = self.home_page.click_key_presses()
        key_press.send_page_down()
        self.assertEqual(key_press.get_result_text(), 'You entered: PAGE_DOWN')
