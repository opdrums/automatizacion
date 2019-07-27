from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time



peiky = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/chromedriver")
peiky.get("https://qa.peiky.com:9083/login")

login =  peiky.find_element_by_name ("email")
login.send_keys("omar.perez@peiky.com")

password =  peiky.find_element_by_name ("password")
password.send_keys("123456")
password.send_keys(Keys.ENTER)

peiky.find_element_by_css_selector("#menu-areas").click()

peiky.find_element_by_css_selector("a[href = '/areas/bulk']").click()

company = Select(peiky.find_element_by_id("company_id"))
company.select_by_value("6")

carga_multiple_areas = peiky.find_element_by_id("file")
carga_multiple_areas.send_keys("/home/omar/Descargas/areas (1).xlsx")

peiky.find_element_by_css_selector("button").click()

time.sleep(5)

search =  peiky.find_element_by_xpath("//input[@type ='search']")
search.send_keys("new1")
time.sleep(2)
search.clear()
time.sleep(2)
search.send_keys("new2")


time.sleep(3)

peiky.close()