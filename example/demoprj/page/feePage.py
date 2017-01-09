# -*- coding: utf-8 -*-


from ixiaoxinxin.Basepage import WebElement
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













