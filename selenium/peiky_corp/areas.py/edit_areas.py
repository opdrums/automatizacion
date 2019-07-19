from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

search = peiky.find_element_by_xpath("//input[@type = 'search']")

search.send_keys("prueba selenium")

time.sleep(2)

peiky.find_element_by_css_selector("a[href = '/areas/51/edit']").click()

area_name = peiky.find_element_by_id("division_name")
area_name.clear()
time.sleep(2)
area_name.send_keys("selenium prueba")

peiky.find_element_by_css_selector("button").click()

time.sleep(2)

peiky.find_element_by_css_selector("#menu-areas").click()

search = peiky.find_element_by_xpath("//input[@type = 'search']")
search.send_keys("selenium prueba")

time.sleep(2)

# search_edit = peiky.find_element_by_xpath("//input[@type = 'search']")
# search_edit.send_keys("prueba selenium")
# time.sleep(2)

peiky.close()