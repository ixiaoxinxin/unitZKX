# -*- coding: utf-8 -*-

from example.demoprj.page import feePage
from ixiaoxinxin import Basepage
import time

def TestCase001():
    feePage.Login.username.Set("sxxykhjl")
    time.sleep(2)
    feePage.Login.passwd.Set("111111")
    time.sleep(2)
    feePage.Login.ok.Click()
    time.sleep(2)
    Basepage.WebBrowser.SwitchToFrame(feePage.changeframes.changeframe1.value)
    feePage.register.hygl.Click()
    feePage.register.hyzc.Click()
    feePage.register.begin.Click()
    feePage.register.loginname.Set("AAA")
