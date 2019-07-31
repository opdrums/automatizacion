from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_utils import WithLogin


class NewArea(WithLogin):
    def test_open_areas(self):
        self.peiky.find_element_by_css_selector("#menu-areas").click()
        self.peiky.find_element_by_css_selector("a[href='/areas/new']").click()
        division = self.peiky.find_element_by_css_selector("#division_name")
        division.send_keys("ensayo areas2")
        self.peiky.find_element_by_css_selector("button").click()
        self.assertTrue(division)

    def test_search_areas(self):
        self.peiky.find_element_by_css_selector("#menu-areas").click()
        search = self.peiky.find_element_by_xpath("//input[@type='search']")
        search.send_keys("ensayo areas2")
        search.clear()
        search.send_keys("area 1")
        self.assertTrue("ensayo areas2".islower())
        self.assertFalse("area 1".isupper())

    def test_dowload_template(self):
        self.peiky.find_element_by_css_selector("#menu-areas").click()
        self.peiky.find_element_by_css_selector(
            "a[href = '/areas/bulk']").click()
        self.peiky.find_element_by_id("upload-excel").click()
