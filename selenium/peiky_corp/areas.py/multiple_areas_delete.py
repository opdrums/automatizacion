from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils import WithLogin
import time


class MultipleArea(WithLogin):
    def test_delete_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        paginador = browser.find_element_by_css_selector(
            "span > a:nth-child(2)")
        paginador.click()
        for x in range(1):
            check = browser.find_elements_by_class_name("select_row")
            if len(check) > 0:
                check[0].click()
                check[1].click()
                check[2].click()
        buttons = browser.find_element_by_id("btn_delete")
        buttons.click()
        time.sleep(5)
        punch_in = browser.find_element_by_xpath(
            "//button[@class='swal-button swal-button--confirm swal-button--danger']")
        punch_in.click()
        comfirmacion_areas = browser.find_element_by_css_selector(
            "div > button[class='swal-button swal-button--confirm']")
        comfirmacion_areas.click()
        time.sleep(5)
        self.assertTrue(comfirmacion_areas)
