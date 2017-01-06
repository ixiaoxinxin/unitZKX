#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
import xlrd
import unittest

#读取测试数据
fname = "E:\\testInfo\\userInfo.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
sh = bk.sheet_by_name(u"testInfoSY")

class register(unittest.TestCase):
    for i in range(sh.nrows):
        iedriver = os.path.abspath("C:\Program Files\Internet Explorer\IEDriverServer")
        os.environ[ "webdriver.ie.driver"] = iedriver
        browser = webdriver.Ie(iedriver)    
        url= "http://172.16.4.247:27002"
        browser.get(url)
        browser.find_element_by_id( "j_username" ).clear()
        browser.find_element_by_name( "j_username" ).send_keys("sxxykhjl")
        browser.find_element_by_id( "j_password" ).clear()
        browser.find_element_by_name( "j_password" ).send_keys( "111111" )
        #点击登录按钮
        browser.find_element_by_xpath("// img[contains( @onclick,'loginCheck()')]" ).click()
        time.sleep(4)
        #登陆成功，打开会员注册页面
        browser.implicitly_wait(30)
        browser.switch_to_frame("nav")
        time.sleep(4)
        browser.find_element_by_link_text(u"会员管理").click()
        time.sleep(4)
        browser.find_element_by_link_text(u"会员注册").click()
        time.sleep(4)
        #填写会员注册信息
        browser.implicitly_wait(30) #切换frame之前必须添加此句代码
        browser.switch_to_default_content()
        browser.switch_to_frame("framecontent")
        time.sleep(3)
        browser.find_element_by_xpath("//img[contains(@id,'welcomeRegOk')]" ).click()
        time.sleep(3)
        #-----录入信息开始------
        browser.find_element_by_id( "loginName" ).clear()
        browser.find_element_by_id( "loginName" ).send_keys(sh.cell_value(i,0))
        time.sleep(2)
        browser.find_element_by_id( "password" ).clear()
        browser.find_element_by_id( "password" ).send_keys(int(sh.cell_value(i,1)))
        time.sleep(2)
        browser.find_element_by_id( "passwordConfirm" ).clear()
        browser.find_element_by_id( "passwordConfirm" ).send_keys(int(sh.cell_value(i,2)))
        time.sleep(2)
        browser.find_element_by_id( "hospitalName" ).clear()
        browser.find_element_by_id( "hospitalName" ).send_keys(sh.cell_value(i,3))
        time.sleep(2)
        browser.find_element_by_id( "registeredAddress" ).clear()
        browser.find_element_by_id( "registeredAddress" ).send_keys(int(sh.cell_value(i,4)))
        time.sleep(2)
        selectc = browser.find_element_by_id( "cityCodeOper" )
        allOptionsc = selectc.find_elements_by_tag_name("option" )
        for option in allOptionsc:
            if sh.cell_value(i,5) in option.text:
                option.click()
        time.sleep(2)
        browser.find_element_by_id( "areaCodeOper" ).click()#点击一下下拉框刷新出该地区下的所有选项
        time.sleep(2)
        selecta = browser.find_element_by_id( "areaCodeOper" )
        allOptionsa = selecta.find_elements_by_tag_name("option" )
        for option in allOptionsa:
            if sh.cell_value(i,6) in option.text:
                option.click()
        time.sleep(2)
        browser.find_element_by_id( "postcode").clear()
        browser.find_element_by_id( "postcode" ).send_keys(sh.cell_value(i,7))
        time.sleep(2)
        browser.find_element_by_id( "lawMan" ).clear()
        browser.find_element_by_id( "lawMan" ).send_keys(sh.cell_value(i,8))       
        time.sleep(2)
        Select(browser.find_element_by_id("owershipType")).select_by_visible_text(sh.cell_value(i,9))
        time.sleep(2)
        Select(browser.find_element_by_id("note")).select_by_visible_text(sh.cell_value(i,10))
        time.sleep(2)
        selectl = browser.find_element_by_id( "levelOneCodes" )
        allOptionsl = selectl.find_elements_by_tag_name("option" )
        for option in allOptionsl:
            if sh.cell_value(i,11) in option.text:
                option.click()
        time.sleep(2)
        if browser.find_element_by_id("otherHospital") == '':
            time.sleep(2)      
        else: 
            time.sleep(2) 
            browser.find_element_by_id("levelTwoCodes").click() #点击一下下拉框刷新出该地区下的所有选项
            time.sleep(2) 
            allOptionsll = browser.find_element_by_id("levelTwoCodes").find_elements_by_tag_name("option")
            for option in allOptionsll:
                if sh.cell_value(i,12) in option.text:
                    option.click()
                time.sleep(2)
        Select(browser.find_element_by_id("surgeryId")).select_by_visible_text(sh.cell_value(i,13))
        time.sleep(2)
        Select(browser.find_element_by_id("mliTypePara")).select_by_visible_text(sh.cell_value(i,14))
        time.sleep(2)
        browser.find_element_by_id( "orgLicenseNo" ).clear()
        browser.find_element_by_id( "orgLicenseNo" ).send_keys(int(sh.cell_value(i,15)))
        time.sleep(2)
        browser.find_element_by_id("orgLicenseNoCFile" ).clear()
        browser.find_element_by_id( "orgLicenseNoCFile" ).send_keys(sh.cell_value(i,16))
        time.sleep(2)
        browser.find_element_by_id("organizationCode" ).clear()
        browser.find_element_by_id( "organizationCode" ).send_keys(int(sh.cell_value(i,17)))
        time.sleep(2)
        browser.find_element_by_id("organizationCodeFile" ).clear()
        browser.find_element_by_id( "organizationCodeFile" ).send_keys(sh.cell_value(i,18))
        time.sleep(2)
        if Select(browser.find_element_by_id("owershipType")) == '营利':
            browser.find_element_by_id("businessLicenseNo" ).clear()
            browser.find_element_by_id( "businessLicenseNo" ).send_keys(int(sh.cell_value(i,19)))
            time.sleep(2)
            browser.find_element_by_id("businessLicenseNoFile" ).clear()
            browser.find_element_by_id( "businessLicenseNoFile" ).send_keys(sh.cell_value(i,20))
            time.sleep(2)
        else:
            time.sleep(2)
        browser.find_element_by_id( "name" ).clear()
        browser.find_element_by_id( "name" ).send_keys(sh.cell_value(i,21))
        time.sleep(2)
        browser.find_element_by_id( "cellPhone" ).clear()
        browser.find_element_by_id( "cellPhone" ).send_keys(int(sh.cell_value(i,22)))
        time.sleep(2)
        browser.find_element_by_id( "email" ).clear()
        browser.find_element_by_id( "email" ).send_keys(sh.cell_value(i,23))
        #-----录入信息结束---------
        #-----输入验证码------
        browser.find_element_by_id( "validateCode" ).click()
        #********此处应该添加等待信息*********       
        browser.implicitly_wait(30)
        time.sleep(20)
        #----勾选同意并点击提交-----
        browser.find_element_by_id("zcjc").click()
        time.sleep(3)
        browser.find_element_by_xpath("/html/body/center/div/form/div/div[1]/div/table[4]/tbody/tr[4]/td[2]/input").click()      
        time.sleep(10)
        browser.quit()
        
        
        
if __name__ == "__main__":
        for i in range(sh.nrows):
                register