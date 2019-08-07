from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time


class NewArea(WithLogin):
    def test_open_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        browser.find_element_by_css_selector("div>div>a:nth-child(1)").click()
        division = browser.find_element_by_css_selector("#division_name")
        division.send_keys("ensayo areas2")
        browser.find_element_by_css_selector("button").click()
        self.assertTrue(division)

    def test_search_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search = browser.find_element_by_xpath("//input[@type='search']")
        search.send_keys("ensayo areas2")
        search.clear()
        search.send_keys("area 1")
        self.assertTrue("ensayo areas2".islower())
        self.assertFalse("area 1".isupper())

    def test_dowload_template(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        browser.find_element_by_css_selector(
            "div>div>a:nth-child(2)").click()
        select = browser.find_element_by_id("upload-excel").click()
        time.sleep(5)
        self.assertIsNone(select)
