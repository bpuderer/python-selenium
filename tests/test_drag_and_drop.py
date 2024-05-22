from tests.base_test_ui import BaseUiTestCase


class DragAndDropTest(BaseUiTestCase):

    def test_drag_and_drop(self):
        dnd = self.home_page.click_drag_and_drop()
        self.assertEqual(dnd.get_left_box_text(), "A");
        self.assertEqual(dnd.get_right_box_text(), "B");
        dnd.drag_left_to_right();
        self.assertEqual(dnd.get_left_box_text(), "B");
        self.assertEqual(dnd.get_right_box_text(), "A");
        dnd.drag_left_to_right();
        self.assertEqual(dnd.get_left_box_text(), "A");
        self.assertEqual(dnd.get_right_box_text(), "B");
        dnd.drag_right_to_left();
        self.assertEqual(dnd.get_left_box_text(), "B");
        self.assertEqual(dnd.get_right_box_text(), "A");
