from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from selenium.common.exceptions import NoSuchElementException
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

# for x in range(1):
#     try:
#         peiky.find_element_by_xpath("//input[@type = 'checkbox']").click()
#         break
#     except NoSuchElementException as e:
#         print("retry")
#         time.sleep(1)
# else:
#     print('check failed')

time.sleep(5)

peiky.close()