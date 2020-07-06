#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/4 13:33
# @File      : DoConfig.py
# @desc      :

import configparser
# from common.logger import Mylog
#
# log = Mylog()】
class config_path:
    config_path = '../Data/Config.config'


class ReadConfig:

    @staticmethod
    def read_config(section, option):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(getattr(config_path,'config_path'), encoding='utf-8')
        # 根据标签、option获取值
        res = cf.get(section, option)
        return res

    @staticmethod
    def read_config_options_value(section):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(getattr(config_path,'config_path'), encoding='utf-8')
        rrr = cf.items(section)
        return rrr

    @staticmethod
    def read_config_options_list(section):
        cf = configparser.ConfigParser()
        cf.read(getattr(config_path,'config_path'), encoding='utf-8')
        opt_list = cf.options(section)
        result = []
        for opt in opt_list:
            rrr = cf.get(section, opt)
            result.append(rrr)
        return result


class WriteConfig:
    @staticmethod
    def write_config(section, option, value):
        cf = configparser.ConfigParser()
        cf.read(getattr(config_path,'config_path'), encoding='utf-8')
        cf.add_section(section)
        cf.set(section, option, value)  # 修改指定section 的option
        with open(getattr(config_path,'config_path'), 'w') as f:
            cf.write(f)
        return True


if __name__ == '__main__':
    logpath = ReadConfig.read_config('file_path','log_path')
    print(logpath)
