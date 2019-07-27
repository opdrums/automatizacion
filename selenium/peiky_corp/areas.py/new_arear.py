from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

peiky = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/chromedriver")
peiky.get("https://qa.peiky.com:9083/login")

login = peiky.find_element_by_name("email")
login.send_keys("omar.perez@peiky.com")

password = peiky.find_element_by_name("password")
password.send_keys("123456")
password.send_keys(Keys.ENTER)
time.sleep(2)


peiky.find_element_by_css_selector("#menu-areas").click()

peiky.find_element_by_css_selector("a[href='/areas/new']").click()

division = peiky.find_element_by_id("division_name")
division.send_keys("pruebass2667")

file_company = Select(peiky.find_element_by_id("division_company_id"))
file_company.select_by_value("6")

peiky.find_element_by_css_selector("button").click()

#forma para buscar
search =  peiky.find_element_by_xpath("//input[@type='search']")

time.sleep(3)
search.send_keys("pruebass2667")

time.sleep(3)

search.clear()
search.send_keys("area 1")

time.sleep(5)

peiky.close()