__author__ = 'ZhangJianMing'

import sys
sys.path.append("..")
from PO.LoginPage import LoginPage
from common import AppiumDriver
import time,unittest

class Login(unittest.TestCase):
	"""docstring for Login"""
	def setUp(self):
		driver = AppiumDriver.driver_mall()
		self.lp = LoginPage(driver)
		time.sleep(5)
		self.lp.click_user()
		if self.lp.isLogin():
			self.lp.login_out()
		
		self.assertEqual(self.lp.page_title(),'登录',msg = '跳转到登录页面失败')
	
	# def test_login(self):
	# 	'''正常登陆'''
	# 	self.lp.input_account('19900000001')
	# 	self.lp.input_password('1234567890')
	# 	self.lp.click_login()
	# 	time.sleep(2)
	# 	self.assertTrue(self.lp.isLogin(),msg = '登录失败')

	def test_toggle(self):
		print(self.lp.find_element(self.lp.btn_toggle_loc)[0].get_attribute('name'))
		# self.lp.click_toggle()
		# print(self.lp.find_element(self.lp.btn_toggle_loc).get_attribute('text'))
		# self.lp.click_toggle()
		

	# def test_switch(self):
	# 	self.lp.click_switch()
	# 	self.lp.take_Shot('保持登录状态开')
	# 	time.sleep(1)
	# 	self.lp.click_switch()
	# 	self.lp.take_Shot('保持登录状态关')

	# def test_forgot(self):
	# 	self.lp.click_forgot()
	# 	self.lp.take_Shot('找回密码页面')

	# def test_regist(self):
	# 	self.lp.click_regist()
	# 	self.lp.take_Shot('注册页面')

	def tearDown(self):
		self.lp.quit()



if __name__ == '__main__':
	unittest.main()
		

