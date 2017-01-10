# -*- coding: utf-8 -*-

from example.demoprj.page import feePage
from ixiaoxinxin import Basepage

def TestCase001():
    feePage.Login.username.Set("sxxykhjl")
    feePage.Login.passwd.Set("111111")
    feePage.Login.username.Click()
    Basepage.WebBrowser.SwitchToFrame(feePage.changeframes.changeframe1.value)
    feePage.register.hygl.Click()
    feePage.register.hyzc.Click()
    feePage.register.begin.Click()
    feePage.register.loginname.Set("AAA")
