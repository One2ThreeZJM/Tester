__author__ = 'ZhangJianMing'
import sys
sys.path.append("..")
from selenium.webdriver.common.by import By
from PO.BasePage import Base
import time

class HomePage(Base):
	"""docstring for HomePage"""	
	# btn_user_loc = (By.CLASS_NAME,"android.widget.RelativeLayout")

	search_loc = (By.ID,"com.yidejia.app.mall:id/ivSearch")
	mainphoto_loc =(By.ID,"com.yidejia.app.mall:id/ivNewsPhoto")
	btn_home_loc = (By.CLASS_NAME,"android.widget.RelativeLayout")

	btn_share_loc = (By.ID,"com.yidejia.app.mall:id/iv_toolbar_menu")
	btn_share_wechat = (By.ID,"com.yidejia.app.mall:id/tv_share_app_wechat")
	btn_share_sina = (By.ID,"com.yidejia.app.mall:id/tv_share_app_sina")
	btn_share_qq = (By.ID,"com.yidejia.app.mall:id/tv_share_app_qq")
	btn_share_qzone = (By.ID,"com.yidejia.app.mall:id/tv_share_app_qzone")
	btn_share_wechat_moments = (By.ID,"com.yidejia.app.mall:id/tv_share_app_wechat_moments")


	def click_home(self):
		self.find_elements(self.btn_home_loc)[-4].click()

	def click_search(self):
		self.clickBtn(self.search_loc)

	def click_mainphoto(self):
		self.clickBtn(self.mainphoto_loc)

	def click_share(self):
		self.clickBtn(self.btn_share_loc)

	def click_wechat(self):
		self.clickBtn(self.btn_share_wechat)

	def click_sina(self):
		self.clickBtn(self.btn_share_sina)

	def click_QQ(self):
		self.clickBtn(self.btn_share_qq)

	def click_qzone(self):
		self.clickBtn(self.btn_share_qzone)

	def click_wechatwechat_moments(self):
		self.clickBtn(self.btn_share_wechat_moments)		








