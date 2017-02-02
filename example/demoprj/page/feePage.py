# -*- coding: utf-8 -*-
'''
Page类封装了页面的控件和操作
需要调用BasePage基类中的方法
'''

from ixiaoxinxin.Basepage import WebElement,WebBrowser
from selenium.webdriver.common.by import By

# class Toubao(unittest.TestCase):
#     def test_login(self):
#         driver = Basepage.Basepage("ff")
#         driver.open("http://172.16.4.247:27002/index.jsp")
#         driver.clear('j_username','j_password')
#         (by,value)=(By.ID, 'j_username')
#         (by, value)=(By.ID, 'j_password')
#         (by,value)=(By.XPATH, '/html/body/table[5]/tbody/tr/td[7]/table/tbody/tr[1]/td/form/table/tbody[3]/tr[2]/td/table/tbody/tr/td[1]/a/img')

class Login:
    class username(WebElement):
        (by, value) = (By.ID, 'j_username')

    class passwd(WebElement):
        (by, value) = (By.ID, 'j_password')

    class ok(WebElement):
        (by, value) = (By.XPATH,
                       '/html/body/table[5]/tbody/tr/td[7]/table/tbody/tr[1]/td/form/table/tbody[3]/tr[2]/td/table/tbody/tr/td[1]/a/img')

class changeframes:

     class changeframe1(WebElement):
      (by, value) = (By.ID, 'nav')

     class changeframe2(WebElement):
      (by, value) = (By.ID, 'framecontent')

class register:
     class hygl(WebElement):
        (by,value) = (By.LINK_TEXT,u'会员管理')

     class hyzc(WebElement):
        (by, value) = (By.LINK_TEXT, u'会员注册')

     class begin(WebElement):
        (by,value) = (By.XPATH,"//img[contains(@id,'welcomeRegOk')]")

     class loginname(WebElement):
        (by,value) = (By.ID,'loginName')












