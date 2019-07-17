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


peiky.find_element_by_css_selector("#menu-archivos").click()

peiky.find_element_by_css_selector("a[href='/files/new']").click()

file_name = peiky.find_element_by_id("file_name")
file_name.send_keys("prueba multimedia_3")

file_description = peiky.find_element_by_id("file_description")
file_description.send_keys("hola prueba selenium")

file_company = Select(peiky.find_element_by_id("file_company_id"))
file_company.select_by_value("6")

time.sleep(2)

file_category = Select(peiky.find_element_by_id("file_file_category_id"))
file_category.select_by_value("3")

file_share = Select(peiky.find_element_by_id("file_shareable"))
file_share.select_by_value("false")

#selecionando class div
# file_multimedia = peiky.find_element_by_xpath("//div[contains(@class, 'box-btn-file')]")

#adjuntar multimedia
#file_only_first_multi
file_multimedia = peiky.find_element_by_id("file_multimedia")
file_multimedia.send_keys("/home/omar/Descargas/WhatsApp Image 2019-06-28 at 3.25.19 PM.jpeg")

#delete_multimedia
# delete_multimedia = peiky.find_element_by_css_selector("i[class = 'fa fa-trash clean-file']").click()

#guardar y compartir
#areas

select_areas = peiky.find_element_by_css_selector("#area_select span.selection ul li input.select2-search__field").click()
select_areas = peiky.find_elements_by_css_selector("#select2-file_area_ids-results li")[0].click()

time.sleep(2)

select_zones = peiky.find_element_by_css_selector("#zone_select span.selection ul li input.select2-search__field").click()
select_zones = peiky.find_elements_by_css_selector("#select2-file_zone_ids-results li")[0].click()

time.sleep(2)

select_leader = peiky.find_element_by_css_selector("#leader_select span.selection ul li input.select2-search__field").click()
select_leader = peiky.find_elements_by_css_selector("#select2-file_leader_ids-results li")[0].click()

time.sleep(2)

select_leader = peiky.find_element_by_css_selector("#role_select span.selection ul li input.select2-search__field").click()
select_leader = peiky.find_elements_by_css_selector("#select2-file_role_ids-results li")[4].click()

peiky.find_element_by_css_selector("button").click()
# peiky.find_element_by_css_selector("#area_select span.selection ul li[title]")

time.sleep(2)

peiky.close()