#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/14 19:23
# @File      : indexpage_loc.py
# @desc      :
from selenium.webdriver.common.by import By


class IndexPage_Locators:
    '''
    首页元素集合
    '''
    button_top_right_user_ele = (By.XPATH, "//*[@class='avatar-wrapper el-dropdown-selfdefine']")
    menu_list_ele = (By.XPATH, "//*[@class='el-menu-item']")
    index_error_ele = (By.XPATH, "//*[@class='el-message el-message--error']")
    product = (By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div/ul/div[2]/li/div")
    categroy = (By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[1]/a/li")
