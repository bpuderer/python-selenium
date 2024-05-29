from tests.base_test_ui import BaseUiTestCase


class FileUploadTests(BaseUiTestCase):

    def test_file_upload(self):
        upload_page = self.home_page.click_file_upload()
        upload_page.upload_file('/tmp/blah.txt')
        self.assertEqual(upload_page.get_uploaded_files(), 'blah.txt')
