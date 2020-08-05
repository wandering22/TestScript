#coding=utf-8
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_partial_link_text("hao").click()
browser.quit()
