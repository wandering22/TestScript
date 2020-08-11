#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入keys 包
import os,time
driver = webdriver.Chrome()
driver.get("http://demo.zentao.net/user-login-Lw==.html")
time.sleep(3)
driver.maximize_window() # 浏览器全屏显示
driver.find_element_by_id("account").clear()
time.sleep(3)
driver.find_element_by_id("account").send_keys("demo")
time.sleep(3)
#tab 的定位相当于清除了密码框的默认提示信息，等同上面的clear()
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(3)
#通过定位密码框，enter（回车）来代替登陆按钮
driver.find_element_by_name("password").send_keys(Keys.ENTER)
'''
#也可定位登陆按钮，通过enter（回车）代替click()
driver.find_element_by_id("login").send_keys(Keys.ENTER)
'''
time.sleep(3)
driver.quit()