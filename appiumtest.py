#coding=utf-8
from appium import webdriver
import time
/test
# device=mr.waitForConnection(5,"047fa8290024760d")
# device.startActivity(component="com.yidejia.app.mall/.ui.MainActivity")


desired_caps = {}
desired_caps['device'] = 'android'
desired_caps['platformName'] = 'android'

desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.1.188:5555'
# desired_caps['appPackage'] = 'com.yidejia.app.mall'
# desired_caps['appActivity'] = 'com.yidejia.app.mall.ui.WelcomeActivity'
desired_caps['appPackage'] = 'com.yidejia.teacher'
desired_caps['appActivity'] = '.ui.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)

driver.quit()

# adb devices
# adb connect [ip]
# adb uninstall com.yidejia.app.mall
# adb uninstall com.yidejia.teacher
# adb install [path]


