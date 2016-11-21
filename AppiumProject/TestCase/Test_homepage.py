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
		time.sleep(5)
		self.hp = HomePage(driver)

	def test_to_search(self):
		'''空关键字'''
		self.hp.click_search()
		self.assertEqual(self.hp.find_element(self.hp.btn_toSearch_loc).text,'搜索',msg='找不到搜索按钮')
		self.hp.click_toSearch()
		self.assertFalse(self.hp.has_imageview(),msg='搜索到内容')

	def test_search_NotExistKeyWords(self):
		'''搜索不匹配的关键字'''
		self.hp.click_search()
		self.assertEqual(self.hp.find_element(self.hp.btn_toSearch_loc).text,'搜索',msg='找不到搜索按钮')
		self.hp.input_search('NotExistKeyWord')
		self.hp.click_toSearch()
		self.assertFalse(self.hp.has_imageview(),msg='搜索到内容')

	def test_search_ExistKeyWords(self):
		'''搜索匹配的关键字'''
		self.hp.click_search()
		self.assertEqual(self.hp.find_element(self.hp.btn_toSearch_loc).text,'搜索',msg='找不到搜索按钮')
		self.hp.input_search('11')
		self.hp.click_toSearch()
		self.assertTrue(self.hp.has_imageview(),msg='搜索不到内容')
		
	def test_mainphoto(self):
		'''进入文件及分享页面'''
		
		# temptitle = self.hp.returnContent()
		print('主页标题：',temptitle)
		self.hp.click_mainphoto()
		#保存标题temptitle，跳转后判断contecnt_desc元素是否存在
		templist = []
		for x in self.hp.find_elements(self.hp.text_loc):
			templist.append(x.get_attribute('name'))
		
		#断言也是是否正常加载
		self.assertTrue(temptitle in templist,msg = '找不到标题')

		self.hp.click_share()
		temp = ['分享到:','微信好友','微博','QQ','QQ空间','微信朋友圈','取消']
		tempshare = self.hp.find_elements(self.hp.share_loc)
		
		self.assertEqual(tempshare[1].text,temp[1],msg='找不到微信好友分享按钮')
		self.assertEqual(tempshare[2].text,temp[2],msg='找不到微博分享按钮')
		self.assertEqual(tempshare[3].text,temp[3],msg='找不到QQ分享按钮')
		self.assertEqual(tempshare[4].text,temp[4],msg='找不到QQ空间分享按钮')
		self.assertEqual(tempshare[5].text,temp[5],msg='找不到微信朋友圈分享按钮')

	def test_home(self):
		'''测试主页面加载数据是否正常'''
		print("打印主页文章标题：")
		for x in self.hp.find_elements(self.hp.mainTestView_loc):
			print(x.text)

	def tearDown(self):
		self.hp.quit()




if __name__ == '__main__':
	unittest.main()

