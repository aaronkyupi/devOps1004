from selenium import webdriver
my_driver = webdriver.Chrome()
my_driver.get("C:/Users/aaronk/Desktop/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
# my_driver.find_element_by_id("musicamt").send_keys("2")
my_driver.find_element_by_id("calculate").click()
