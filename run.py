import  unittest
from BeautifulReport import BeautifulReport

from TestCase.test_api import Testapi
#创建一个测试执行计划
suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(Testapi))  #括号里面跟的是测试类

#unittest框架还可以生成html测试报告
BeautifulReport(suite).report(filename = "test_report",description = "unittest自动化生成的测试报告")