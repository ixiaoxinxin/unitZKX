from src.test.common import executer
from config import conf
from src.test.case import feeTest

executer.run(conf.MultiBrowsersDemo, feeTest.feePage)