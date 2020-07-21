#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/10 11:04
# @File      : BasePage.py
# @desc      :

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
import time
import os.path
from common.logger import Mylog
from selenium.common.exceptions import NoSuchElementException
from common.DoConfig import *
from common.tool import upload

logger = Mylog()


# 公共方法
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # 等待元素可见
    def wait_ele_visible(self, k, v):
        try:
            self.wait.until(EC.visibility_of_element_located((k, v)))
        except Exception as e:
            raise e

    def wait_elePresence(self, k, v):
        """
        显示等待页面元素存在
        :param locatorMethod:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            self.wait.until(EC.presence_of_element_located((k, v)))
        except Exception as e:
            raise e

    # 退出浏览器
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 浏览器刷新
    def refresh(self):
        self.driver.refresh()

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器")
        except Exception as e:
            logger.error("关闭浏览器窗口失败： %s" % e)

    # 保存截图
    def get_windows_img(self):

        try:
            self.driver.get_screenshot_as_file(Get_path.get_screenshot_path())
            logger.info("咔嚓！！")
        except Exception as e:
            logger.error("截图失败： %s" % e)
            self.get_windows_img()

    # 定位元素
    def get_element(self, k, v):
        try:
            self.wait_ele_visible(k, v)
            element = self.driver.find_element(k, v)
            return element
        except Exception as e:
            logger.error("元素定位失败: %s" % e)
            self.get_windows_img()

    # 定位多个元素
    def get_elements(self, k, v):

        try:
            self.wait_ele_visible(k, v)
            element = self.driver.find_elements(k, v)
            return element
        except Exception as e:
            logger.error("元素定位失败: %s" % e)
            self.get_windows_img()

    # 定位输入框并输入
    def input_send(self, k, v, text):
        if text is not None:
            el = self.get_element(k, v)
            self.clear(k, v)
            try:
                self.driver.find_element(k, v).send_keys(text)
            except Exception as e:
                logger.error("输入失败： %s" % e)
                self.get_windows_img()
        else:
            pass

    # 清除文本框
    def clear(self, k, v):
        el = self.get_element(k, v)
        try:
            self.driver.find_element(k, v).clear()
        except Exception as e:
            logger.error("输入框清空失败： %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, k, v):
        self.get_element(k, v)
        try:
            self.driver.find_element(k, v).click()
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)
            self.get_windows_img()

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 获取元素文本内容
    def get_ele_text(self, k, v):
        ele = self.driver.find_element(k, v)
        time.sleep(0.5)
        return ele.text

    # 获取元素属性
    def get_ele_attribute(self):
        pass

    # 上传
    def upload_file(self, k, v, filepath):
        if filepath:
            self.click(k, v)
            self.sleep(1)
            logger.info('---上传文件：{}'.format(filepath))
            upload(filepath)
            self.sleep(1)
        else:
            pass

    # 检查元素是否存在
    def isElementExist(self, k, v):
        flag = True
        try:
            self.driver.find_element(k, v)
            return flag
        except:
            flag = False
            return flag

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        # logger.info("强制等待： %d seconds" % seconds)

    @staticmethod
    def im_wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        # logger.info("隐式等待： %d seconds." % seconds)


class Waitele(object):
    '''等待封装'''

    def __init__(self, driver, wtime=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wtime)

    def wait_elePresence(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素存在
        :param locatorMethod:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            self.wait.until(EC.presence_of_element_located((locationType, locatorExpression)))
        except Exception as e:
            raise e

    def frame_to_be_available_and_switch_to_it(self, locationType, locatorExpression, *args):
        """
        检查frame是否存在，存在则切换进去
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((locationType, locatorExpression)))
        except Exception as e:
            # 抛出异常信息给上层调用者
            raise e

    def wait_elevisible(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素可见
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located((locationType, locatorExpression)))
            return element
        except Exception as e:
            raise e

    #
    # # 强制等待
    # @staticmethod
    # def sleep(seconds):
    #     time.sleep(seconds)
    #     # logger.info("强制等待： %d seconds" % seconds)

    # 隐式等待
    def im_wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        # logger.info("隐式等待： %d seconds." % seconds)
