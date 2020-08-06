# coding = utf-8
from selenium import webdriver
import time #调入time 函数
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.implicitly_wait(30) #智能等待30秒
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()