from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_utils import WithLogin
import time


class CargaAreas(WithLogin):

    def test_dowload_template(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        browser.find_element_by_css_selector(
            "div>div>a:nth-child(2)").click()
        select = browser.find_element_by_id("upload-excel").click()
        time.sleep(5)
        self.assertIsNone(select)

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
        mensage_alert = browser.find_element_by_css_selector(
            "div>h4").text
        self.assertEqual(
            mensage_alert, "¡Éxito!")

    def test_create_multiple_areas_adjunto_incorrect(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        browser.find_element_by_css_selector("div>a:nth-child(2)").click()
        division = browser.find_element_by_css_selector(
            "input[accept='.xlsx']")
        division.send_keys("/home/omar/Descargas/Aug 12, 2019 10_11 AM.webm")
        input_buttons = browser.find_element_by_css_selector(
            "button[type='submit']").click()
        time.sleep(5)
        mensage = browser.find_element_by_css_selector("div>h4").text
        self.assertEqual(mensage, "Error al cargar las áreas")

    def test_search_areas_created(self):

        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search_name = browser.find_element_by_css_selector(
            "input[type = 'search']")
        search_name.send_keys("area 2")
        name_area = browser.find_element_by_css_selector(
            "tr[class='even']>td:nth-child(2)").text
        self.assertEqual(name_zone.lower(), "area 2")
