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
from common.tool import del_data_img
logger = Mylog()


def run():
    # 清理一个月前的code_img 和截图
    del_data_img(Get_path.get_coed_img_path())
    del_data_img(Get_path.get_screenshot_path())

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    from TestCase import Test_category_login,Test_product_setmeal
    suite.addTest(
        loader.loadTestsFromTestCase(Test_category_login.test_category_login))
    unittest.TextTestRunner(verbosity=2)
    # 生成HTML报告
    with open(Get_path.get_report_path(), 'wb') as ff:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=ff, verbosity=2, title='Ui Test Report',
                                                  description='测试报告', tester='zhaofy')

    runner.run(suite)


if __name__ == '__main__':
    run()
