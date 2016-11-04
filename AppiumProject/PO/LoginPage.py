__author__ = 'ZhangJianMing'
import sys
sys.path.append("..")
from selenium.webdriver.common.by import By
from PO.BasePage import Base
import time

class LoginPage(Base):
	"""docstring for login"""
	title_loc = (By.ID,"com.yidejia.app.mall:id/tv_toolbar_title")
	edt_account_loc = (By.ID,"com.yidejia.app.mall:id/edt_account")
	edt_pwd_loc = (By.ID,"com.yidejia.app.mall:id/edt_password")
	btn_toggle_loc = (By.ID,"com.yidejia.app.mall:id/text_input_password_toggle")
	btn_forgot_loc = (By.ID,"com.yidejia.app.mall:id/tv_forgot_password")
	btn_switch_loc = (By.ID,"com.yidejia.app.mall:id/switch_login_status")
	btn_login_loc = (By.ID,"com.yidejia.app.mall:id/btn_login_now")
	btn_regist_loc = (By.ID,"com.yidejia.app.mall:id/tv_toolbar_menu")
	
	btn_user_loc = (By.CLASS_NAME,"android.widget.RelativeLayout")
	
	def click_user(self):
		'''应用启动默认在首页位置，需要点击用户按钮才到登录页面'''
		# print('点击个人信息按钮')
		self.find_elements(self.btn_user_loc)[-1].click()
		# print('跳转到：'+self.page_title()+'页面')

	def page_title(self):
		return self.find_element(self.title_loc).text

	def input_account(self,account):
		self.send_keys(self.edt_account_loc,account,click_first=False)

	def input_password(self,password):
		self.send_keys(self.edt_pwd_loc,password,click_first=False)

	def click_toggle(self):
		self.clickBtn(self.btn_toggle_loc)

	def click_switch(self):
		self.clickBtn(self.btn_switch_loc)

	def click_login(self):
		self.clickBtn(self.btn_login_loc)

	def click_forgot(self):
		self.clickBtn(self.btn_forgot_loc)

	def click_regist(self):
		self.clickBtn(self.btn_regist_loc)
	
		# 测试登录判断：输入不符合逻辑的account，能不能按登录键
		# 输入账号、密码。是否可以跳转。判断页面是否跳转、或者按钮能不能按
		# self.quit()

