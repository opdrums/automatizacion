from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time


class EditArea(WithLogin):
    def test_update_area(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search = browser.find_element_by_css_selector("input[type = 'search']")
        search.send_keys("prueba peiky2")
        time.sleep(2)

        select_edit = browser.find_element_by_css_selector(
            "a[class = 'btn btn-warning']")
        select_edit.click()
        name_area = browser.find_element_by_css_selector("#division_name")
        time.sleep(2)
        name_area.clear()
        name_area.send_keys("prueba peiky2")
        buttons = browser.find_element_by_css_selector("button").click()
        time.sleep(2)
        self.assertNotEqual("peiky 2", "prueba peiky2",
                            "Area actualizada correctamente.")

    def test_search_area(self):
        browser_1 = self.peiky
        browser_1.find_element_by_css_selector("#menu-areas").click()
        search_name = browser_1.find_element_by_css_selector(
            "input[type = 'search']")
        search_name.send_keys("prueba peiky")
        self.assertIsNotNone(search_name)
        time.sleep(5)
