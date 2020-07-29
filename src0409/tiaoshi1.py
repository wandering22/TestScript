# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt, unpack, data, file_data
import sys, csv
import os


def getCsv(file_name):
    rows=[]
    path=sys.path[0].replace('\test', '')
    print(path)
    with open(path+'/data/'+file_name, 'rt', encoding='gbk') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows=[]
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

@ddt    # 引入数据驱动
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors=[]
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    @data(*getCsv('test_baidu_data.txt'))
    @unpack
    def test_hao(self,value,expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(4)
        self.assertEqual(expected_value, driver.title)
        print(expected_value)
        print(driver.title)
if __name__ == "__main__":
    unittest.main()