from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from test_utils import WithLogin
import time


class DeleteArea(WithLogin):
    def test_delete_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        search = browser.find_element_by_css_selector("input[type = 'search']")
        search.send_keys("Nuevas Zonas232")
        time.sleep(2)
        delete_area = browser.find_element_by_css_selector(
            "a[class='btn btn-danger']").click()
        alert = browser.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        mensage = browser.find_element_by_css_selector("div>h4").text
        self.assertEqual(mensage, "Información")

    def test_delete_multiple_areas(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        paginador = browser.find_element_by_css_selector(
            "span > a:nth-child(4)").click()
        time.sleep(2)
        check = browser.find_elements_by_css_selector(
            "input[class='select_row']")
        if len(check) > 0:
            check[0].click()
            check[1].click()
        input_delete = browser.find_element_by_css_selector(
            "#btn_delete").click()
        time.sleep(2)
        comfirmation_delete = browser.find_element_by_css_selector(
            "button[class='swal-button swal-button--confirm swal-button--danger']")
        comfirmation_delete.click()
        time.sleep(3)
        mensage = browser.find_element_by_css_selector(
            "div[class='swal-text']").text
        time.sleep(3)
        self.assertEqual(mensage, "Se borraron todos los areas seleccionados")

    def test_delete_multliple_areas_first_opcion(self):

        browser = self.peiky
        browser.find_element_by_css_selector("#menu-areas").click()
        check = browser.find_element_by_id("select_main").click()
        buttons = browser.find_element_by_css_selector("#btn_delete")
        buttons.click()
        time.sleep(5)
        punch_in = browser.find_element_by_css_selector(
            "button[class='swal-button swal-button--confirm swal-button--danger']").click()
        time.sleep(5)
        self.assertRaisesRegex(
            ValueError, "Las siguientes áreas no pudieron ser eliminadas porque hay zonas o usuarios asociados a ella")
