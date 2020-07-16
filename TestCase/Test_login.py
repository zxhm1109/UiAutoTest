#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/9 16:46
# @File      : Test_login.py
# @desc      :

import unittest
from Pageobject import login_page, index_page, category_page
from common.Brower import brower
from ddt import ddt, data
from common.rw_yaml import *
from common.BasePage import *

login_fault_casedata, login_fault_url = get_case_data('login_fault')
login_succeed_casedata, login_succeed_url = get_case_data('login_succeed')
category_add_casedata, category_add_url = get_case_data('category_add')
category_edit_casedata, category_edit_url = get_case_data('category_edit')
category_L2_add_casedata, category_L2_add_url = get_case_data('category_L2_add')
category_L3_add_casedata, category_L3_add_url = get_case_data('category_L3_add')


@ddt
class test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = brower.chrome(login_fault_url)

    @classmethod
    def tearDownClass(cls):
        logger.info('----------{}执行完毕，关闭浏览器----------'.format(__name__))
        cls.driver.close()

    def setUp(self):
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(1)

    @data(*login_fault_casedata)
    def test_1_login_fault(self, casedata):
        '''
        账号密码登录功能测试用例_异常
        :param casedata:
        :return:
        '''
        loginpage = login_page.LoginPage(self.driver)
        loginpage.operate_login(casedata['username'], casedata['password'], casedata['access_token'])
        if '$' in casedata['assert']:
            self.assertTrue(index_page.IndexPage(self.driver).button_top_right_user())
        else:
            self.assertEqual(loginpage.check_login_error_msg(), casedata['assert'])
        time.sleep(4)

    @data(*login_succeed_casedata)
    def test_2_login_succeed(self, login_succeed_casedata):
        '''
        账号密码登录功能测试用例_正常
        :return:
        '''
        loginpage = login_page.LoginPage(self.driver)
        loginpage.operate_login(login_succeed_casedata['username'], login_succeed_casedata['password'],
                                login_succeed_casedata['access_token'])
        try:
            self.assertTrue(index_page.IndexPage(self.driver).button_top_right_user())
        except NoSuchElementException:
            unittest.main()

    def test_3_index(self):
        '''
        打开分类管理菜单
        :return:
        '''
        # index = index_page.IndexPage(self.driver)
        category = category_page.CategoryPage(self.driver)
        category.open_menu()
        self.assertTrue(category.check_page_path())

    @data(*category_add_casedata)
    def test_4_category_stair_add(self, category_casedata):
        '''
        创建一级分类功能用例
        :param category_casedata:
        :return:
        '''
        category = category_page.CategoryPage(self.driver)
        category.add_stair_category(category_casedata['g_name'], category_casedata['g_keywords'], category_casedata['g_img'],
                                    category_casedata['g_desc'],
                                    category_casedata['g_sort'])
        if '$' in category_casedata['assert']:
            self.assertTrue(category.check_gname_in_glist(category_casedata['g_name']))
        else:
            self.assertIn(category_casedata['assert'], category.check_add_edit_error())
        time.sleep(0.5)
        self.driver.refresh()

    @data(*category_edit_casedata)
    def test_5_category_L1_edit(self, category_edit_casedata):
        '''
        编辑一级分类功能用例
        :return:
        '''
        category = category_page.CategoryPage(self.driver)
        category.edit_L1_category(category_edit_casedata['g_name'], category_edit_casedata['g_keywords'],
                                  category_edit_casedata['g_img'],
                                  category_edit_casedata['g_desc'],
                                  category_edit_casedata['g_sort'])

        if '$' in category_edit_casedata['assert']:
            self.assertTrue(category.check_gname_in_glist(category_edit_casedata['g_name']))
        else:
            self.assertIn(category_edit_casedata['assert'], category.check_add_edit_error())

    @data(*category_L2_add_casedata)
    def test_6_category_L2_add(self, category_L2_add_casedata):
        category = category_page.CategoryPage(self.driver)
        category.add_L2_category(category_L2_add_casedata['g_name'], category_L2_add_casedata['g_keywords'],
                                 category_L2_add_casedata['g_img'],
                                 category_L2_add_casedata['g_desc'],
                                 category_L2_add_casedata['g_sort'])
        self.assertTrue(category.check_gname_in_glist(category_L2_add_casedata['g_name']))

    @data(*category_L3_add_casedata)
    def test_7_category_L3_add(self,category_L3_add_casedata):
        category = category_page.CategoryPage(self.driver)
        category.add_L3_category(category_L3_add_casedata['g_name'], category_L3_add_casedata['g_keywords'],
                                 category_L3_add_casedata['g_img'],
                                 category_L3_add_casedata['g_desc'],
                                 category_L3_add_casedata['g_sort'])
        self.assertTrue(category.check_gname_in_glist(category_L3_add_casedata['g_name']))

    def test_8_category_del(self):
        pass

if __name__ == '__main__':
    unittest.main()
