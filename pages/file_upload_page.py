from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FileUploadPage():

    INPUT_FIELD = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")

    def __init__(self, driver):
        self.driver = driver

    def click_upload_button(self):
        self.driver.find_element(*FileUploadPage.UPLOAD_BUTTON).click()

    def upload_file(self, absolute_file_path):
        # https://www.selenium.dev/documentation/webdriver/elements/file_upload/
        self.driver.find_element(*FileUploadPage.INPUT_FIELD).send_keys(absolute_file_path)
        self.click_upload_button()

    def get_uploaded_files(self):
        return self.driver.find_element(*FileUploadPage.UPLOADED_FILES).text
