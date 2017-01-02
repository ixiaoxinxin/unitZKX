# -*- coding: utf-8 -*-
from src.test.common import Basepage
from src.test.suit import run
import unittest


class Toubao(Basepage):
    (by,value)=(By.ID, 'j_username')
    (by, value)=(By.ID, 'j_password')
    (by,value)=(By.XPATH, '/html/body/table[5]/tbody/tr/td[7]/table/tbody/tr[1]/td/form/table/tbody[3]/tr[2]/td/table/tbody/tr/td[1]/a/img')












