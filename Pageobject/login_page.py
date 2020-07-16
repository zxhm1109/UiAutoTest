#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/3 18:16
# @File      : login_page.py
# @desc      :

from common.Brower import brower
from common.rw_yaml import DoYaml
from common.img_code import base64_api
from common.tool import *
from common.BasePage import *
from PageLocators.loginpage_loc import loginpage_locators as loc


class LoginPage(BasePage):

    def input_username_send(self, username):
        '''
        输入用户名
        :param username:
        :return:
        '''
        self.input_send(*loc.username_ele, username)

    def input_password_send(self, password):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.input_send(*loc.password_ele, password)

    def input_imgcode_send(self, code):
        '''
        识别GIF图片验证码，并输入
        :return:
        '''
        if code is not None:
            self.input_send(*loc.input_imgcode_ele, code)
        else:

            img_code = self.get_element(*loc.imgcode_ele)
            img_path = img_code.get_attribute('src')
            res = base64_api(load_img(img_path))
            self.input_send(*loc.input_imgcode_ele, res)

    def button_login_click(self):
        self.click(*loc.login_ele)

    def clear_input(self):
        self.clear(*loc.username_ele)
        self.clear(*loc.password_ele)
        self.clear(*loc.input_imgcode_ele)

    def check_login_error_msg(self):
        ele = self.get_ele_text(*loc.login_error_ele)
        logger.info('msg:{}'.format(ele))
        return ele

    def operate_login(self, username, password, imgcode):
        self.input_username_send(username)
        self.input_password_send(password)
        self.input_imgcode_send(imgcode)
        self.button_login_click()


if __name__ == '__main__':
    driver = brower.chrome(DoYaml().read('login', 'url'))
    # LoginPage(driver).input_username_send()
