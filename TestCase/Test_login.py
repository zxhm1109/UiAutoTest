#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/10/28 18:34 
# @File      : Test_login.py 
# @desc      : 登录功能测试用例（账号密码登录、手机号验证码登录）

url = 'https://t2wxapi.sancell.top/saas-back/#/login'

import unittest
from Pageobject import login_page, index_page, category_page
from common.Brower import brower
from ddt import ddt, data
from common.rw_yaml import *
from common.BasePage import *


@ddt
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = brower.chrome(url)

    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self):
        self.driver.implicitly_wait(20)

    def tearDown(self):
        time.sleep(1)

    # @data()
    def test_isthelogin(self):
        loginpage = login_page.LoginPage(self.driver)
        loginpage.verify_input(1)


if __name__ == '__main__':
    unittest.TestCase()
