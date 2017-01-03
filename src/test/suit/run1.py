# -*- coding: utf-8 -*-

import config
import testcase

from src.test.common import executer

# executer.run(conf.MSWindows, testcase.validations.TestCase001_NormalInputTest)
# executer.run(conf.ChromeDemo, testcase.validations.TestCase002_Data_In_Excel)


executer.run(config.IEDriverServer, testcase.feeTest)










