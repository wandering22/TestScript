import unittest
import os, sys, csv
import time
from src0409 import Baidu1040601
from src0409 import Baidu204062


def createsuite():

    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(Baidu1040601.Baidu1))
    # suite.addTest(unittest.makeSuite(Baidu204062.Baidu1))
    # return suite



    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Baidu1040601.Baidu1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Baidu204062.Baidu1)
    # suite = unittest.TestSuite([suite1, suite2])
    # return suite


    discovers = unittest.defaultTestLoader.discover("../src0409", pattern="Baidu*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__=="__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
