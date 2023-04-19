from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.opencart.com/admin/")

driver.implicitly_wait(10)

uname = driver.find_element("id", "input-username")
uname.send_keys("demo")


pwd = driver.find_element("id", "input-password")
pwd.send_keys("demo")


driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()


driver.close()