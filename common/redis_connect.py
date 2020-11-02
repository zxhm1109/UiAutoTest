#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/21 15:45
# @File      : redis_connect.py
# @desc      :

import redis, time
from common.DoConfig import *
from common.logger import Mylog
from common.rw_yaml import DoYaml

logger = Mylog()


def redis_conn(key):
    # 测试环境
    if DoYaml('BaseData').read('base', 'env') == 'test':
        redisparms = ReadConfig.read_config_options_dict('test_redis')
    # 预发环境
    elif DoYaml('BaseData').read('base', 'env') == 'pre':
        redisparms = ReadConfig.read_config_options_dict('pre_redis')
    else:
        return ValueError('请检查BaseData环境参数是否正常！')
    conn = redis.Redis(host=redisparms['host'], port=redisparms['port'], password=redisparms['password'], db=1)
    result = conn.get(key)
    return result


def get_phone_code(phone):
    b = redis_conn('ssxq:PIN:' + phone)
    logger.info('短信验证码：{}'.format(int(b)))
    return b


def get_img_code(key):
    # 获取图片验证码
    b = str(redis_conn('saas:captcha:' + key))[-5:-1]
    # WriteConfig.write_config('Base', 'ImgCode', str(b))
    logger.info('图片验证码：{}，写入conf文件成功'.format(b))
    return b


if __name__ == '__main__':
    a = 'ssxq:PIN:17777777773'
    # result = get_img_code('saas:captcha:15145e5cba11433ca23ac530afe78f1c')
    result = get_phone_code(a)
    print(int(result))
