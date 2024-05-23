from selenium.webdriver.common.by import By


class NestedFramesPage():

    BOTTOM_FRAME = "frame-bottom"
    TOP_FRAME = "frame-top"
    LEFT_FRAME = "frame-left"
    MIDDLE_FRAME = "frame-middle"
    RIGHT_FRAME = "frame-right"
    FRAME_BODY = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver

    def get_bottom_frame_text(self):
        self.switch_to_bottom_frame()
        text = self.get_frame_body_text()
        self.switch_to_parent_frame()
        return text

    def switch_to_bottom_frame(self):
        self.driver.switch_to.frame(NestedFramesPage.BOTTOM_FRAME)

    def get_frame_body_text(self):
        return self.driver.find_element(*NestedFramesPage.FRAME_BODY).text

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()


    def get_left_frame_text(self):
        return self.get_top_frame_text(NestedFramesPage.LEFT_FRAME)

    def get_middle_frame_text(self):
        return self.get_top_frame_text(NestedFramesPage.MIDDLE_FRAME)

    def get_right_frame_text(self):
        return self.get_top_frame_text(NestedFramesPage.RIGHT_FRAME)

    def get_top_frame_text(self, frame_name):
        self.switch_to_top_frame()
        if frame_name == NestedFramesPage.LEFT_FRAME:
            self.switch_to_left_frame()
        elif frame_name == NestedFramesPage.MIDDLE_FRAME:
            self.switch_to_middle_frame()
        elif frame_name == NestedFramesPage.RIGHT_FRAME:
            self.switch_to_right_frame()
        text = self.get_frame_body_text()
        self.switch_to_parent_frame()
        self.switch_to_parent_frame()
        return text

    def switch_to_top_frame(self):
        self.driver.switch_to.frame(NestedFramesPage.TOP_FRAME)

    def switch_to_left_frame(self):
        # left frame is inside top frame.  middle and right too
        self.driver.switch_to.frame(NestedFramesPage.LEFT_FRAME)

    def switch_to_middle_frame(self):
        self.driver.switch_to.frame(NestedFramesPage.MIDDLE_FRAME)

    def switch_to_right_frame(self):
        self.driver.switch_to.frame(NestedFramesPage.RIGHT_FRAME)
