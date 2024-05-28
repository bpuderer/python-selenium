from tests.base_test_ui import BaseUiTestCase


class AuthTests(BaseUiTestCase):

    def test_add_remove_elements(self):
        basic_auth = self.home_page.click_basic_auth_plus_credentials('admin', 'admin')
        self.assertEqual(basic_auth.get_body_text(), 'Congratulations! You must have the proper credentials.')
