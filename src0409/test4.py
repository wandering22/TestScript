# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from ddt import ddt, unpack, data, file_data
import sys, csv


def getCsv(file_name):
    rows=[]
    path=sys.path[0]

    with open(path+'/data/'+file_name, 'rt') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows=[]
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows


@ddt
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors=[]
        self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    @file_data('test_baidu_data.json')
    #@data(*getCsv('test_baidu_data.txt'))
    #([周迅,周迅_百度搜索],[张国荣,张国荣_百度搜索])
    #@unpack
    #@data("王凯", "Lisa", "特朗普", "蒋欣")
    def test_baidu1(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)
        # self.assertEqual(driver.title, expected_value, msg="搜索结果和期望不一致")
        # time.sleep(3)

    @unittest.skip("skipping")
    @data(["Lsia", u"Lsia423432_百度搜索"], [u"双笙", u"双笙324_百度搜索"], ["999", u"999_百度搜索"])
    @unpack
    # @file_data('test_baidu_data.json')
    def test_baidu2(self, value, expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        driver.maximize_window()
        time.sleep(6)
        # 判断搜索网页的title和我们期望的是否一致
        self.assertEqual(expected_value, driver.title, msg="不一致！")
        print(expected_value)
        print(driver.title)

if __name__ == "__main__":
    unittest.main()