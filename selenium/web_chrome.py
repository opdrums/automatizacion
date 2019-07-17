from selenium import webdriver

driver = webdriver.Chrome(executable_path= r"/home/omar/Escritorio/driver/chromedriver")

#driver.get() manda una solictud de la pagina web

driver.get("https://www.youtube.com/watch?v=18fxDASTmX0&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=4")
driver.get("https://selenium-python.readthedocs.io/installation.html")

#driver.close() cerrar la pagina

driver.close()