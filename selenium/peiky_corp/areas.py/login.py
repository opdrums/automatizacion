
import os
from test_utils import LoginUtil


class LoginUnittests(LoginUtil):
    def test_user_login(self):
        self.user_login("omar.perez@peiky.com", os.getenv('EMAIL_PASSWORD'))
        home = self.peiky.find_element_by_css_selector("a[href='/index']")
        self.assertIsNotNone(home)
