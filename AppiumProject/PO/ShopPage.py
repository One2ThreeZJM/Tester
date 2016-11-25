__author__ = 'ZhangJianMing'
import sys
sys.path.append("..")
from selenium.webdriver.common.by import By
from PO.BasePage import Base
import time

class ShopPage(Base):
	"""docstring for ShopPage"""
	#走马灯
	banner_loc = (By.ID,"com.yidejia.app.mall:id/iv_banner")
	#我的订单、类目、活动馆、手机充值、消息中心、伊日惠、积分卡券、肌肤测试
	shortcut_loc =(By.ID,"com.yidejia.app.mall:id/iv_shortcut")
	
	#伊日惠
	yirihui_loc =(By.ID,"com.yidejia.app.mall:id/iv_yirihui") 
	hot_sell_top_loc =(By.ID,"com.yidejia.app.mall:id/iv_hot_sell_top")
	hot_sell_bottom_loc =(By.ID,"com.yidejia.app.mall:id/iv_hot_sell_bottom")
	
	#美妆城布局ID
	rl_djdzm_title_loc = (By.ID,"com.yidejia.app.mall:id/rl_djdzm_title")
	djdzm_left_loc = (By.ID,"com.yidejia.app.mall:id/iv_djdzm_left")
	djdzm_right_top_loc = (By.ID,"com.yidejia.app.mall:id/iv_djdzm_right_top")
	djdzm_right_bottom_loc = (By.ID,"com.yidejia.app.mall:id/iv_djdzm_right_bottom")

	#时装城布局ID
	rl_szc_title_loc = (By.ID,"com.yidejia.app.mall:id/rl_szc_title")
	szc_top_left_loc = (By.ID,"com.yidejia.app.mall:id/iv_szc_top_left")
	szc_top_right_loc = (By.ID,"com.yidejia.app.mall:id/iv_szc_top_right")
	szc_bottom_left_loc = (By.ID,"com.yidejia.app.mall:id/iv_szc_bottom_left")
	iszc_bottom_mid_loc = (By.ID,"com.yidejia.app.mall:id/iv_szc_bottom_mid")
	iszc_bottom_right_loc = (By.ID,"com.yidejia.app.mall:id/iv_szc_bottom_right")

	#随心逛布局ID
	sxg_top_loc = (By.ID,"com.yidejia.app.mall:id/iv_sxg_top")
	sxg_left_loc = (By.ID,"com.yidejia.app.mall:id/iv_sxg_left")
	sxg_right_top_loc = (By.ID,"com.yidejia.app.mall:id/iv_sxg_right_top")
	sxg_right_bottom_loc = (By.ID,"com.yidejia.app.mall:id/iv_sxg_right_bottom")

	search_loc = (By.CLASS_NAME,"android.widget.TextView")
	btn_shop_loc = (By.CLASS_NAME,"android.widget.RelativeLayout")

	#以下内容用于assertEqual
	#搜索页面按钮
	btn_search_loc = (By.ID,"com.yidejia.app.mall:id/tv_search")
	edt_search_loc = (By.ID,"com.yidejia.app.mall:id/edt_search")
	goods_type_name_loc = (By.ID,"com.yidejia.app.mall:id/goods_type_name")
	image_loc = (By.ID,"com.yidejia.app.mall:id/iv_image")
	view_loc =(By.CLASS_NAME,"android.view.View")
	#跳转页面后的页面title ID基本一致
	toolbar_title_loc = (By.ID,"com.yidejia.app.mall:id/tv_toolbar_title")


	def click_shop(self):
		self.find_elements(self.btn_shop_loc)[-3].click()

	def click_search(self):
		testview = self.find_elements(self.search_loc)
		for x in testview:
			if x.text == '搜索伊的家的商品':
				x.click()
				break

	def page_title(self):
		return self.find_element(self.toolbar_title_loc).text

	#点击走马灯
	def click_banner(self):
		self.clickBtn(self.banner_loc)

	#点击按钮我的订单、类目、活动馆、手机充值、消息中心、伊日惠、积分卡券、肌肤测试
	def click_myOrders(self):
		self.find_elements(self.shortcut_loc)[0].click()
	def click_category(self):
		self.find_elements(self.shortcut_loc)[1].click()
	def click_activities(self):
		self.find_elements(self.shortcut_loc)[2].click()
	def click_phoneRecharge(self):
		self.find_elements(self.shortcut_loc)[3].click()
	def click_news(self):
		self.find_elements(self.shortcut_loc)[4].click()	
	def click_yirihui(self):
		self.find_elements(self.shortcut_loc)[5].click()		
	def click_pointsCard(self):
		self.find_elements(self.shortcut_loc)[6].click()
	def click_skinTest(self):
		self.find_elements(self.shortcut_loc)[7].click()
	
	def click_Btnyirihui(self):
		self.clickBtn(self.yirihui_loc)
	def click_hot_sell_top(self):
		self.clickBtn(self.hot_sell_top_loc)	
	def click_hot_sell_top(self):
		self.clickBtn(self.hot_sell_top_loc)
	def click_hot_sell_bottom(self):
		self.clickBtn(self.hot_sell_bottom_loc)
	
	#美妆城按钮点击
	def click_rl_djdzm_title(self):
		self.clickBtn(self.rl_djdzm_title_loc)
	def click_djdzm_left(self):
		self.clickBtn(self.djdzm_left_loc)
	def click_djdzm_right_top(self):
		self.clickBtn(self.djdzm_right_top_loc)
	def click_djdzm_right_bottom(self):
		self.clickBtn(self.djdzm_right_bottom_loc)
	
	#时装城按钮点击
	def click_rl_szc_title(self):
		self.clickBtn(self.rl_szc_title_loc)
	def click_szc_top_left(self):
		self.clickBtn(self.szc_top_left_loc)
	def click_szc_top_right(self):
		self.clickBtn(self.szc_top_right_loc)
	def click_szc_bottom_left(self):
		self.clickBtn(self.szc_bottom_left_loc)
	def click_iszc_bottom_mid(self):
		self.clickBtn(self.iszc_bottom_mid_loc)
	def click_iszc_bottom_right(self):
		self.clickBtn(self.iszc_bottom_right_loc)		

	#随心逛按钮点击
	def click_sxg_top(self):
		self.clickBtn(self.sxg_top_loc)
	def click_sxg_left(self):
		self.clickBtn(self.sxg_left_loc)
	def click_sxg_right_top(self):
		self.clickBtn(self.sxg_right_top_loc)
	def click_sxg_right_bottom(self):
		self.clickBtn(self.sxg_right_bottom_loc)

	def click_btn_search(self):
		self.clickBtn(self.btn_search_loc)
	
	def input_search(self,value):
		self.send_keys(self.edt_search_loc,value)

	def searchpage_Title(self):
		return self.find_element(self.edt_search_loc).text

	def has_image(self):
		if self.find_element(self.image_loc):
			return True
		else:
			return False

	def has_goods_type(self):
		if self.find_elements(self.goods_type_name_loc):
			return True
		else:
			return False

	def has_data(self):
		for x in self.find_elements(self.view_loc):
			if len(x.get_attribute('name')) > 0:
				return True
		return False
			

	
	