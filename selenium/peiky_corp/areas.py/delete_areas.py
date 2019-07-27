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

search =  peiky.find_element_by_xpath("//input[@type='search']")

search.send_keys("one ")

time.sleep(2)

delete_area = peiky.find_element_by_css_selector("a[ href ='/areas/547']").click()

time.sleep(2)

alert = peiky.switch_to.alert #metodo para controlar los pop up de chrone

time.sleep(2)

alert.accept()

time.sleep(2)

peiky.close()