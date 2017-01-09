from ixiaoxinxin import executer

from example.demoprj import conf

from example.demoprj.testcase import feeTest

executer.run(conf.IEDriverServer,feeTest)