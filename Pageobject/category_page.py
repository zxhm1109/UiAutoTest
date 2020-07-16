#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/15 14:04
# @File      : category_page.py
# @desc      :

from PageLocators.categorypage_loc import CategoryPage_locators as loc
from common.BasePage import BasePage
from common.logger import Mylog

logger = Mylog()


class CategoryPage(BasePage):

    # 分类列表页顶部错误提示
    def check_list_error_msg(self):
        ele = self.get_ele_text(*loc.category_error_ele)
        return ele

    # 点击菜单 打开分类页面
    def open_menu(self):
        self.click(*loc.button_menu_1)
        self.click(*loc.button_menu_2)

    # 添加一级分类
    def add_stair_category(self, name, keywords, img, desc, sort):
        self.click(*loc.button_add_L1_ele)
        self.input_send(*loc.input_category_name_ele, name)
        self.input_send(*loc.input_category_keywords_ele, keywords)
        self.upload_file(*loc.button_img_ele, img)
        self.input_send(*loc.input_category_desc_ele, desc)
        self.input_send(*loc.input_category_sort_ele, sort)
        self.click(*loc.button_submit_ele)

    # 检查分类名称是否在分类列表中
    def check_gname_in_glist(self, gname):
        ele = self.get_elements(*loc.g_name_eles)
        for name in ele:
            self.sleep(0.5)
            if gname == name.text:
                return True
        else:
            return False

    # 编辑排在第一个的一级分类
    def edit_L1_category(self, name, keywords, img, desc, sort):
        self.click(*loc.button_edit_L1_ele)
        self.input_send(*loc.input_category_name_ele, name)
        self.input_send(*loc.input_category_keywords_ele, keywords)
        self.upload_file(*loc.button_img_ele, img)
        self.input_send(*loc.input_category_desc_ele, desc)
        self.input_send(*loc.input_category_sort_ele, sort)
        self.click(*loc.button_submit_ele)

    # 检查创建/编辑分类弹框中的输入框错误提示
    def check_add_edit_error(self):
        msgs = self.get_elements(*loc.error_add_edit_msg_eles)
        err_list = []
        for msg in msgs:
            err_list.append(msg.text)
        return err_list

    # 在排在第一个的一级分类下添加二级分类
    def add_L2_category(self, name, keywords, img, desc, sort):
        self.click(*loc.button_add_L2_ele)
        self.input_send(*loc.input_category_name_ele, name)
        self.input_send(*loc.input_category_keywords_ele, keywords)
        self.upload_file(*loc.button_img_ele, img)
        self.input_send(*loc.input_category_desc_ele, desc)
        self.input_send(*loc.input_category_sort_ele, sort)
        self.click(*loc.button_submit_ele)

    # 在第一个一级分类的第一个二级分类下添加三级分类
    def add_L3_category(self, name, keywords, img, desc, sort):
        self.click(*loc.button_unfold_L2_ele)
        self.click(*loc.button_add_L3_ele)
        self.input_send(*loc.input_category_name_ele, name)
        self.input_send(*loc.input_category_keywords_ele, keywords)
        self.upload_file(*loc.button_img_ele, img)
        self.input_send(*loc.input_category_desc_ele, desc)
        self.input_send(*loc.input_category_sort_ele, sort)
        self.click(*loc.button_submit_ele)

    # 删除排在第一个的一级分类
    def del_L1_category(self):
        self.click(*loc.button_del_L1_ele)
        self.click(*loc.button_del_confirm_ele)

    #删除第一个一级分类下的第一个二级分类
    def del_L2_category(self):
        self.click(*loc.button_del_L2_ele)
        self.click(*loc.button_del_confirm_ele)

    # 删除第一个一级分类下的第一个二级分类的第一个三级分类
    def del_L3_category(self):
        self.click(*loc.button_del_L3_ele)
        self.click(*loc.button_del_confirm_ele)

    # 隐藏/显示 排在第一个的一级分类
    def hide_L1_category(self):
        self.click(*loc.button_hide_L1_ele)


    # 检查页面顶部路径
    def check_page_path(self):
        res = self.isElementExist(*loc.top_path_name_ele)
        return res
