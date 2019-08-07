from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_utils import WithLogin
import time


class DeleteArea(WithLogin):
    def test_delete_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search = browser.find_element_by_css_selector("input[type = 'search']")
        search.send_keys("two")
        select_area = browser.find_element_by_css_selector(
            "input[class='select_row").click()
        time.sleep(2)
        delete_area = browser.find_element_by_css_selector(
            "a[class='btn btn-danger']").click()

        alert = browser.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        self.assertIsNone(delete_area, "Area eliminada correctamente.")
