from tests.base_test_ui import BaseUiTestCase
import logging
import time

log = logging.getLogger(__name__)


class WindowsTest(BaseUiTestCase):

    def test_multiple_tab_demo(self):
        dyn_loading = self.home_page.click_dynamic_loading()
        dyn_loading.right_click_example2()
        dyn_loading.right_click_example2()
        log.debug(self.get_window_titles())
        # note: appearance of tabs does not match order of handles
        # new tab opened to right, handles are added to end
        self.switch_to_window_by_index(2)
        time.sleep(2)
        self.switch_to_window_by_index(3)
        time.sleep(2)
        self.switch_to_window_by_title('The Internet')
        time.sleep(2)
        self.switch_to_window_by_title('The Internaut')

