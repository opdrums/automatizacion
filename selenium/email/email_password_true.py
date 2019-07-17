# from selenium import webdriver , import = import el module, from = framework

from selenium import webdriver 

# from selenium.webdriver.common.keys import Keys, keys =  directorio o ruta, Keys = modulo

from selenium.webdriver.common.keys import Keys
import time #secuencia  de carga de pc para abrir una pagina web 

#executable_path = para poner la ruta  del browser

web = webdriver.Chrome(executable_path=r"/home/omar/Escritorio/driver/chromedriver")
web.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1562893982&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dd18a3efe-ac60-de27-aed8-87d58b9ca8c1&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")

user = web.find_element_by_id("i0116")
user.send_keys("mono_124@hotmail.com")
user.send_keys(Keys.ENTER)
time.sleep(3) # tiempo para recargar nuestra pagina 

password = web.find_element_by_name("passwd")
password.send_keys("piano@3")
password.send_keys(Keys.ENTER)

time.sleep(3)

web.close()
