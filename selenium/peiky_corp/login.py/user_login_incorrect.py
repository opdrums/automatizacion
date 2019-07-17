from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

peiky = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/driver/chromedriver")
peiky.get("https://qa.peiky.com:9083/login")

login = peiky.find_element_by_name("email")
login.send_keys("omar.perez@peiky.com")

password = peiky.find_element_by_name("password")
password.send_keys("contraseña_false")
password.send_keys(Keys.ENTER)

time.sleep(2)

peiky.find_element_by_css_selector("a[href = '/pass/reset']").click()
forget_password = peiky.find_element_by_name("email")
forget_password.send_keys("omar.perez@peiky.com")
forget_password.send_keys(Keys.ENTER)

time.sleep(2)

peiky.close()