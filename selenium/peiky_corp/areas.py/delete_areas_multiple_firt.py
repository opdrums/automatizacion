from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

peiky = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/driver/chromedriver")
peiky.get("https://qa.peiky.com:9083/login")

login = peiky.find_element_by_name("email")
login.send_keys("omar.perez@peiky.com")

password = peiky.find_element_by_name("password")
password.send_keys("123456")
password.send_keys(Keys.ENTER)
time.sleep(2)

peiky.find_element_by_css_selector("#menu-areas").click()

check = peiky.find_element_by_id("select_main")
check.click()

buttons = peiky.find_element_by_id("btn_delete")
buttons.click()

punch_in = peiky.find_element_by_xpath("//button[@class='swal-button swal-button--confirm swal-button--danger']").click()
time.sleep(5)

peiky.close()