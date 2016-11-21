from appium import webdriver

def driver_mall():
	desired_caps = {}
	desired_caps['device'] = ''
	desired_caps['platformName'] = ''
	desired_caps['platformVersion'] = ''
	desired_caps['deviceName'] = ''
	desired_caps['appPackage'] = 'com.yidejia.app.mall'
	desired_caps['appActivity'] = 'com.yidejia.app.mall.ui.WelcomeActivity'
	return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

def driver_teacher():
	desired_caps = {}
	desired_caps['device'] = ''
	desired_caps['platformName'] = ''
	desired_caps['platformVersion'] = ''
	desired_caps['deviceName'] = ''
	desired_caps['appPackage'] = 'com.yidejia.teacher'
	desired_caps['appActivity'] = '.ui.MainActivity'
	return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)