from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

peiky = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/driver/chromedriver")
peiky.get("https://qa.peiky.com:9083/login")

login = peiky.find_element_by_name("email")
login.send_keys("omar.perez@peiky.com")
# login.send_keys("omar.perez+12124@peiky.com")

password = peiky.find_element_by_name("password")
# password.send_keys("D0KXDU")
password.send_keys("123456")
password.send_keys(Keys.ENTER)
time.sleep(2)

peiky.find_element_by_css_selector("#menu-zonas").click()

peiky.find_element_by_css_selector("a[href='/zones/new']").click()


zones = peiky.find_element_by_id("division_name")
zones.send_keys("zona 53")

file_company = Select(peiky.find_element_by_id("division_company_id"))
file_company.select_by_value("6")

time.sleep(2)

file_company = Select(peiky.find_element_by_id("division_parent_id"))
file_company.select_by_value("54")

peiky.find_element_by_css_selector("button").click()



