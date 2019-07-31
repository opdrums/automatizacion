from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_utils import WithLogin
import time


class DeleteArea(WithLogin):
    def test_delete_areas(self):
        self.peiky.find_element_by_css_selector("#menu-areas").click()
        search = self.peiky.find_element_by_xpath("//input[@type='search']")
        search.send_keys("Wwwww")
        select_area = self.peiky.find_element_by_css_selector(
            "input[class='select_row").click()
        time.sleep(2)
        delete_area = self.peiky.find_element_by_css_selector(
            "a[class='btn btn-danger']").click()

        alert = self.peiky.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        self.assertTrue(search)
