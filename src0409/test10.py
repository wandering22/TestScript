import unittest
from src0409 import Baidu1040601
from src0409 import Baidu204062

def createsuite():
    suite = unittest.TestSuite()
    #将测试用例加入到测试容器（套件）中
    suite.addTest(Baidu204062.Baidu1("test_baidusearch"))
    suite.addTest(Baidu1040601.Baidu1("test_hao"))
    suite.addTest(Baidu1040601.Baidu1("test_baidusearch"))
    return suite

if __name__=="__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
