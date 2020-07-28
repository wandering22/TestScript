# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
import os
import re
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


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
    # @unittest.skip("skipping")
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        # 判断打开的网址是否是百度
        # self.assertEqual(driver.title, "百度一下", msg="Not equal!")
        # self.assertNotEqual(driver.title, "百度一下，你就知道", msg="122344")
        try:
            self.assertTrue("123456" == "12345", msg="Not equal!!!")
        except:
        #     错误截图
            self.saveScreenShot(driver, "baidu.png")

        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"大虞海棠")
        driver.find_element_by_id("su").click()
        time.sleep(6)

    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url)
        # driver.find_element_by_link_text("hao123").click()
        driver.maximize_window()
        time.sleep(6)
        try:
            print(driver.title)
            self.assertEqual(u"hao123_上网从这里开始", driver.title)
        except:
            self.saveScreenShot(driver, "hao.png")
        # self.assertTrue("admin"=="admin1",msg="12345")
        # self.assertFalse("admin"=="admin1",msg="12345")
        # self.assertNotEqual("admin","admin1", msg="12345")
        time.sleep(8)
    #截图
    def saveScreenShot(self, driver, file_name):
        if not os.path.exists("./errorImage"):
            os.makedirs("./errorImage")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        print("---------------")
        print(time.time())
        print(time.localtime(time.time()))
        print(now)
        driver.get_screenshot_as_file("./errorImage/"+now+"-"+file_name)
        time.sleep(3)

    # 判断element是否存在，可删除
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    # 判断alert是否存在，可删除
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True
    # 关闭alert，可删除
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    if __name__ == "__main__":
        unittest.main()