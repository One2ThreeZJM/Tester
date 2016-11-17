__author__ = 'ZhangJianMing'

import sys
sys.path.append("..")
from PO.LoginPage import LoginPage
from common import AppiumDriver
import time,unittest

class Login(unittest.TestCase):
	"""测试登录失败情况"""
	def setUp(self):
		driver = AppiumDriver.driver_mall()
		self.lp = LoginPage(driver)
		
	def test_login_fail(self):
		'''测试登录功能'''
		pass
		
	def tearDown(self):
		self.lp.quit()
		

