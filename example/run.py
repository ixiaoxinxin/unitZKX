from ixiaoxinxin import executer

from example.demoprj import conf

from example.demoprj.testcase import eg1,feeTest

executer.run(conf.IEDriverServer,feeTest)