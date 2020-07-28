import unittest
import os, sys
import time
import HTMLTestRunner

def createsuite():
    discovers = unittest.defaultTestLoader.discover("../src0409", pattern="Baidu*.py", top_level_dir=None)
    print(discovers)
    return discovers


if __name__=="__main__":

    #sys.path是python的搜索模块的路径集，返回的结果是一个list
    # curpath = sys.path[0]
    # print(sys.path)
    # print("====================")
    # print(sys.path[0])
    # if not os.path.exists(curpath+'/resultreport'):
    #     os.makedirs(curpath+'/resultreport')



    if not os.path.exists('./resultreport'):
         os.makedirs('./resultreport')
    #time.strftime(format[, t])
    #strftime作用是格式化时间戳为本地的时间
    #time()函数用于返回当前时间的时间戳（1970年01月08时00分00秒到现在的浮点秒数）
    #localtime()函数的作用是格式化时间戳为本地 struct_time。如果secs参数未输入则默认为当前时间
    #localtime()函数语法：time.localtime([secs])
    # //time指的是time模块,可选参数secs表示1970-1-1到现在的秒数

    # %Y%m%d-%H%M%S
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print("---------------------")
    print(time.time())
    print("---------------------")
    print(time.localtime(time.time()))
    print("---------------------")
    print(now)
    filename = curpath + '/resultreport/' + now + 'resultreport.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行结果",
                                              verbosity = 2)
        suite = createsuite()
        runner.run(suite)
