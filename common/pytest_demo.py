#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/14 14:59
# @File      : pytest_demo.py
# @desc      :


import unittest
from Pageobject import login_page
from common.Brower import brower
from ddt import ddt, data
from common.rw_yaml import *
from common.BasePage import *
import pytest
from common.logger import Mylog

logger = Mylog()

casedata, url = get_case_data()


class test_login():

    @classmethod
    def setUpClass(cls):
        print('-----------------------开始执行用例-----------------------------')
        cls.driver = brower.chrome(url)
        Waitele(cls.driver).im_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('---------------------用例执行完毕，关闭浏览器--------------------')

    def setUp(self):
        BasePage(self.driver).refresh()

    def tearDown(self):
        time.sleep(5)

    @pytest.mark.parametrize(*casedata)
    def test_login_normal_1(self, casedata):
        print('---------执行：{}---------'.format(casedata['casename']))
        loginpage = login_page.LoginPage(self.driver)
        loginpage.input_username_send(casedata['username'])
        loginpage.input_password_send(casedata['password'])
        loginpage.button_login_click()
        result = loginpage.check_login_error_msg()
        logger.info(result)
        assert result == True
        print('---------{}：执行完毕---------'.format(casedata['casename']))


if __name__ == '__main__':
    pytest.main()
