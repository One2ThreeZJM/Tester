__author__ = 'ZhangJianMing'

import unittest
from common import HTMLTestRunner
import time
import os

case_path = '.\\TestCase\\'
result = "..\\Result\\"

def Creatsuit():
	#将测试用例加入测试容器中
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)
	for test_suite in discover:
		for casename in test_suite:
			testunit.addTest(casename)
	return testunit

test_case = Creatsuit()

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

tdresutl = result + day

if os.path.exists(tdresutl):
	filename = tdresutl + "\\" + now +"_result.html"
	fp = open(filename,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u'Appium测试报告',description=u'用例详情：')
	runner.run(test_case)
	fp.close()
else:
	os.makedirs(tdresutl)
	filename = tdresutl + "\\" + now + "_result.html"
	fp = open(filename,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u'Appium测试报告',description=u'用例详情：')
	runner.run(test_case)
	fp.close()




