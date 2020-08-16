# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os
import selenium.webdriver.support.ui as ui
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('E:\\PycharmProjects\\modal.html')
dr.get(file_path)
# 打开对话框
dr.find_element_by_id('show_modal').click()
sleep(3)
# 点击对话框中的链接
link = dr.find_element_by_id('myModal').find_element_by_id('click')
link.click()
#dr.execute_script('$(arguments[0]).click()', link)
sleep(4)
# 关闭对话框
buttons =dr.find_element_by_class_name('modal-footer').find_elements_by_tag_name('button')
buttons[0].click()
sleep(2)
dr.quit()