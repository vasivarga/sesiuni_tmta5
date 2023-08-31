import unittest

from pages.login_page import LoginPage

class LoginTests(unittest.TestCase):

    def test_invalid_login(self):
        login_page = LoginPage()
        login_page.navigate_to_login_page()
        login_page.set_email("tmta@itfactory.ro")
        login_page.set_password("alabalaportocala")
        login_page.click_login_button()
        assert login_page.is_main_error_message_displayed()


