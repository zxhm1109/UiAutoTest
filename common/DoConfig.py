#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/4 13:33
# @File      : DoConfig.py
# @desc      :

import configparser, os, time


def config_path():
    config_path = os.path.abspath(os.path.dirname(__file__)).split('UiAutoTest')[0] + 'UiAutoTest\Data\Config.config'
    return config_path


class ReadConfig:

    @staticmethod
    def read_config(section, option):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(config_path(), encoding='utf-8')
        # 根据标签、option获取值
        res = cf.get(section, option)
        return res

    @staticmethod
    def read_config_options_value(section):
        # 读取config文件
        cf = configparser.ConfigParser()
        cf.read(config_path(), encoding='utf-8')
        rrr = cf.items(section)
        return rrr

    @staticmethod
    def read_config_options_list(section):
        cf = configparser.ConfigParser()
        cf.read(config_path(), encoding='utf-8')
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
        cf.read(config_path(), encoding='utf-8')
        cf.add_section(section)
        cf.set(section, option, value)  # 修改指定section 的option
        with open(config_path(), 'w') as f:
            cf.write(f)
        return True


class Get_path:
    project_path = os.path.abspath(os.path.dirname(__file__)).split('UiAutoTest')[0]
    log = ReadConfig.read_config('file_path', 'log_path')
    report = ReadConfig.read_config('file_path', 'report_path')
    conf = 'UiAutoTest\Data\Config.config'
    yaml = ReadConfig.read_config('file_path', 'yaml_path')
    screenshot = ReadConfig.read_config('file_path', 'screenshot_path')

    @classmethod
    def get_report_path(cls):
        report = os.path.join(cls.project_path, cls.report)
        if not os.path.exists(report):
            os.makedirs(report)
        # report_path = os.path.join(report, str(time.strftime('%Y%m%d%H%M%S', time.localtime())) + '_UiAutoTest.html')
        report_path = os.path.join(report, str(time.strftime('%Y%m%d%H', time.localtime())) + '_UiAutoTest.html')
        return report_path

    @classmethod
    def get_config_path(cls):
        return os.path.join(cls.project_path, cls.conf)

    @classmethod
    def get_log_path(cls):
        logpath = os.path.join(cls.project_path, cls.log)
        if not os.path.exists(logpath):
            os.makedirs(logpath)
        log_path = os.path.join(logpath,
                                str(time.strftime('%Y%m%d', time.localtime())) + '_UiAutoTest.log')
        return log_path

    @classmethod
    def get_yaml_path(cls):
        return os.path.join(cls.project_path, cls.yaml)

    @classmethod
    def get_screenshot_path(cls):
        screenshotpath = cls.project_path + cls.screenshot
        if not os.path.exists(screenshotpath):
            os.makedirs(screenshotpath)
        path = os.path.join(screenshotpath, str(time.strftime('%Y%m%d%H%M%S', time.localtime())) + '.png')
        return path


if __name__ == '__main__':
    # logpath = ReadConfig.read_config('file_path', 'log_path')
    # print(logpath)
    a = Get_path.get_screenshot_path()
    print(a)
