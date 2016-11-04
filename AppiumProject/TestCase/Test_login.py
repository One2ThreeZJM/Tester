__author__ = 'ZhangJianMing'

import sys
sys.path.append("..")
import unittest
from PO.LoginPage import LoginPage
from appium import webdriver
import time


class Login(unittest.TestCase):
	"""docstring for Login"""
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
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
		
		time.sleep(5)
		self.lp = LoginPage(driver)

		self.temp = [['',''],['1',''],['','1'],['12345678911','12345'],['123456789123','123456']]

	def test_login_fail(self):
		'''测试登录功能'''
		self.lp.click_user()
		self.assertEqual(self.lp.page_title(),'登录')

		for x in self.temp:
			self.lp.input_account(x[0])
			self.lp.input_password(x[1])
			self.lp.click_login()
			self.assertEqual(self.lp.page_title(),'登录')

		

		


	
	def tearDown(self):
		self.lp.quit()

if __name__ == '__main__':
	unittest.main()