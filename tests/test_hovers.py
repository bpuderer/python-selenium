from tests.base_test_ui import BaseUiTestCase


class HoversTests(BaseUiTestCase):

    def test_hovering(self):
        hovers = self.home_page.click_hovers()
        caption = hovers.hover_over_figure(2)
        self.assertTrue(caption['is_displayed'])
        self.assertEqual(caption['header'], "name: user2")
        self.assertEqual(caption['link_text'], "View profile")
        self.assertTrue(caption['link'].endswith("/users/2"))

