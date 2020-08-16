# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('E:\\PycharmProjects\\alert.html')
dr.get(file_path)
# 点击链接弹出alert
dr.find_element_by_id('tooltip').click()
sleep(2)
alert = dr.switch_to.alert()
alert.accept()
sleep(2)
dr.quit()


#接受警告信息
alert = dr.switch_to_alert()
alert.accept()
#得到文本信息打印
alert = dr.switch_to_alert()
print(alert.text)
#取消对话框（如果有的话）
alert = dr.switch_to.alert()
alert.dismiss()
#输入值
alert = dr.switch_to.alert()
alert.send_keys("hello word")