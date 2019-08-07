from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time


class DeleteMultipleArea(WithLogin):
    def test_multliple_area(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        check = browser.find_element_by_id("select_main").click()
        buttons = browser.find_element_by_css_selector("#btn_delete")
        buttons.click()
        time.sleep(5)
        punch_in = browser.find_element_by_css_selector(
            "button[class='swal-button swal-button--confirm swal-button--danger']").click()
        time.sleep(5)
        self.assertRaisesRegex(
            ValueError, "Las siguientes áreas no pudieron ser eliminadas porque hay zonas o usuarios asociados a ella")
