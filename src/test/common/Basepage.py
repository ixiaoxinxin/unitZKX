# -*- coding: utf-8 -*-
from config import env
from log import log
import time, sys
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, UnexpectedAlertPresentException, WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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






