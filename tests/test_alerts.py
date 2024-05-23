from tests.base_test_ui import BaseUiTestCase


class WaitsTest(BaseUiTestCase):

    def test_accept_alert(self):
        alerts_page = self.home_page.click_javascript_alerts()
        alerts_page.trigger_alert()
        alerts_page.alert_click_to_accept()
        self.assertEqual(alerts_page.get_result(), "You successfully clicked an alert")

    def test_get_text_from_alart(self):
        alerts_page = self.home_page.click_javascript_alerts()
        alerts_page.trigger_confirm()
        alert_text = alerts_page.alert_get_text()
        alerts_page.alert_click_to_dismiss()
        self.assertEqual(alert_text, "I am a JS Confirm")
        self.assertEqual(alerts_page.get_result(), "You clicked: Cancel")

    def test_enter_text_alert(self):
        alerts_page = self.home_page.click_javascript_alerts()
        alerts_page.trigger_prompt()
        test_string = "TAU rocks"
        alerts_page.alert_set_input(test_string)
        alerts_page.alert_click_to_accept()
        self.assertEqual(alerts_page.get_result(), "You entered: " + test_string)
