__author__ = 'ZhangJianMing'

import sys
sys.path.append("..")

from PO.HomePage import HomePage
from common import AppiumDriver
import time,unittest


class Take_homepage(unittest.TestCase):
	"""docstring for TakeShot"""
	def setUp(self):
		driver = AppiumDriver.driver_mall()
		time.sleep(3)
		self.hp = HomePage(driver)

	def test_search(self):
		self.hp.click_search()
		time.sleep(3)
		self.hp.take_Shot("主页_搜索页面")

	# def test_mainphoto(self):
	# 	self.hp.click_mainphoto()
	# 	time.sleep(3)
	# 	self.hp.take_Shot("主页_主图文章")
		
	# 	self.hp.click_share()
	# 	self.hp.take_Shot("文章分享")

	# 	self.hp.click_wechat()
	# 	self.hp.take_Shot("微信分享")

	# 	self.hp.click_sina()
	# 	time.sleep(2)
	# 	self.hp.take_Shot("微博分享")
	# 	self.hp.dr_back()

	# 	self.hp.click_QQ()
	# 	time.sleep(2)
	# 	self.hp.take_Shot("QQ分享")
	# 	self.hp.dr_back()

	# 	self.hp.click_qzone()
	# 	self.hp.take_Shot("QQ空间分享")

	# 	self.hp.click_wechatwechat_moments()
	# 	self.hp.take_Shot("朋友圈分享")

	# def test_home(self):
	# 	self.hp.click_home()
	# 	self.hp.take_Shot("主页面")
		
	# 	self.hp.swipe_Up()
	# 	self.hp.take_Shot("主页面滑动1")

	# 	self.hp.swipe_Up()
	# 	self.hp.take_Shot("主页面滑动2")



	def tearDown(self):
		self.hp.quit()




if __name__ == '__main__':
	unittest.main()

