from tests.base_test_ui import BaseUiTestCase


class LoginTest(BaseUiTestCase):

    def test_login_success(self):
        login_page = self.home_page.click_form_authentication()
        login_page.set_username("tomsmith")
        login_page.set_password("SuperSecretPassword!")
        secure_page = login_page.click_login_button()
        self.assertIn("You logged into a secure area!", secure_page.get_alert_text())

    def test_login_failure_incorrect_password(self):
        login_page = self.home_page.click_form_authentication()
        login_page.set_username("tomsmith")
        login_page.set_password("wrongpassword!")
        login_page.click_login_button()
        self.assertIn("Your password is invalid!", login_page.get_flash_error_text())

    def test_login_failure_unknown_user(self):
        login_page = self.home_page.click_form_authentication()
        login_page.set_username("whoisthis")
        login_page.set_password("somepswd!")
        login_page.click_login_button()
        self.assertIn("Your username is invalid!", login_page.get_flash_error_text())

    def test_login_failure_empty_fields(self):
        login_page = self.home_page.click_form_authentication()
        login_page.click_login_button()
        self.assertIn("Your username is invalid!", login_page.get_flash_error_text())
