__author__ = 'ZhangJianMing'
import sys
sys.path.append("..")
from selenium.webdriver.common.by import By
from PO.BasePage import Base
import time

class HomePage(Base):
	"""docstring for HomePage"""	
	
	search_loc = (By.ID,"com.yidejia.app.mall:id/ivSearch")
	mainphoto_loc =(By.ID,"com.yidejia.app.mall:id/ivNewsPhoto")
	btn_home_loc = (By.CLASS_NAME,"android.widget.RelativeLayout")
	btn_share_loc = (By.ID,"com.yidejia.app.mall:id/iv_toolbar_menu")
	btn_share_wechat = (By.ID,"com.yidejia.app.mall:id/tv_share_app_wechat")
	btn_share_sina = (By.ID,"com.yidejia.app.mall:id/tv_share_app_sina")
	btn_share_qq = (By.ID,"com.yidejia.app.mall:id/tv_share_app_qq")
	btn_share_qzone = (By.ID,"com.yidejia.app.mall:id/tv_share_app_qzone")
	btn_share_wechat_moments = (By.ID,"com.yidejia.app.mall:id/tv_share_app_wechat_moments")
	edt_search = (By.ID,"com.yidejia.app.mall:id/edt_search")
	btn_toSearch_loc = (By.ID,"com.yidejia.app.mall:id/tv_search")
	imageview_loc = (By.CLASS_NAME,"android.widget.ImageView")

	txt_tvTitle_loc = (By.ID,"com.yidejia.app.mall:id/tvTitle")
	txt_tv_toolbar_title_loc = (By.ID,"com.yidejia.app.mall:id/tv_toolbar_title")

	share_loc = (By.CLASS_NAME,"android.widget.TextView")
	mainTestView_loc = (By.CLASS_NAME,"android.widget.TextView")

	text_loc = (By.CLASS_NAME,"android.view.View")
	
	def click_home(self):
		self.find_elements(self.btn_home_loc)[-4].click()

	def click_search(self):
		self.clickBtn(self.search_loc)

	def click_mainphoto(self):
		self.clickBtn(self.mainphoto_loc)

	def click_share(self):
		self.clickBtn(self.btn_share_loc)


	def click_toSearch(self):
		self.clickBtn(self.btn_toSearch_loc)

	def input_search(self,text):
		self.send_keys(self.edt_search,text)

	def has_imageview(self):
		if self.find_elements(self.imageview_loc):
			return True
		else:
			return False
	
	def returnContent(self):
		return self.find_element(self.txt_tvTitle_loc).text









