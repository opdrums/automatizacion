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

peiky.find_element_by_css_selector("a[href = '/areas/bulk']").click()

peiky.find_element_by_id("upload-excel").click()

time.sleep(3)

peiky.close()