#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/6 11:04
# @File      : loginpage_loc.py
# @desc      :

from selenium.webdriver.common.by import By


class loginpage_locators:
    '''
    登录页面元素集合
    '''
    username_ele = (By.XPATH, '//*[@name="username"]')
    password_ele = (By.XPATH, "//*[@name='password']")
    login_ele = (By.XPATH, "//*[@class='el-button el-button--primary']")
    imgcode_ele = (By.XPATH, "//img[@class='el-image__inner']")
    input_imgcode_ele = (By.XPATH, '//*[@placeholder="验证码"]')
    login_error_ele = (By.XPATH, "/html/body/div[2]/p")

    button_passlogin_ele=(By.XPATH,"//*[@class='el-tabs__item is-active']")



if __name__ == '__main__':
    pass
