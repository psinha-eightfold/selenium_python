#Zoho login

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.zoho.com/forms/signup.html")

cname = driver.find_element(By.ID, "portalcompanyname")
cname.send_keys("Eightfold")
time.sleep(2)

email = driver.find_element(By.ID, "email")
email.send_keys("priyank@gmail.com")
time.sleep(2)

pwd = driver.find_element(By.ID, "password")
pwd.send_keys("Eightfold")
time.sleep(2)

mob = driver.find_element(By.ID, "rmobile")
mob.send_keys("9778562353")

agr = driver.find_element(By.ID, "signup-termservice").click()
time.sleep(2)

sign = driver.find_element(By.ID, "signupbtn").click()

time.sleep(3)

driver.close()