"""
Separate Unittest-style suite, kept apart from the PyTest suite on purpose:
the capstone spec calls for demonstrating both Unittest and PyTest.
Run with:  python -m unittest legacy_unittest.test_login_unittest -v
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.driver_factory import get_driver
from utils.config_reader import get_config
from pages.login_page import LoginPage


class TestLoginUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.base_url = get_config()["base_url"]

    def tearDown(self):
        self.driver.quit()

    def test_login_page_has_required_fields(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page(self.base_url)

        self.assertTrue(login_page.is_visible(login_page.LOGIN_EMAIL))
        self.assertTrue(login_page.is_visible(login_page.LOGIN_PASSWORD))
        self.assertTrue(login_page.is_visible(login_page.LOGIN_BUTTON))

    def test_invalid_credentials_rejected(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page(self.base_url)
        login_page.login("unittest_bogus_user@example.com", "wrongpass000")

        self.assertTrue(login_page.is_login_error_shown())


if __name__ == "__main__":
    unittest.main()
