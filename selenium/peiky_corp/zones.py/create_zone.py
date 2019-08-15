from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import unittest
import time


class CreateZone(WithLogin):
    def test_create_zone(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(1)").click()
        zones = browser.find_element_by_css_selector("#division_name")
        zones.send_keys("zona 55")
        input_areas = browser.find_element_by_css_selector(
            "select>option:nth-child(2)")
        input_areas.click()
        time.sleep(2)
        browser.find_element_by_css_selector("button").click()
        mensage_alert = browser.find_element_by_css_selector(
            "div>h4").text
        self.assertEqual(
            mensage_alert, "¡Éxito!")

    def test_create_format_zone_incorrect(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(1)").click()
        zones = browser.find_element_by_css_selector("#division_name")
        zones.send_keys("zone_123**")
        browser.find_element_by_css_selector("button").click()
        time.sleep(2)
        self.assertIsNotNone(zones)

    def test_search_zone_created(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector(
            "input[type='search']")
        search.send_keys("Nuevas Zonas232")
        name_zone = browser.find_element_by_css_selector(
            "tr>td:nth-child(2)").text
        self.assertEqual(name_zone.lower(), "Nuevas Zonas232")
