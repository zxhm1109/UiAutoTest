#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/4 16:13
# @File      : tool.py
# @desc      :

import time, os
from common.logger import Mylog

logger = Mylog()


def load_img(img_path):
    from urllib import request
    res = request.Request(img_path)
    data = request.urlopen(res, timeout=10).read()
    path = "../Data/img/"
    img = "img-{}.gif".format(str(nowtimestr()))
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + img, 'wb') as f:
        f.write(data)
    return path + img


def nowtimestr():
    strtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return strtime


import win32con
import win32gui


def upload(filePath, browser_type="chrome"):
    '''
    通过pywin32模块实现文件上传的操作
    :param filePath: 文件的绝对路径
    :param browser_type: 浏览器类型（默认值为chrome）
    :return:
    '''
    logger.info("上传文件地址：{}".format(filePath))
    if browser_type.lower() == "chrome":
        title = "打开"
    elif browser_type.lower() == "firefox":
        title = "文件上传"
    elif browser_type.lower() == "ie":
        title = "选择要加载的文件"
    else:
        title = ""  # 这里根据其它不同浏览器类型来修改

    # 找元素
    # 一级窗口"#32770","打开"
    dialog = win32gui.FindWindow("#32770", title)
    # 向下传递
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

    # 输入文件的绝对路径，点击“打开”按钮
    time.sleep(0.5)
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
    time.sleep(0.5)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
    logger.info('-----文件上传完成：{}'.format(filePath))


if __name__ == '__main__':
    load_img(
        'http://192.168.200.104:9900/api-uaa/validata/code/1242764A-783B-4374-B24E-077B6ECB2737?t=1593853142000')
