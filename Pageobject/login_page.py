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
from selenium.webdriver.common.by import By

# 密码登录Tip按钮
ele_passlogin_button = (By.XPATH, "//*[contains(text(),'密码登录')]")
ele_account_input = (By.XPATH, '//*[@placeholder="账号"]')
ele_password_input = (By.XPATH, '//*[@placeholder="密码"]')
ele_verify_input = (By.XPATH, '//*[@placeholder="验证码"]')
ele_verify_img = (By.XPATH, '//*[@id="app"]/div[1]/form/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/a/img')

# 手机号登录Tip按钮
ele_phonelogin_button = (By.XPATH, "//*[contains(text(),'手机号登录')]")
ele_phone_input = (By.XPATH, '//*[placeholder="手机号"]')
ele_smsverify_input=(By.XPATH,'//*[placeholder="短信验证码"]')
ele_sendsms_button=(By.XPATH,"//*[contains(text(),'发送验证码')]")

# 十天免登陆勾选框
ele_rememberlogin_checkbox = (By.XPATH, '//*[@class="el-checkbox__inner"]')
# 忘记密码
ele_forgetpassword_button = (By.XPATH, '//*[@class="forgotPwd router-link-exact-active router-link-active"]')
# 登录 按钮
ele_tologin_button = (By.XPATH, '//*[@id="app"]/div[1]/form/div[2]/div[3]/div/button')

# 输入框错误提示
ele_InputError_msg = (By.XPATH, '//*[@class="el-form-item__error"]')

# 顶部弹出框错误提示
ele_TopError_msg = (By.XPATH, '//*[@class="el-message__group"]/p')


class LoginPage(BasePage):

    def input_username_send(self, username):
        '''
        输入用户名
        :param username:
        :return:
        '''
        self.input_send(*ele_account_input, username)

    def input_password_send(self, password):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.input_send(*ele_password_input, password)

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
        '''
        点击登录按钮
        :return:
        '''
        self.click(*ele_tologin_button)

    def checkbox_rememberlogin(self):
        '''
        十天内免登陆勾选
        :return:
        '''
        self.click(*ele_rememberlogin_checkbox)

    def clear_input(self, ele):
        '''
        清空输入框
        :return:
        '''
        self.clear(*ele)

    def check_login_error_msg(self):
        '''
        old 错误提示
        :return:
        '''
        ele = self.get_ele_text(*loc.login_error_ele)
        logger.info('msg:{}'.format(ele))
        return ele

    def check_input_error(self):
        '''
        输入框底部错误提示，可能存在多个
        :return:
        '''
        ele = self.get_ele_text(*ele_InputError_msg)
        logger.info('msg:{}'.format(ele))
        return ele

    def check_Top_error(self):
        '''
        页面顶部错误提示
        :return:
        '''
        ele = self.get_ele_text(*ele_TopError_msg)
        logger.info('msg:{}'.format(ele))
        return ele

    def operate_account_login(self, username, password, imgcode=None):
        '''
        输入账号、密码、验证码登录功能
        :param username:
        :param password:
        :param imgcode:
        :return:
        '''
        self.click(*ele_passlogin_button)
        self.input_username_send(username)
        time.sleep(3)
        self.input_password_send(password)
        time.sleep(3)

        # 如果给到验证码即输入该验证码，如果不给就识别输入验证码
        if imgcode is not None:
            self.input_send(*ele_verify_input, imgcode)
        else:
            self.ocr_verify_input(imgcode)
        time.sleep(3)
        self.button_login_click()
        if self.DoubleCheck_verify(imgcode):
            logger.info('登录成功：{}'.format(username))

    def ocr_verify_input(self, code=None):
        '''
        识别GIF图片验证码，并输入
        :return:
        '''
        img_path = self.screenshot_ele_png(*ele_verify_img)
        # 先处理src地址，图片转bese64
        res = base64_api(img_path)
        self.input_send(*ele_verify_input, res)

    def DoubleCheck_verify(self, code=None):
        '''
        图片识别失败/错误时，重新输入验证码登良，直至登录成功
        :param code:
        :return:
        '''
        while 'login' not in self.driver.current_url:
            try:
                if self.check_Top_error() == '验证码错误':
                    self.clear_input(ele_verify_input)
                    self.click(*ele_verify_img)
                    self.ocr_verify_input(code)
                    self.button_login_click()
            except Exception:
                return True
        else:
            return True

    def operate_phone_login(self, phone=None):
        '''
        手机号验证码登录，通过redis_connect获取短信验证码
        :param phone:
        :return:
        '''
        self.click(*ele_phonelogin_button)
        self.input_send(*ele_phone_input,phone)
        self.click(*ele_sendsms_button)
        from common.redis_connect import get_phone_code
        self.input_send(*ele_smsverify_input,get_phone_code(str(phone)))


if __name__ == '__main__':
    driver = brower.chrome(DoYaml().read('login_fault', 'url'))
    # LoginPage(driver).operate_account_login('SSBM', '8888')
    LoginPage(driver).operate_phone_login()
