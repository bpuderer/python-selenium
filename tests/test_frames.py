from tests.base_test_ui import BaseUiTestCase


class FramesTests(BaseUiTestCase):

    def test_nested_frames(self):
        nested_frames = self.home_page.click_frames().click_nested_frames()
        self.assertEqual(nested_frames.get_bottom_frame_text(), "BOTTOM")
        self.assertEqual(nested_frames.get_left_frame_text(), "LEFT")
        self.assertEqual(nested_frames.get_middle_frame_text(), "MIDDLE")
        self.assertEqual(nested_frames.get_right_frame_text(), "RIGHT")
