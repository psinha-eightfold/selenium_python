from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https:\\www.gmail.com")

time.sleep(5)

driver.close()