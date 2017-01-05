# -*- coding: utf-8 -*-


import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from config import env
from src.test.common import log


class compatiblemethod(object):
    """写一个兼容的方法，继承基类"""
    def __init__(self, method):
        self._method = method
    #obj是object的实例，klass是所有类
    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj) #如果没有其他参数，类本身就是参数
            print obj

        if isinstance(obj, klass):
            klass = obj
            klass.__name__ = klass.__class__.__name__


        def newfunc(*args, **kws):
            '''传参的数量任意，就是调用这个静态方法的每个参数（即浏览器要做出的动作click什么的）'''
            return self._method(klass, *args, **kws)

        return newfunc


class WebBrowser:
    """cls是在WebBrowser的第一个方法中命名的"""
    @compatiblemethod
    def ScrollTo(cls,x,y):
        log.step_normal(u"Element [%s]: Scroll To [%s, %s]" % (cls.__name__, x, y))
        env.threadlocal.BROWSER.execute_script("window.scrollTo(%s, %s);" % (x, y))

    @compatiblemethod
    def AlertAccept(cls):
        """接受警告信息"""
        log.step_normal("AlertAccept()")
        time.sleep(2)
        try:
            log.step_normal("switch_to_alert()")
            alert = env.threadlocal.BROWSER.switch_to_alert()
            alert.accept()
        except NoAlertPresentException:
            log.step_normal("Alert Not Found.")
        try:
            log.step_normal("switch_to_default_content()")
            env.threadlocal.BROWSER.switch_to_default_content()
        except:
            pass

    @compatiblemethod
    def AlertDismiss(cls):
        """取消点击弹窗"""
        log.step_normal("AlertDismiss()")

        time.sleep(2)
        try:
            log.step_normal("switch_to_alert()")
            alert = env.threadlocal.BROWSER.switch_to_alert()
            alert.dismiss()
        except NoAlertPresentException:
            log.step_normal("Alert Not Found.")

        try:
            log.step_normal("switch_to_default_content()")
            env.threadlocal.BROWSER.switch_to_default_content()
        except:
            pass

    @compatiblemethod
    def AlertSendKeys(cls, value):
        """在弹窗中输入值：就是将页面的value值输入到弹窗的文本框中"""
        log.step_normal("AlertSendKeys [%s]" % value)
        try:
            env.threadlocal.BROWSER.switch_to.alert.send_keys(value)
            env.threadlocal.BROWSER.switch_to.default_content()
        except:
            log.step_warning(str(sys.exc_info()))

    @compatiblemethod
    def SwitchToFrame(cls, frame):
        '''必须传入frame这个参数'''
        log.step_normal("SwitchToFrame()")
        env.threadlocal.BROWSER.switch_to.frame(frame)

    @compatiblemethod
    def SwitchToDefaultContent(cls):
        '''默认的frame不需要传参'''
        log.step_normal("SwitchToDefaultContent()")

        try:
            env.threadlocal.BROWSER.switch_to.default_content()
        except:
            log.step_warning("env.threadlocal.BROWSER.switch_to.default_content()")
            pass


    # @compatiblemethod
    # def Refresh(cls, times=4):
    #     log.step_normal(u"Element [%s]: Browser Refresh" % (cls.__name__,))
    #
    #     for i in range(times):
    #         action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #         action.key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
    #         time.sleep(5)

    # @compatiblemethod
    # def DeleteAllCookies(cls):
    #     log.step_normal(u"Element [%s]: Browser Delete All Cookies" % (cls.__name__,))
    #     env.threadlocal.BROWSER.delete_all_cookies()
    #     time.sleep(3)

    # @compatiblemethod
    # def DeleteAllCookies(cls):
    #     log.step_normal(u"Element [%s]: Browser Delete All Cookies" % (cls.__name__,))
    #     env.threadlocal.BROWSER.delete_all_cookies()
    #     time.sleep(3)

    # @compatiblemethod
    # def NavigateTo(cls, url):#打开新页面
    #     log.step_normal(u"Element [%s]: Navigate To [%s]" % (cls.__name__, url))
    #     env.threadlocal.BROWSER.get(url)
    #     time.sleep(3)


    # @compatiblemethod
    # def AlertTextHave(cls, txt_value):
    #     log.step_normal("AlertTextHave [%s]" % txt_value)
    #     alert_text = env.threadlocal.BROWSER.switch_to_alert().text()
    #
    #     if txt_value in alert_text:
    #         log.step_pass("pass")
    #     else:
    #         log.step_fail("fail")
    #     env.threadlocal.BROWSER.switch_to_default_content()


    # @compatiblemethod
    # def SwitchToNewPopWindow(cls):
    #     log.step_normal("SwitchToNewPopWindow()")
    #
    #     t = 0
    #     while (t < 10):
    #         t = t + 1
    #         time.sleep(3)
    #
    #         if len(env.threadlocal.BROWSER.window_handles) < 2:
    #             log.step_normal("Pop Window Not Found. Wait 3 Seconds then Try Again!")
    #         else:
    #             break
    #
    #     env.threadlocal.BROWSER.switch_to.window(env.threadlocal.BROWSER.window_handles[-1])
    #
    #     log.step_normal("Switch To The New Window of : %s" % str(env.threadlocal.BROWSER.window_handles))
    #
    # @compatiblemethod
    # def SwitchToDefaultWindow(cls):
    #     log.step_normal("SwitchToDefaultWindow()")
    #
    #     log.step_normal("Switch To The Default Window of: %s" % str(env.threadlocal.BROWSER.window_handles))
    #
    #     try:
    #         env.threadlocal.BROWSER.switch_to.window(env.threadlocal.BROWSER.window_handles[0])
    #     except:
    #         log.step_warning("env.threadlocal.BROWSER.switch_to.window(env.threadlocal.BROWSER.window_handles[0])")
    #         pass


class WebElement:
    (by, value) = (None, None)
    index       = 0

    @compatiblemethod
    def __init__(cls,by=None, value=None):
        '''by和value的值就是页面参数.by和.value的值'''
        cls.by = by
        cls.value = value

    @compatiblemethod
    def Set(cls, value):
        log.step_normal(u"Element [%s]: Set [%s]." % (cls.__name__, value))

        value = str(value)

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        if elements[cls.index].tag_name == "select" or elements[cls.index].tag_name == "ul":
            cls.Select(value) #有可能是下拉框取值

        else:
            elements[cls.index].clear() #先清空输入框
            action = webdriver.ActionChains(env.threadlocal.BROWSER)
            action.send_keys_to_element(elements[cls.index], value)
            action.perform()
            cls.__clearup()

    @compatiblemethod
    def Click(cls):
        log.step_normal("Element [%s]: Click()" % (cls.__name__))
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.click(elements[cls.index])
        action.perform()
        cls.__clearup()







    # @compatiblemethod
    # def ScrollIntoView(cls):
    #     log.step_normal(u"Element [%s]: ScrollToView()" % cls.__name__)
    #
    #     cls.__wait()
    #     elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #     i = 0
    #     while not elements[cls.index].is_displayed():
    #         WebBrowser.ScrollTo(0, i)
    #         i = i + 10
    #
    #         if i == 1000:
    #             log.step_normal("still not displayed. break out.")










