from tests.base_test_ui import BaseUiTestCase


class DropdownTest(BaseUiTestCase):

    def test_dropdown_single_select(self):
        dd = self.home_page.click_dropdown()
        SELECTION = "Option 2"
        dd.select_from_dropdown(SELECTION)
        selected = dd.get_selected_options()
        self.assertEqual(len(selected), 1)
        self.assertIn(SELECTION, selected)

    def test_dropdown_multi_select(self):
        dd = self.home_page.click_dropdown()
        OPTION1 = "Option 1"
        OPTION2 = "Option 2"
        dd.enable_multi_select()
        dd.select_from_dropdown(OPTION1)
        dd.select_from_dropdown(OPTION2)
        selected = dd.get_selected_options()
        self.assertEqual(len(selected), 2)
        self.assertIn(OPTION1, selected)
        self.assertIn(OPTION2, selected)
