from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
email = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/driver/chromedriver")
email.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1562896354&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fRpsCsrfState%3dd18a3efe-ac60-de27-aed8-87d58b9ca8c1&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")

user = email.find_element_by_id("i0116")
user.send_keys("mono_124@hotmail.com")
user.send_keys(Keys.ENTER)
time.sleep(5)

password = email.find_element_by_name("passwd")
password.send_keys("falso123")
password.send_keys(Keys.ENTER)

email.close()