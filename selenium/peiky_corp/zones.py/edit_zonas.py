from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time


class EditZone(WithLogin):
    def test_search_zone_by_name(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector(
            "input[type='search']")
        search.send_keys("nuevas zonas232")
        name_zone = browser.find_element_by_css_selector(
            "tr>td:nth-child(2)").text
        self.assertEqual(name_zone.lower(), "nuevas zonas232")

    def test_search_zone_by_company(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector(
            "input[type='search']")
        search.send_keys("nuevas zonas232")
        company_zone = browser.find_element_by_css_selector(
            "tr>td:nth-child(3)").text
        self.assertEqual(company_zone.lower(), "empresa prueba")

    def test_search_zone_not_found(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector(
            "input[type='search']")
        search.send_keys("not found")
        result_search = browser.find_element_by_css_selector("tr>td").text
        time.sleep(2)
        self.assertEqual(result_search, "Sin resultados encontrados")

    def test_edit_zone(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector("input[type='search']")
        search.send_keys("nuevas zonas23")
        edit_zone = browser.find_element_by_css_selector(
            "a[class='btn btn-warning']")
        edit_zone.click()
        new_zone = browser.find_element_by_css_selector(
            "input[class='form-control']")
        new_zone.clear()
        time.sleep(2)
        new_zone.send_keys("nuevas zonas232")
        buttons = browser.find_element_by_css_selector("button[type='submit']")
        buttons.click()
        time.sleep(5)
        mensage_alert = browser.find_element_by_css_selector(
            "div>h4").text
        self.assertEqual(
            mensage_alert, "¡Éxito!")
