# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

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

    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("hao123").click()
        # self.assertEqual(u"hao123", driver.title)
        time.sleep(6)

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"隐秘的角落")
        driver.find_element_by_id("su").click()
        time.sleep(6)


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
    if __name__=="__main__":
        unittest.main()