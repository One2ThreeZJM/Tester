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
	
	Avatar_loc = (By.ID,"com.yidejia.app.mall:id/ci_avatar")
	btn_login_out_loc = (By.ID,"com.yidejia.app.mall:id/tv_logout")

	btn_loginout_commit_loc = (By.ID,"com.yidejia.app.mall:id/md_buttonDefaultPositive")
	btn_lgoinout_cancel_loc = (By.ID,"com.yidejia.app.mall:id/md_buttonDefaultNegative")
	# title_userinfo_loc = (By.ID,"com.yidejia.app.mall:id/tv_toolbar_title")
	
	def click_user(self):
		'''应用启动默认在首页位置，需要点击用户按钮才到登录页面'''
		# print('点击个人信息按钮')
		self.find_elements(self.btn_user_loc)[-1].click()
		# print('跳转到：'+self.page_title()+'页面')

	def page_title(self):
		if self.find_element(self.title_loc):
			return self.find_element(self.title_loc).text
		else:
			return False

	def input_account(self,account):
		self.send_keys(self.edt_account_loc,account)

	def input_password(self,password):
		self.send_pwds(self.edt_pwd_loc,password)

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

	def isLogin(self):
		if self.find_element(self.Avatar_loc):
			return True
		else:
			return False

	def login_out(self):
		self.clickBtn(self.Avatar_loc)
		self.find_element(self.title_userinfo_loc)
		self.swipe_Up()
		self.clickBtn(self.btn_login_out_loc)
		self.clickBtn(self.btn_loginout_commit_loc)





