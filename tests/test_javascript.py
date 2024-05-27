from tests.base_test_ui import BaseUiTestCase


class JavascriptTests(BaseUiTestCase):

    def test_scroll_into_view(self):
        #self.home_page.click_infinite_scroll().scroll_to_paragraph(20)
        inf_scrl = self.home_page.click_infinite_scroll()
        inf_scrl.scroll_to_paragraph(20)
        self.assertEqual(inf_scrl.get_number_of_paragraphs_present(), 20)

    def test_scroll_to_table(self):
        self.home_page.click_large_and_deep_dom().scroll_to_table()
