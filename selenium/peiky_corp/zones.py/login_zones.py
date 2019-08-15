import os
import time
from test_utils import LoginUtil


class LoginUnittests(LoginUtil):
    def test_user_login(self):
        self.user_login("omar.perez@peiky.com", os.getenv('EMAIL_PASSWORD'))
        home = self.peiky.find_element_by_css_selector("a[href='/index']")
        self.assertIsNotNone(home)

    def test_login_incorrect(self):
        self.user_login("omar.perez@peiky.com", "false password")
        self.assertRaisesRegex(ValueError, "¡Error!")

    def test_password_recovery(self):
        browser = self.peiky
        recovery = browser.find_element_by_css_selector(
            "a[href='/pass/reset']")
        recovery.click()
        input_email = browser.find_element_by_css_selector(
            "input[type='email']")
        input_email.send_keys("oefperez1@gmail.com")
        input_buttons = browser.find_element_by_css_selector(
            "button[type='submit']")
        input_buttons.click()
        while self.assertTrue(input_buttons):
            browser.find_element_by_css_selector(
                "div[class='alert alert-success alert-dismissible']")
        time.sleep(3)
