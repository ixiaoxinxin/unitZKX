# -*- coding: utf-8 -*-

from example.demoprj.page import feePage


def TestCase001_sousuo():
    feePage.Login.kw.Set("https://www.baidu.com")
    feePage.Login.su.Click()
