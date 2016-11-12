__author__ = 'ZhangJianMing'

import sys
sys.path.append("..")
import unittest
from PO.LoginPage import LoginPage
from appium import webdriver
import time


class Login(unittest.TestCase):
	"""测试登录失败情况"""
	def setUp(self):
		desired_caps = {}
		desired_caps['device'] = 'android'
		desired_caps['platformName'] = 'android'
		desired_caps['platformVersion'] = '6.0.1'
		desired_caps['deviceName'] = '255f4e4c'
		desired_caps['appPackage'] = 'com.yidejia.app.mall'
		desired_caps['appActivity'] = 'com.yidejia.app.mall.ui.WelcomeActivity'
		
		# desired_caps['deviceName'] = 'emulator-5554'
		# desired_caps['appPackage'] = 'com.yidejia.teacher'
		# desired_caps['appActivity'] = '.ui.MainActivity'
		# desired_caps['appPackage'] = 'com.android.calculator2'
		# desired_caps['appActivity'] = '.Calculator'	
		# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
		
		time.sleep(5)
		self.lp = LoginPage(driver)

		self.temp = [['',''],['19900000001',''],['','ydj998'],['1990000000','12345'],['19900000002','123456'],
		['19900000001','123456 7'],['199000000 2','123456']]

	def test_login_fail(self):
		'''测试登录功能'''
		self.lp.click_user()
		self.assertEqual(self.lp.page_title(),'登录')

		for x in self.temp:
			self.lp.input_account(x[0])
			self.lp.input_password(x[1])
			self.lp.click_login()
			self.assertEqual(self.lp.page_title(),'登录')

	def test_login_success(self):
		'''测试登录功能'''
		self.lp.click_user()
		self.assertEqual(self.lp.page_title(),'登录')

		self.lp.input_account('19900000001')
		self.lp.input_password('123456789')
		self.lp.click_login()
		self.assertEqual(self.lp.page_title(),'NotFound')
		


	def tearDown(self):
		self.lp.quit()
		# print('test_login_fail_tearDown')

