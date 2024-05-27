from selenium.webdriver.common.by import By


class InfiniteScrollPage():

    TEXT_BLOCKS = (By.CLASS_NAME, "jscroll-added")

    def __init__(self, driver):
        self.driver = driver

    def get_number_of_paragraphs_present(self):
        return len(self.driver.find_elements(*InfiniteScrollPage.TEXT_BLOCKS))

    def scroll_to_paragraph(self, paragraph_number):
        # one based
        script = "window.scrollTo(0, document.body.scrollHeight)"
        while self.get_number_of_paragraphs_present() < paragraph_number:
            self.driver.execute_script(script)
