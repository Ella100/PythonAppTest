from common.capability_yaml import desired_caps
from appium import webdriver
from common.ObjectMap import get_element
from selenium.webdriver.support.ui import WebDriverWait
from time import strftime, localtime
import time
import logging
import os
#用于实现具体页面动作的封装

# 定义全局driver变量
driver = None

def open_app():
    # 打开应用
    global driver
    try:
        driver = desired_caps()
    except Exception as e:
        raise e

def quit_app():
    #退出应用
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def visit_url(url,*arg):
    #访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def sleep(sleepSeconds, *arg):
    #强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*args):
    #清除输入框默认内容
    global driver
    try:
        get_element(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    #在页面输入框中输入数据
    global driver
    try:
        get_element(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*arg):
    #单击页面元素
    global driver
    try:
        get_element(driver,locationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*arg):
    #断言页面源码是否存在某关键字或关键字符串
    global driver
    try:
        assert assertString in driver.page_source," %s not found in page_source" % assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def switch_alert_accept():
    # 弹窗中点击确定,适用于APP弹窗
    global driver
    try:
        alert_window_a = driver.switch_to.active_element
        alert_window_a.click()
    except Exception as e:
        raise e

def switch_alert_accept2():
    # 弹窗中点击确定
    global driver
    try:
        alert_window_a = driver.switch_to.alert
        alert_window_a.accept()
    except Exception as e:
        raise e


#获取当前上下文情况
def get_context():
    global driver
    try:
        contexts = driver.contexts
        print(contexts)
    except Exception as e:
        raise e

#切换上下文
def switch_to_context(contextName,*arg):
    global driver
    try:
        driver.switch_to.context(contextName)
    except Exception as e:
        raise e

def get_size(*arg):
    global driver
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

def swipeLeft(*arg):
    global driver
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

def swipeUp(*arg):
    #向上滑动
    global driver
    l = get_size()
    x1=int(l[0]*0.5)
    y1=int(l[1]*0.75)
    y2=int(l[1]*0.25)
    driver.swipe(x1,y1,x1,y2,1000)

def swipeDown(*arg):
    # 向下滑动
    global driver
    l = get_size()
    x1=int(l[0]*0.5)
    y1=int(l[1]*0.25)
    y2=int(l[1]*0.75)
    driver.swipe(x1,y1,x1,y2,1000)

#截取屏幕图片
def getScreenShot(sheetname,*arg):
    global driver
    time = strftime('%Y%m%d%H_%M_%S',localtime())
    image_file = os.path.dirname(os.path.dirname(__file__))+'\screenshots\%s_%s.png' % (sheetname,time)
    logging.info("image_file:%s" % image_file)
    driver.get_screenshot_as_file(image_file)
    return image_file

#检查frame是否存在，存在则切进frame空间中
def waitPresenceOfElementLocated(locationType,locatorExpression,*args):
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def assertUrl(url,*args):
    #断言URL是否正确
    global driver
    try:
        currentPageUrl = driver.current_url
        print(currentPageUrl)
        if url == currentPageUrl:
            pass
        else:
            raise Exception
    except Exception as e:
        raise e

def getText(locationType,locatorEpression,*args):
    #获得表达式的text值，并保存至全局变量Text中
    global driver,Text
    try:
        Text = get_element(driver,locationType,locatorEpression).text
        print(Text)
        return Text
    except Exception as e:
        raise e

def getValue(locationType,locatorExpression,*args):
    #获取选定元素的Value属性值，并保存至全局变量GValue中
    global driver,GValue
    try:
        GValue = get_element(driver,locationType,locatorExpression).get_attribute("value")
        # print(GValue)
        return GValue
    except Exception as e:
        raise e

def assert_element_text(locationType,locatorExpression,input_value,*arg):
    #判断element_text
    global driver
    try:
        element = get_element(driver,locationType,locatorExpression)
        if element:
            value = element.text
            if value.find(input_value) != -1 or value.find(Text) != -1 or value.find(GValue) != -1:
                # print(u'存在')
                pass
            else:
                # print(u'无此字段')
                raise Exception
        else:
            print(element)
            raise Exception
    except Exception as e:
        raise e

def assertElementHtml(locationType,locatorExpression,String,*args):
    #断言选中元素源码中存在某字段
    global driver
    try:
        SourceHtml = get_element(driver,locationType,locatorExpression).get_attribute("outerHTML")
        # print(SourceHtml)
        if String in SourceHtml:
            pass
        else:
            raise Exception
    except Exception as e:
        raise e
