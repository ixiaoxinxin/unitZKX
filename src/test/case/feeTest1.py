import unittest

from elements.feePage import feePage




class feeTest(feePage,unittest.TestCase):
    def TestCase_LoginTest_In_Excel(self):
        xls = datadriver.ExcelSheet("users.xls", "syusers")
        for i in range(1, xls.nrows()):
            username   = xls.cell(i, "username")
            passwd    = xls.cell(i, "passwd")

            #### login ###
