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
        select_edit = browser.find_element_by_css_selector(
            "a[class = 'btn btn-warning']")
        select_edit.click()
        name_area = browser.find_element_by_css_selector("#division_name")
        name_area.clear()
        name_area.send_keys("prueba peiky2")
        buttons = browser.find_element_by_css_selector("button").click()
        time.sleep(2)
        mensage = browser.find_element_by_css_selector("div>h4").text
        self.assertEqual(mensage, "¡Éxito!")

    def test_search_area(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search_name = browser.find_element_by_css_selector(
            "input[type = 'search']")
        search_name.send_keys("prueba peiky")
        name_area = browser.find_element_by_css_selector(
            "tr>td:nth-child(2)").text
        time.sleep(3)
        self.assertEqual(name_area.lower(), "prueba peiky")

    def test_search_area_not_found(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search = browser.find_element_by_css_selector(
            "input[type='search']")
        search.send_keys("not found")
        result_search = browser.find_element_by_css_selector("tr>td").text
        time.sleep(2)
        self.assertEqual(result_search, "Sin resultados encontrados")
