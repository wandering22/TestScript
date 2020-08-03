import HTMLTestRunner
import os
import sys
import time
import unittest

def createsuite():
    discovers = unittest.defaultTestLoader.discover("../src0409", pattern="Baidu*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__=="__main__":
    # sys.path是一个list
    curpath = sys.path[0]
    print(sys.path)
    print("==================")
    print(sys.path[0])
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')
    # 对时间格式化 time.strftime("格式化的形式", time.localtime<本地时间>(time.time()<获取时间戳>))
    # 为了生成的 HTML 报告名字不重复，引入时间戳的概念
    # 时间戳---time.time()
    # 将时间戳转化为本地的一个时间time.local.time(time.time())
    # 再将本地时间以 "%Y-%m-%d-%H %M:%S" 的形式输出
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print("=================================11111")
    print(time.time())
    print("=================================22222")
    print(time.localtime(time.time()))
    print("=========================")
    print(now)
    # 经过上述步骤，已经得到了 HTML 报告的名称
    filename = curpath + '/resultreport/'+now + 'resultreport.html'
    # 打开 HTML 文件, wb 以写的方式
    with open(filename, 'wb') as fp:
        # 括号里的参数是 HTML 报告里面的参数
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告",
                                               description=u"用例执行情况", verbosity=2)
        suite = createsuite()
        runner.run(suite)