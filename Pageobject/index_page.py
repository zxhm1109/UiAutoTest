#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/14 19:23
# @File      : index_page.py
# @desc      :

from common.Brower import brower
from common.rw_yaml import DoYaml
from common.img_code import base64_api
from common.tool import *
from common.BasePage import *
from PageLocators.indexpage_loc import IndexPage_Locators as loc


class IndexPage(BasePage):

    def button_top_right_user(self):

        ele = self.get_ele_text(*loc.button_top_right_user_ele)
        logger.info(ele)
        return ele

    def get_menu_dict(self):
        ele = self.get_elements(*loc.menu_list_ele)
        menulist = []
        for i in ele:
            menulist.append(i.text)
        logger.info('菜单列表：{}'.format(menulist))
        return ele

    def button_menu_click(self, menuname):
        try:
            if menuname =='catehory':
                self.click(*loc.product)
                time.sleep(0.5)
                self.click(*loc.categroy)
                return True
        except Exception as e:
            return False

    def check_error_message(self):
        ele = self.get_element(*loc.index_error_ele)
        return ele.text


if __name__ == '__main__':
    IndexPage.button_top_right_user()
