__author__ = 'ZhangJianMing'

import sys,time,os
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait
from common import KeyValue
from appium import webdriver

class Base(object):

	def __init__(self, appium_driver):
		self.driver = appium_driver

	def find_element(self,loc):
		'''封装单个元素定位方法'''
		try:
			WebDriverWait(self.driver,15.).until(lambda driver:driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except Exception as e:
			print(u"%s 页面中未能找到 %s 元素" %(self,loc))
			

	def find_elements(self,loc):
		'''封装一组元素定位方法'''
		try:
			if len(self.driver.find_elements(*loc)):
				return self.driver.find_elements(*loc)
		except Exception as e:
			print(u"%s 页面中未能找到 %s 元素" %(self,loc))
			

	def quit(self):
		self.driver.quit()

	def send_keys(self,loc,value,clear_first=True,click_first=True):
		'''封装输入方法'''
		try:
			if click_first:
				self.find_element(loc).click()
			if clear_first:
				self.find_element(loc).clear()
			self.find_element(loc).send_keys(value)
			# self.find_element(loc).set_value(value)

		except AttributeError:
			print(u"%s 页面中未能找到 %s 元素" %(self,loc))
	
	def send_pwds(self,loc,value,clear_first=True,click_first=True):
		'''对密码框输入进行处理，appium有bug'''
		try:
			if click_first:
				self.find_element(loc).click()
			if clear_first:
				self.driver.keyevent(KeyValue.KEYCODE_MOVE_END)
				for x in range(0,32):
					self.driver.keyevent(KeyValue.KEYCODE_DEL)
			
			self.find_element(loc).send_keys(value)
			# self.find_element(loc).set_value(value)

		except AttributeError:
			print(u"%s 页面中未能找到 %s 元素" %(self,loc))

	def clickBtn(self,loc):
		'''封装点击方法'''
		try:
			self.find_element(loc).click()
		except AttributeError:
			print(u"%s 页面中未能找到 %s 元素" %(self,loc))

	def swipe_Up(self):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width/2,height*3/4,width/2,height/4,500)

	def swipe_Down(self):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width/2,height/4,width/2,height*3/4,500)

	def swipe_Left(self):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width/4,height/2,width*3/4,height/2,500)

	def swipe_Rigth(self):
		window_size = self.driver.get_window_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width*4/5,height/2,width/5,height/2,500)

	#dr_ 封装系统按钮键
	def dr_back(self):
		self.driver.keyevent(KeyValue.KEYCODE_BACK)

	def dr_home(self):
		self.driver.keyevent(KeyValue.KEYCODE_HOME)

	def dr_menu(self):
		self.driver.keyevent(KeyValue.KEYCODE_MENU)

	def take_Shot(self,name):
		day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
		fp = "..\\Result\\" + day
		tm = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
		type = '.png'
		
		filename = ''
		if os.path.exists(fp):
			filename = fp+"\\" + tm +'_'+ name + type
		else:
			os.makedirs(fp)
			filename = fp+"\\" + tm +'_'+ name + type
		
		self.driver.save_screenshot(filename)	

# [
# 'ACCESSIBILITY_ID', 
# 'ANDROID_UIAUTOMATOR', 
# 'CLASS_NAME', 
# 'CSS_SELECTOR', 
# 'ID', 
# 'IOS_UIAUTOMATION', 
# 'LINK_TEXT', 
# 'NAME', 
# 'PARTIAL_LINK_TEXT', 
# 'TAG_NAME', 
# 'XPATH'
# ]

# [ 'clear', 'click', 'find_element', 'find_element_by_accessibility_id',
# 'find_element_by_android_uiautomator', 'find_element_by_class_name', 
# 'find_element_by_css_selector', 'find_element_by_id', 'find_element_by_ios_uiautomation', 
# 'find_element_by_link_text', 'find_element_by_name', 'find_element_by_partial_link_text', 
# 'find_element_by_tag_name', 'find_element_by_xpath', 'find_elements', 
# 'find_elements_by_accessibility_id', 'find_elements_by_android_uiautomator', 
# 'find_elements_by_class_name', 'find_elements_by_css_selector', 
# 'find_elements_by_id', 'find_elements_by_ios_uiautomation', 
# 'find_elements_by_link_text', 'find_elements_by_name', 
# 'find_elements_by_partial_link_text', 
# 'find_elements_by_tag_name', 
# 'find_elements_by_xpath', 'get_attribute', 'id', 'is_displayed', 'is_enabled', 
# 'is_selected', 'location', 'location_in_view', 
# 'location_once_scrolled_into_view', 'parent', 'rect', 'screenshot', 
# 'screenshot_as_base64', 'screenshot_as_png', 'send_keys', 'set_text', 'set_value', 
# 'size', 'submit', 'tag_name', 'text', 'value_of_css_property']
