# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/11 14:38
# @File      : Run.py
# @desc      :


from common import HTMLTestRunnerNew
from common.logger import Mylog
import unittest
from common.DoConfig import Get_path

logger = Mylog()


def run():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    from TestCase import Test_login
    suite.addTest(
        loader.loadTestsFromTestCase(Test_login.test_login))
    # 生成HTML报告
    with open(Get_path.get_report_path(), 'wb') as ff:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=ff, verbosity=2, title='Ui Test Report',
                                                  description='测试报告', tester='zhaofy')
        runner.run(suite)


if __name__ == '__main__':
    run()
