#!/usr/bin/python
#coding:utf-8
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
MAX = 0
RES_DICT = {}

def scrollDown(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height'] 
    driver.swipe(x/2, y * 4/5, x/2, y * 1/5, 876)

def swipeDownUntilElementShow(driver, by, pattern):
    try:
        s = 'new UiSelector().text("' + pattern + '")'
        driver.find_element_by_android_uiautomator(s)
    except:
        scrollDown(driver)
        swipeDownUntilElementShow(driver, by, pattern)

def saveSettingAboutPhone(driver):
    i = 0
    allReadyIn = 0
    global MAX
    global RES_DICT
    try:
        while True:
            titleStr = 'new UiSelector().resourceId("android:id/title").instance({})'.format(i)
            title = driver.find_element_by_android_uiautomator(titleStr)
            summaryStr = 'new UiSelector().resourceId("android:id/summary").instance({})'.format(i)
            summary = driver.find_element_by_android_uiautomator(summaryStr)
            if title.text.replace(u'\u2011' , '-') in RES_DICT:
                allReadyIn = allReadyIn + 1
            else:
                RES_DICT[title.text.replace(u'\u2011' , '-')] = summary.text    
            i = i + 1
    except:
        if MAX == 0:
            MAX = i
        if allReadyIn != i:
            scrollDown(driver)
            saveSettingAboutPhone(driver)

def printResult():
    global RES_DICT
    print('Result is:')
    for k, v in RES_DICT.items():
        print("{} -> {}".format(k, v))

def getSettingAboutPhone():
    dc = {}
    driver = None

    dc['deviceName'] = 'HTC_U-3u'
    dc['udid'] = 'FA7671801901'
    dc['platformName'] = 'android'
    dc['appPackage'] = 'com.android.settings'
    dc['appActivity'] = 'com.android.settings.Settings'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)
    swipeDownUntilElementShow(driver, By.XPATH, "About")
    driver.find_element_by_android_uiautomator('new UiSelector().text("About")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("Phone identity")').click()
    saveSettingAboutPhone(driver)
    printResult()




    driver.quit()
        
if __name__ == '__main__':
    getSettingAboutPhone()
