from tests.base_test_ui import BaseUiTestCase


class ContextClickAlertsTests(BaseUiTestCase):

    def test_context_click_clear_alert(self):
        context_menu = self.home_page.click_context_menu()
        context_menu.send_context_click_in_box()
        self.assertEqual(context_menu.alert_get_text(), "You selected a context menu")
        context_menu.clear_alert()
