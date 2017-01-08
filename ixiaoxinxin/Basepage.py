# -*- coding: utf-8 -*-


import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, UnexpectedAlertPresentException, WebDriverException
import log
import env


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



    @compatiblemethod
    def Select(cls,value):
        log.step_normal("Element [%s] : Select [%s]." % (cls.__name__, value))

        ############从浏览器获取by和value################
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        is_selected = False

        ############select##################
        if elements[cls.index].tag_name == "select":
            options = elements[cls.index].find_elements_by_tag_name('option')

            for options in options:

                if options.text == value:
                    options.click()
                    is_selected = True
                    break

        elif elements[cls.index].tag_name == "ul":
            lis = elements[cls.index].find_element_by_tag_name("li")

            for li in lis:

                if li.text == value:
                    li.click()
                    is_selected =True
                    break

        else:
            log.step_fail("Element [%s] : Tag [%s] NOT supert [Select] method" %
                          (cls.__name__, elements[cls.index].tag_name))

        if is_selected is False:
            log.step_fail("No item selected!")

        cls.clearup()

    def MouseOver(cls):
        log.step_normal("Element [%s]:MouseOver" % (cls.__name__))

        time.sleep(1)

        cls._wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.move_to_element(elements[cls.index])
        action.perform()

        cls.__clearup()

        time.sleep(1)


    def DoubleClick(cls):
        log.step_normal("Element [%s]: DoubleClick()" % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.double_click(elements[cls.index])
        action.perform()

        cls.__clearup()

    @compatiblemethod
    def TypeIn(cls, value):
        '''Input value without clear existing values
        '''
        log.step_normal(u"Element [%s]: TypeIn [%s]." % (cls.__name__, value))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        elements[cls.index].send_keys(value)
        # =======================================================================
        # action = webdriver.ActionChains(env.threadlocal.BROWSER)
        # action.send_keys_to_element(elements[cls.index], value)
        # action.perform()
        # =======================================================================

        cls.__clearup()

    @compatiblemethod
    def SendEnter(cls):
        log.step_normal(u"Element [%s]: SendEnter()" % (cls.__name__,))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.send_keys_to_element(elements[cls.index], Keys.ENTER)
        action.perform()

        cls.__clearup()

    @compatiblemethod
    def GetObjectsCount(cls):
        log.step_normal("Element [%s]: GetObjectsCount." % (cls.__name__))

        cls.__wait_for_appearing()

        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: GetObjectsCount = [%s]" % (cls.__name__, len(elements)))

        cls.__clearup()
        return len(elements)

    @compatiblemethod
    def GetRealTimeObjCount(cls):  #### get real time obj counts, without waiting.
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: GetRealTimeObjCount = [%s]" % (cls.__name__, len(elements)))

        cls.__clearup()
        return len(elements)

    @compatiblemethod
    def GetElementObj(cls):  #### get real time obj counts, without waiting.
        log.step_normal("Element [%s]: GetElementObj." % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        cls.__clearup()
        return elements[cls.index]

    @compatiblemethod
    def GetAttribute(cls, attr):
        log.step_normal(u"Element [%s]: GetAttribute [%s]." % (cls.__name__, attr))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        attr_value = elements[cls.index].get_attribute(attr)
        log.step_normal(u"Element [%s]: Attribute Value = [%s]." % (cls.__name__, attr_value))

        cls.__clearup()
        return attr_value

    @compatiblemethod
    def GetParentElement(cls):
        log.step_normal("Element [%s]: GetParentElement()" % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        return elements[cls.index].parent()

    @compatiblemethod
    def GetText(cls):
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal(u"Element [%s]: Gets the text of the element, the content is %s." % (
        cls.__name__, elements[cls.index].text))
        return elements[cls.index].text

    @compatiblemethod
    def Wait(cls, seconds):
        log.step_normal("Element [%s]: Wait for [%s] seconds." % (cls.__name__, seconds))

        time.sleep(seconds)

    @compatiblemethod
    def WaitForAttribute(cls, name, value, method="equal"):
        '''
        处理断言的方法
        Example:
            NewClaim.Dates.ReminderDate.WaitForAttribute('ng-model', 'hello', method='equal')
            NewClaim.Dates.ReminderDate.WaitForAttribute('ng-model', 'hello', method='contain')
            NewClaim.Dates.ReminderDate.WaitForAttribute('ng-model', 'hello', method='not contain')
            NewClaim.Dates.ReminderDate.WaitForAttribute('ng-model', 'hello', method='in')
            NewClaim.Dates.ReminderDate.WaitForAttribute('ng-model', 'hello', method='not equal')

        Description for "method":
            equal  => real value is 'hello'
            has    => real value contains 'hello', e.g. 'hello world'.
            in     => real value in 'hello', e.g. 'he'
            differ => real value not equal to 'hello', e.g. 'hehe'

        '''
        log.step_normal("Element [%s]: WaitForAttribute [%s] <%s> [%s]." % (cls.__name__, name, method, value))

        i = 0
        while True:
            cls.__wait()
            elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

            realvalue = elements[cls.index].get_attribute(name)

            if method.lower() == 'equal':
                if value.lower() == realvalue.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue)
                    break
                else:
                    log.step_normal("No! real value=[%s]" % realvalue)

            elif method.lower() == 'contain':
                if value.lower() in realvalue.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue[:150])
                    break
                else:
                    log.step_normal("No! real value=[%s]" % realvalue[:150])

            elif method.lower() == 'not contain':
                if value.lower() in realvalue.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue[:150])
                else:
                    log.step_normal("No! real value=[%s]" % realvalue[:150])
                    break

            elif method.lower() == 'in':
                if realvalue.lower() in value.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue[:150])
                    break
                else:
                    log.step_normal("No! real value=[%s]" % realvalue[:150])

            elif method.lower() == 'not equal':
                if value.lower() == realvalue.lower():
                    log.step_normal("No! real value=[%s]" % realvalue)
                else:
                    log.step_normal("Yes! real value=[%s]" % realvalue)
                    break

            else:
                log.step_fail("code error.")

            i = i + 1
            if i > 90:
                log.step_fail("Not Found Expected Value! real value=[%s]" % realvalue)
                break

            time.sleep(1)

        cls.__clearup()

    @compatiblemethod
    def WaitForAppearing(cls):
        log.step_normal("Element [%s]: WaitForAppearing..." % (cls.__name__))

        cls.__wait_for_appearing()
        cls.__clearup()

    @compatiblemethod
    def WaitForDisappearing(cls):
        log.step_normal("Element [%s]: WaitForDisappearing..." % (cls.__name__))

        cls.__wait_for_disappearing()
        cls.__clearup()

    @compatiblemethod
    def WaitForVisible(cls):
        log.step_normal("Element [%s]: WaitForVisible..." % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        t = 0
        while (t < 90):
            if elements[cls.index].is_displayed():
                log.step_normal("Element [%s]: IS visible now." % (cls.__name__))
                break
            else:
                log.step_normal("Element [%s]: Still NOT visible, wait 1 second." % (cls.__name__))
                time.sleep(1)

        cls.__clearup()

    @compatiblemethod
    def WaitForEnabled(cls):
        log.step_normal("Element [%s]: WaitForEnabled..." % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        t = 0
        while (t < 90):
            if elements[cls.index].is_enabled():
                log.step_normal("Element [%s]: is enabled now." % (cls.__name__))
                break
            else:
                log.step_normal("Element [%s]: still NOT enabled, wait 1 second." % (cls.__name__))
                time.sleep(1)

            t = t + 1

        cls.__clearup()

    @compatiblemethod
    def IsEnabled(cls):
        log.step_normal(u"Element [%s]: Is Enabled?" % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        if elements[cls.index].is_enabled():
            log.step_normal(u"Yes!")
            cls.__clearup()
            return True
        else:
            log.step_normal(u"No!")
            cls.__clearup()
            return False

    @compatiblemethod
    def IsExist(cls):
        log.step_normal("Element [%s]: IsExist?" % (cls.__name__))

        time.sleep(2)

        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: IsExist? Count = [%s]" % (cls.__name__, len(elements)))

        cls.__clearup()

        if len(elements) > 0:
            return True
        else:
            return False

    @compatiblemethod
    def IsVisible(cls):
        log.step_normal("Element [%s]: IsVisible?" % (cls.__name__))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        if elements[cls.index].is_displayed():
            cls.__clearup()
            return True
        else:
            cls.__clearup()
            return False

    @compatiblemethod
    def IsAttribute(cls, name, value, method="contain"):
        log.step_normal("Element [%s]: IsAttribute [%s] <%s> [%s]." % (cls.__name__, name, method, value))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        realvalue = elements[cls.index].get_attribute(name)

        if method.lower() == 'equal':
            if value == realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False

        elif method.lower() == 'not equal':
            if not value == realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False

        elif method.lower() == 'contain':
            if value in realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False

        elif method.lower() == 'not contain':
            if not value in realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False

        elif method.lower() == 'in':
            if realvalue in value:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False


        else:
            log.step_fail("code error.")

        cls.__clearup()

    @compatiblemethod
    def VerifyExistence(cls, trueORfalse):
        log.step_normal("Element [%s]: Verify Existence = [%s]." % (cls.__name__, trueORfalse))

        if trueORfalse == True:
            cls.__wait_for_appearing()
        else:
            cls.__wait_for_disappearing()

        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: Count = [%s]" % (cls.__name__, len(elements)))

        cls.__clearup()
        if len(elements) > 0:
            if trueORfalse == True:
                log.step_pass("Exist!")
            else:
                log.step_fail("Exist!")
        else:
            if trueORfalse == False:
                log.step_pass("Not Exist!")
            else:
                log.step_fail("Not Exist!")

    @compatiblemethod
    def VerifyVisible(cls, trueORfalse):
        log.step_normal("Element [%s]: Verify Visible = [%s]." % (cls.__name__, trueORfalse))

        cls.__wait()

        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: Count = [%s]" % (cls.__name__, len(elements)))

        if elements[cls.index].is_displayed():
            if trueORfalse == True:
                log.step_pass("Visible!")
            else:
                log.step_fail("Visible!")
        else:
            if trueORfalse == False:
                log.step_pass("Not Visible!")
            else:
                log.step_fail("Not Visible!")

        cls.__clearup()

    @compatiblemethod
    def VerifyEnabled(cls, trueOrfalse):
        log.step_normal(u"Element [%s]: Verify Enabled = [%s]" % (cls.__name__, trueOrfalse))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        is_disabled = elements[cls.index].get_attribute("disabled")
        log.step_normal(u"Element [%s]: attribute 'is_disabled' = [%s]" % (cls.__name__, is_disabled))

        if is_disabled == "true":
            if trueOrfalse == False:
                log.step_pass("Pass...")
            else:
                log.step_fail("Fail...")

        elif elements[cls.index].is_enabled():
            if trueOrfalse == True:
                log.step_pass("Pass")
            else:
                log.step_fail("Fail")

        else:
            log.step_fail("Not verified.")

        cls.__clearup()

    @compatiblemethod
    def VerifyInnerHTMLContains(cls, contain_content):
        log.step_normal("Element [%s]: VerifyInnerHTMLContains [%s]." % (cls.__name__, str(contain_content)))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        inner_html = elements[cls.index].get_attribute('innerHTML')

        if isinstance(contain_content, list):
            for content in contain_content:
                if content in inner_html:
                    log.step_pass("Real inner_hmtl=[%s]" % inner_html)
                else:
                    log.step_fail("Real inner_hmtl=[%s]" % inner_html)

        else:
            if contain_content in inner_html:
                log.step_pass("Real inner_hmtl=[%s]" % inner_html)
            else:
                log.step_fail("Real inner_hmtl=[%s]" % inner_html)

        cls.__clearup()

    @compatiblemethod
    def VerifyAttribute(cls, name, value, method='equal'):
        '''
        Example:
            NewClaim.Dates.ReminderDate.VerifyAttribute('ng-model', 'hello', method='equal')
            NewClaim.Dates.ReminderDate.VerifyAttribute('ng-model', 'hello', method='contain')
            NewClaim.Dates.ReminderDate.VerifyAttribute('ng-model', 'hello', method='in')
            NewClaim.Dates.ReminderDate.VerifyAttribute('ng-model', 'hello', method='not equal')

        Description for "method":
            equal  => real value is 'hello'
            has    => real value contains 'hello', e.g. 'hello world'.
            in     => real value in 'hello', e.g. 'he'
            differ => real value not equal to 'hello', e.g. 'hehe'

        '''
        log.step_normal("Element [%s]: VerifyAttribute [%s] <%s> [%s]." % (cls.__name__, name, method, value))

        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        realvalue = elements[cls.index].get_attribute(name)

        if method.lower() == 'equal':
            if value == realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)

        elif method.lower() == 'not equal':
            if not value == realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)

        elif method.lower() == 'contain':
            if value in realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)

        elif method.lower() == 'not contain':
            if not value in realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)

        elif method.lower() == 'in':
            if realvalue in value:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)

        else:
            log.step_fail("code error.")

        cls.__clearup()

    @compatiblemethod
    def __wait_for_enabled(cls):
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        if elements[cls.index].is_enabled():
            return
        else:
            t = 0
            while t < 90:
                if elements[cls.index].is_enabled():
                    break

                log.step_normal("Element [%s]: __wait_for_enabled for 1 second, By [%s :: %s :: %s]" % (
                cls.__name__, cls.by, cls.value, cls.index))
                time.sleep(0.5)

    @compatiblemethod
    def __wait(cls):
        t = 0
        while t < 300:
            t = t + 1

            try:
                elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            except NoSuchElementException:
                log.step_normal("Element [%s]: NoSuchElementException." % cls.__name__)
                elements = []
            except UnexpectedAlertPresentException:
                log.step_warning("Element [%s]: UnexpectedAlertPresentException." % cls.__name__)

            if len(elements) == 0:
                time.sleep(0.5)
                log.step_normal("Element [%s]: Wait 0.5 second, By [%s :: %s :: %s]" % (
                cls.__name__, cls.by, cls.value, cls.index))
            else:
                if len(elements) > 1:
                    log.step_normal("Element [%s]: There are [%s] Elements!" % (cls.__name__, len(elements)))

                break

        if len(elements) < cls.index + 1:
            log.step_fail("Element [%s]: Element Index Issue! There are [%s] Elements! Index=[%s]" % (
            cls.__name__, len(elements), cls.index))

    @compatiblemethod
    def __wait_for_disappearing(cls):

        t = 0
        while t < 120:
            t = t + 1

            try:
                elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            except NoSuchElementException:
                log.step_normal("Element [%s]: NoSuchElementException." % cls.__name__)
                elements = []
                continue
            except UnexpectedAlertPresentException:
                log.step_warning("Element [%s]: UnexpectedAlertPresentException." % cls.__name__)

            if len(elements) == 0:
                return True
            else:
                time.sleep(0.5)
                log.step_normal("Element [%s]: WairForDisappearing... Found [%s] Element. Tried [%s] Times." % (
                cls.__name__, len(elements), t))

        return False

    @compatiblemethod
    def __wait_for_appearing(cls):

        t = 0
        while t < 120:
            t = t + 1

            try:
                elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            except NoSuchElementException:
                log.step_normal("Element [%s]: NoSuchElementException." % cls.__name__)
                elements = []
                continue
            except UnexpectedAlertPresentException:
                log.step_warning("Element [%s]: UnexpectedAlertPresentException." % cls.__name__)

            if len(elements) == 0:
                time.sleep(0.5)
                log.step_normal(
                    "Element [%s]: WaitForAppearing... Wait 1 second, By [%s]" % (cls.__name__, cls.value))
            else:
                log.step_normal(
                    "Element [%s]: Found [%s] Element. Tried [%s] Times." % (cls.__name__, len(elements), t))
                break

    @compatiblemethod
    def __clearup(cls):
        if cls.index != 0:
            log.step_normal("Element [%s]: The Operation Element Index = [%s]." % (cls.__name__, cls.index))

            #         cls.index = 0




























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


    # @compatiblemethod
    # def SelectByPartial(cls, value):
    #     log.step_normal("Element [%s]: Select [%s]." % (cls.__name__, value))
    #
    #     cls.__wait()
    #     elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #
    #     is_selected = False
    #
    #     #### select ################
    #     if elements[cls.index].tag_name == "select":
    #         options = elements[cls.index].find_elements_by_tag_name('option')
    #
    #         for option in options:
    #             if value in option.text:
    #                 option.click()
    #                 is_selected = True
    #                 break
    #
    #     #### ul ################
    #     elif elements[cls.index].tag_name == "ul":
    #         lis = elements[cls.index].find_elements_by_tag_name('li')
    #
    #         for li in lis:
    #             if value in li.text:
    #                 li.click()
    #                 is_selected = True
    #                 break
    #
    #     #### NOT Supported ################
    #     else:
    #         log.step_fail(
    #             "Element [%s]: Tag [%s] NOT support [Select] method" % (cls.__name__, elements[cls.index].tag_name))
    #
    #     if is_selected is False:
    #         log.step_fail("No item selected!")
    #
    #     cls.__clearup()

    # @compatiblemethod
    # def SelectByOrder(cls, order):
    #     log.step_normal("Element [%s] : Select by Order [%s]" % (cls.__name__, order))
    #     order = int(order)
    #
    #     cls.__wait()
    #     elements =env.threadlocal.BROWSER.find_elements(cls.by,cls.value)
    #
    #     if elements[cls.index].tag_name == "ul":
    #         lis = elements[cls.index].find_element_by_tag_name('li')
    #
    #         if order > 0:
    #             t = 0
    #             #############尝试等待下拉框取值显示出来################
    #             while(len(lis) == 0):
    #                 lis = elements[cls.index].find_elements_by_tag_name('li')
    #                 time.sleep(3)
    #                 t = t+1
    #                 log.step_normal("Element [%s] : Wait 3 Seconds for [li]" % cls.__name__)
    #
    #                 if t == 20 and len(lis) == 0:
    #                     log.step_fail("Element [%s]:List Count = [%s]" % (cls.__name__, len(lis)))
    #                     return
    #
    #             log.step_normal("Element [%s] : List Count = [%s]" % (cls.__name__, len(lis)))
    #
    #             if(order > len(lis)):
    #                 log.step_fail("Element [%s]: Not so many lists. [%s]" % (cls.__name__, len(lis)))
    #             else:
    #                 log.step_normal("Element [%s]:Do click [%s]" % (cls.__name__,order))
    #                 action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #
    #                 elements = env.threadlocal.BROWSER.find_elements(cls.by,cls.value)
    #                 lis = elements[cls.index].find_elements_by_tag_name('li')
    #
    #                 action.click(lis[order-1])
    #                 action.perform()
    #         else:
    #             log.step_fail("Order = [%s],Value Error" % order)
    #
    #     else:
    #         ###select####
    #         options = elements[cls.index].find_element_by_tag_name('option')
    #
    #         if order > 0:
    #             #####如果下拉选项不存在，则多试几次######
    #             t = 0
    #             while(len(options) == 0):
    #                 options = elements[cls.index].find_element_by_tag_name('option')
    #                 time.sleep(3)
    #                 t = t + 1
    #                 log.step_normal("Element [%s]:Wait 3 Seconds for [option]" % cls.__name__)
    #
    #                 if t == 20 and len(lis) == 0:
    #                     log.step_fail("Element [%s]: options Count = [%s]." % (cls.__name__, len(options)))
    #                     return
    #
    #             log.step_normal("Element [%s]: options Count = [%s]." % (cls.__name__, len(options)))
    #
    #             if (order > len(options)):
    #                 log.step_fail("Element [%s]: Not so many options. [%s]" % (cls.__name__, len(options)))
    #             else:
    #                 log.step_normal("Element [%s]: Do Click [%s]" % (cls.__name__, order))
    #                 action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #                 action.click(options[order-1])
    #                 action.perform()
    #         else:
    #             log.step_fail("Order = [%s], Value Error." % order)
    #
    #
    #     cls.__clearup()


    # @compatiblemethod
    # def ClickTillObjAppear(cls, obj):
    #     '''
    #     DESCRIPTION
    #         Sometimes, one click on the element doesn't work. So wait 3 seconds, then
    #         click again and again until the expected object "obj" appear.
    #
    #     RISK
    #         It may do click() for many times!!!
    #
    #     EXAMPLES
    #         Login.LoginButton.ClickTillObjAppear(OverView.LatestClaims.Button_Office())
    #     '''
    #     log.step_normal("Element [%s]: ClickTillObjAppear()" % (cls.__name__))
    #
    #     cls.Click()
    #
    #     # =======================================================================
    #     # cls.__wait()
    #     # elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #     #
    #     # i = 0
    #     # while obj.GetRealTimeObjCount() == 0:
    #     #     try:
    #     #         action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #     #         action.click(elements[cls.index])
    #     #         action.perform()
    #     #
    #     #         log.step_normal("click [%s] times..." % i)
    #     #         time.sleep(5)
    #     #
    #     #         i = i + 1
    #     #         if i == 2:
    #     #             log.step_normal("too many clicking times....")
    #     #             break
    #     #     except:
    #     #         log.step_normal(sys.exc_info()[0])
    #     #
    #     # cls.__clearup()
    #     # =======================================================================


    # @compatiblemethod
    # def ClickTillObjDisappear(cls, obj):
    #     '''
    #     DESCRIPTION
    #         Sometimes, one click on the element doesn't work. So wait 3 seconds, then
    #         click again and again until the expected object "obj" disappear.
    #
    #     RISK
    #         It may do click() for many times!!!
    #
    #     EXAMPLES
    #         Login.LoginButton.ClickTillObjDisappear(OverView.Button_Office())
    #     '''
    #     log.step_normal("Element [%s]: ClickTillObjDisappear()" % (cls.__name__))
    #
    #     cls.Click()
    #
    #     # =======================================================================
    #     # cls.__wait()
    #     # elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #     #
    #     # i = 0
    #     # while True:
    #     #     if obj.GetRealTimeObjCount() == 0:
    #     #         break
    #     #
    #     #     try:
    #     #         action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #     #         action.click(elements[cls.index])
    #     #         action.perform()
    #     #     except:
    #     #         log.step_normal(sys.exc_info()[0])
    #     #
    #     #     log.step_normal("click [%s] times..." % i)
    #     #     time.sleep(5)
    #     #
    #     #     i = i + 1
    #     #     if i == 2:
    #     #         log.step_fail("too many clicking times....")
    #     #         break
    #     #
    #     # cls.__clearup()
    #     # =======================================================================


    # @compatiblemethod
    # def ClickAndHold(cls):
    #     log.step_normal("Element [%s]: ClickAndHold()" % (cls.__name__))
    #
    #     cls.__wait()
    #     elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #
    #     action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #     action.click_and_hold(elements[cls.index])
    #     action.perform()
    #
    #     cls.__clearup()
    #
    #
    # @compatiblemethod
    # def DragAndDropByOffset(cls, xoffset, yoffset):
    #     '''
    #     Holds down the left mouse button on the source element,
    #     then moves to the target offset and releases the mouse button.
    #     '''
    #     log.step_normal("Element [%s]: drag_and_drop_by_offset()" % (cls.__name__))
    #     cls.__wait()
    #     elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #
    #     action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #     action.drag_and_drop_by_offset(elements[cls.index], xoffset, yoffset)
    #     action.perform()
    #
    #     cls.__clearup()
    #
    #
    # @compatiblemethod
    # def ReleaseClick(cls):
    #     log.step_normal("Element [%s]: ReleaseClick()" % (cls.__name__))
    #
    #     cls.__wait()
    #     elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
    #
    #     action = webdriver.ActionChains(env.threadlocal.BROWSER)
    #     action.release(elements[cls.index])
    #     action.perform()
    #
    #     cls.__clearup()
    #
    # @compatiblemethod
    # def FetchSubElementOfXPath(cls, layer):
    #     return WebElement(cls.by, "/".join(cls.value.split("/")[:layer + 2]))


