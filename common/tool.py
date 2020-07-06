#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/4 16:13
# @File      : tool.py
# @desc      :

import time,os


def load_img(img_path):
    from urllib import request
    res = request.Request(img_path)
    data = request.urlopen(res, timeout=10).read()
    path="../Data/img/"
    img = "img-{}.gif".format(str(nowtimestr()))
    if not os.path.exists(path):
       os.makedirs(path)
    with open(path+img, 'wb') as f:
        f.write(data)
    return path+img


def nowtimestr():
    strtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return strtime


if __name__ == '__main__':
    load_img(
        'http://192.168.200.104:9900/api-uaa/validata/code/1242764A-783B-4374-B24E-077B6ECB2737?t=1593853142000')
