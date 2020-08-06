#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("test")
time.sleep(2)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)
#通过submit() 来操作
driver.find_element_by_id("su").submit()
time.sleep(3)
driver.quit()