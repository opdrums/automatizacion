from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os


class WithSelenium(unittest.TestCase):
    def setUp(self):
        self.peiky = webdriver.Chrome(
            executable_path=r"/home/omar/Escritorio/driver/chromedriver")
        self.peiky.implicitly_wait(5)
        self.peiky.get("https://qa.peiky.com:9083/login")


class LoginUtil(WithSelenium):
    def user_login(self, email, password):
        input_email = self.peiky.find_element_by_name("email")
        input_email.send_keys(email)

        input_password = self.peiky.find_element_by_name("password")

        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)


class WithLogin(LoginUtil):
    def setUp(self):
        super().setUp()
        self.user_login("omar.perez@peiky.com", os.getenv('EMAIL_PASSWORD'))
