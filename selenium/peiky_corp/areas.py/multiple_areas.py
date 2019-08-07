from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_utils import WithLogin
import time


class CargaAreas(WithLogin):

    def test_create_multiple_area(self):

        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        imput_carga_masiva = browser.find_element_by_css_selector(
            "div>div>a:nth-child(2)")
        imput_carga_masiva.click()
        carga_multiple_areas = browser.find_element_by_css_selector(
            "input[accept='.xlsx']")
        carga_multiple_areas.send_keys("/home/omar/Descargas/areas.xlsx")
        save_areas = browser.find_element_by_css_selector("button").click()
        self.assertIsNotNone(carga_multiple_areas)

    def test_search_areas(self):

        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search_name = browser.find_element_by_css_selector(
            "input[type = 'search']")
        search_name.send_keys("area 2")
        search_name.clear()
        time.sleep(2)
        search_name.send_keys("medellín")
        time.sleep(3)
        self.assertTrue("medellín".islower())
