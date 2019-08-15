from test_utils import WithLogin
import unittest
import time


class DeleteZone(WithLogin):
    def tests_delete_one_zone(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector("input[type='search']")
        search.send_keys("pruebaa")
        delete_zone = browser.find_element_by_css_selector(
            "a[class='btn btn-danger']").click()
        time.sleep(2)
        alert = browser.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        mensage = browser.find_element_by_css_selector(
            "div>h4").text
        self.assertEqual(mensage, "Información")

    def tests_delete_multiples_zone(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        paginador = browser.find_element_by_css_selector(
            "span > a:nth-child(2)")
        paginador.click()
        time.sleep(2)
        check = browser.find_elements_by_css_selector(
            "input[class='select_row']")
        if len(check) > 0:
            check[5].click()
            check[6].click()
            check[7].click()
        input_delete = browser.find_element_by_css_selector(
            "#btn_delete").click()
        time.sleep(2)
        comfirmation_delete = browser.find_element_by_css_selector(
            "button[class='swal-button swal-button--confirm swal-button--danger']")
        comfirmation_delete.click()
        time.sleep(3)
        buttons = browser.find_element_by_css_selector(
            "div>button[class='swal-button swal-button--confirm']")
        buttons.click()
        time.sleep(3)
        self.assertTrue(buttons)

    def test_delete_zone_mensage_validation(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        search = browser.find_element_by_css_selector("input[type='search']")
        search.send_keys("Soachad")
        delete_zone = browser.find_element_by_css_selector(
            "a[class='btn btn-danger']").click()
        time.sleep(2)
        alert = browser.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        self.assertRaisesRegex(
            ValueError, "La zona no puede ser eliminada porque hay líderes o usuarios asociados a ella")

    def test_delete_multiple_zona_mensage_validation(self):
        browser = self.peiky
        browser.find_element_by_css_selector("#menu-zonas").click()
        check_box = browser.find_element_by_css_selector(
            "#select_main").click()
        input_delete = browser.find_element_by_css_selector(
            "#btn_delete").click()
        time.sleep(2)
        comfirmation_delete = browser.find_element_by_css_selector(
            "button[class='swal-button swal-button--confirm swal-button--danger']")
        comfirmation_delete.click()
        time.sleep(3)
        buttons = browser.find_element_by_css_selector(
            "div>button[class='swal-button swal-button--confirm']")
        mensage = browser.find_element_by_css_selector(
            "div[class='swal-title']").text
        time.sleep(3)
        self.assertEqual(
            mensage, "Las siguientes zonas no pudieron ser eliminadas porque hay líderes o usuarios asociados a ella")
