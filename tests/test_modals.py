from tests.base_test_ui import BaseUiTestCase


class ModalTests(BaseUiTestCase):

    def test_modals(self):
          entry_ad = self.home_page.click_entry_ad()
          self.assertEqual(entry_ad.get_modal_title(), "THIS IS A MODAL WINDOW")
          self.assertEqual(entry_ad.get_modal_text(), "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker).")
          entry_ad.click_close_on_modal()
