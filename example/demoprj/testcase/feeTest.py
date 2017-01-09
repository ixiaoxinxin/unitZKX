# -*- coding: utf-8 -*-

from example.demoprj.page import feePage


def TestCase001_sousuo():
    feePage.Login.username.Set("sxxykhjl")
    feePage.Login.passwd.Set("111111")
    feePage.Login.username.Click()
