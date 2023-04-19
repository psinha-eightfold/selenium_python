from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://cdn3.digialm.com/EForms/configuredHtml/1936/81584/login.html")
driver.implicitly_wait(5)

uname = driver.find_element("id", "userid")
uname.send_keys("demo")

pwd = driver.find_element("id", "confData")
pwd.send_keys("demo")
time.sleep(5)

fw = driver.find_element(By.ID, "finalSubmit_button").click()
time.sleep(30)



driver.close()