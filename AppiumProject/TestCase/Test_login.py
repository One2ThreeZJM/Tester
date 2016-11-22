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
	
	def test_login(self):
		'''正常登陆'''
		self.lp.input_account('19900000001')
		self.lp.input_password('123456789')
		self.lp.click_login()
		time.sleep(2)
		self.assertTrue(self.lp.isLogin(),msg = '登录失败')

	def test_toggle(self):
		'''测试隐藏密码按钮'''
		temp = '1234567890'
		self.lp.input_password(temp)
		self.lp.click_toggle()
		self.assertEqual(self.lp.find_element(self.lp.edt_pwd_loc).text,temp) 
		
	def test_forgot(self):
		'''测试忘记密码按钮'''
		self.lp.click_forgot()
		self.assertEqual(self.lp.find_element(self.lp.title_loc).text,'找回密码')
		print('跳转到找回【找回密码】成功')

	def test_regist(self):
		'''测试注册按钮'''
		self.lp.click_regist()
		self.assertEqual(self.lp.find_element(self.lp.title_loc).text,'账户注册')
		print('跳转到找回【账户注册】成功')

	def tearDown(self):
		self.lp.quit()



if __name__ == '__main__':
	unittest.main()
		

