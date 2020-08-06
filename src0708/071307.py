#coding = utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print (driver.title) # 把页面title 打印出来
print (driver.current_url) #打印url
driver.quit()

