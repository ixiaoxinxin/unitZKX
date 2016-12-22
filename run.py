# -*- coding: utf-8 -*-

import executer
import config
import testcase

# executer.run(conf.MSWindows, testcase.validations.TestCase001_NormalInputTest)
# executer.run(conf.ChromeDemo, testcase.validations.TestCase002_Data_In_Excel)


executer.run(config.IEDriverServer, testcase.feeTest)










