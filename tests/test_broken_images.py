from tests.base_test_ui import BaseUiTestCase


class BrokenImagesTests(BaseUiTestCase):

    def test_for_broken_images(self):
        self.assertFalse(self.home_page.click_broken_images().any_broken_images())
