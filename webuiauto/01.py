from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost/ecshop/admin/index.php")
time.sleep(5)