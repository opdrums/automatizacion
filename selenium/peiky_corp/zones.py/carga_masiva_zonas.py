from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time

import unittest


class CargaMasivaZone(WithLogin):
    def test_dowload_zone(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(2)").click()
        upload = browser.find_element_by_css_selector(
            "a[class='btn btn-info']").click()
        time.sleep(5)
        self.assertIsNone(upload)

    def test_file_upload_error(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(2)").click()
        upload = browser.find_element_by_css_selector("input[accept='.xlsx']")
        upload.send_keys("/home/omar/Descargas/Aug 10, 2019 3_47 PM.webm")
        buttons = browser.find_element_by_css_selector(
            "button[type='submit']").click()
        time.sleep(5)
        self.assertRaisesRegex(
            ValueError, "Revise los errores listados a continuación")

    def test_upload_error_by_xlsx(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(2)").click()
        upload = browser.find_element_by_css_selector("input[accept='.xlsx']")
        upload.send_keys("/home/omar/Descargas/areas (2).xlsx")
        buttons = browser.find_element_by_css_selector(
            "button[type='submit']").click()
        time.sleep(5)
        self.assertRaisesRegex(ValueError, " Error al cargar las zonas")

    def test_create_carga_masiva(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(2)").click()
        create = browser.find_element_by_css_selector("input[accept='.xlsx']")
        create.send_keys("/home/omar/Descargas/zones.xlsx")
        buttons = browser.find_element_by_css_selector(
            "button[type='submit']").click()
        time.sleep(5)
        mensage_alert = browser.find_element_by_css_selector(
            "div>h4").text
        self.assertEqual(
            mensage_alert, "¡Éxito!")
