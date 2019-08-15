from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time


class NewArea(WithLogin):

    def test_create_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(1)").click()
        division = browser.find_element_by_css_selector("#division_name")
        division.send_keys("ensayo areas6")
        browser.find_element_by_css_selector("button").click()
        mensage = browser.find_element_by_css_selector("div>h4").text
        self.assertEqual(mensage, "¡Éxito!")

    def test_create_areas_name_repeat(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(1)").click()
        division = browser.find_element_by_css_selector("#division_name")
        division.send_keys("ensayo areas2")
        browser.find_element_by_css_selector("button").click()
        mensage = browser.find_element_by_css_selector("div>h4").text
        self.assertEqual(mensage, "El área no puede ser creada")

    def test_search_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search = browser.find_element_by_css_selector("input[type='search']")
        search.send_keys("ensayo areas2")
        name_area = browser.find_element_by_css_selector(
            "tr>td:nth-child(2)").text
        time.sleep(3)
        self.assertEqual(name_area.lower(), "ensayo areas2")
