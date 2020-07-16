#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/15 14:05
# @File      : categorypage_loc.py
# @desc      :

from selenium.webdriver.common.by import By


class CategoryPage_locators:
    # 顶部错误提示
    category_error_ele = (By.XPATH, "//*[@class='el-message el-message--error']")
    # 创建一级分类按钮
    button_add_L1_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[2]/button[2]")
    # 分类名称输入框
    input_category_name_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[2]/form/div[1]/div/div/input")
    # 分类搜索关键字输入框
    input_category_keywords_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[2]/form/div[2]/div/div/input")
    # 分类描述输入框
    input_category_desc_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[2]/form/div[4]/div/div/textarea")
    # 分类排序值输入框
    input_category_sort_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[2]/form/div[5]/div/div/div/input")
    # 分类创建/编辑 确认按钮
    button_submit_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[3]/div/button[2]")
    # 分类创建/编辑 取消按钮
    button_cancel_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[3]/div/button[1]")
    # 分类图片上传按钮
    button_img_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[2]/form/div[3]/div/div/div[1]")
    # 侧边导航栏-商品管理按钮
    button_menu_1 = (By.XPATH, "//div[@id='app']/div/div/div/div/div/ul/div[2]/li/div")
    # 侧边导航栏-类别列表按钮
    button_menu_2 = (By.XPATH, "//div[@id='app']/div/div/div/div/div/ul/div[2]/li/ul/div/a/li")
    # 添加二级分类按钮（默认第一个分类）
    button_add_L2_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[7]/div/button[1]")
    # 删除一级分类按钮（默认第一个）
    button_del_L1_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[7]/div/button[3]")
    # 删除二级分类按钮（第一个有二级的一级分类）
    button_del_L2_ele = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[2]/td[7]/div/button[3]')
    # 删除三级分类按钮 （第一个有二级、三级的分类）
    button_del_L3_ele = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[3]/td[7]/div/button[3]')
    # 删除分类 确认按钮
    button_del_confirm_ele = (By.XPATH, "/html/body/div[2]/div/div[3]/button[2]")
    # 删除分类 取消按钮
    button_del_cancel_ele = (By.XPATH, "/html/body/div[2]/div/div[3]/button[1]")
    # 编辑一级分类按钮（默认第一个）
    button_edit_L1_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[7]/div/button[2]")
    # 一级分类是否隐藏 开关按钮（默认第一个）
    button_hide_L1_ele = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/div/span")
    # 列表页分类名称（全部）
    g_name_eles = (By.XPATH, "//*[@class='el-table_1_column_2  ']")
    # 编辑、创建分类输入框错误提示
    error_add_edit_msg_eles = (By.XPATH, "//*[@class='el-form-item__error']")
    # 页面顶部路径
    top_path_name_ele = (By.XPATH, '//*[@class="no-redirect"]')
    # 展开二级分类（默认第一个一级分类）
    button_unfold_L2_ele = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[1]/div/div')
    # 展开三级分类（默认第一个一级分类的第一个二级分裂）
    button_unfold_L3_ele = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[2]/td[1]/div/div')
    # 创建三级分类按钮
    button_add_L3_ele = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[2]/td[7]/div/button[1]')

    # 第一个一级分类 显示状态
    status_L1_show = (By.XPATH, "//*[contains(@class='is-center')]//div[contains(@class='el-switch')]")
    # 第一个一级分类 隐藏状态
    status_L1_hide = (By.XPATH, "//*[@class='el-table__row']//div[contains@class,'el-switch is-checked']")
