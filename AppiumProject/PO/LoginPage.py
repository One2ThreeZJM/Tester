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
		print('点击个人信息按钮')
		userbtn = self.find_elements(self.btn_user_loc)[-1].click()
		print('跳转到：'+self.find_element(self.title_loc).text+'页面')



	def login(self,account,pwd):
		self.click_user()
		self.send_keys(self.edt_account_loc,account,click_first=False)
		self.send_keys(self.edt_pwd_loc,pwd,click_first=False)
		self.clickBtn(self.btn_toggle_loc)
		self.clickBtn(self.btn_switch_loc)
		self.clickBtn(self.btn_login_loc)
		# 测试登录判断：输入不符合逻辑的account，能不能按登录键
		# 输入账号、密码。是否可以跳转。判断页面是否跳转、或者按钮能不能按
		# self.quit()

# desired_caps = {}
# desired_caps['device'] = 'android'
# desired_caps['platformName'] = 'android'
# desired_caps['platformVersion'] = '6.0.1'
# desired_caps['deviceName'] = '255f4e4c'
# desired_caps['appPackage'] = 'com.yidejia.app.mall'
# desired_caps['appActivity'] = 'com.yidejia.app.mall.ui.WelcomeActivity'
# # desired_caps['appPackage'] = 'com.yidejia.teacher'
# # desired_caps['appActivity'] = '.ui.MainActivity'	
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# lp = LoginPage(driver)
# time.sleep(5)
# lp.login('1000000000','222222')
