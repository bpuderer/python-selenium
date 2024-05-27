from tests.base_test_ui import BaseUiTestCase


class SliderTest(BaseUiTestCase):

    def test_slider(self):
        slider_page = self.home_page.click_horizontal_slider()
        for _ in range(5):
            slider_page.send_right_arrow_key_to_slider()
        self.assertEqual(slider_page.get_range(), "2.5")
