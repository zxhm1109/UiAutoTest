#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/3 16:19
# @File      : rw_yaml.py
# @desc      :

import yaml
from common.DoConfig import ReadConfig


class DoYaml:

    def __init__(self):
        self.yamlpath = ReadConfig.read_config('file_path', 'yaml_path')

    def read(self, section=None, option=None):
        parh='../Data/page_data.yaml'
        with open(parh, encoding='utf-8')as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
        if section is None:
            return res
        else:
            for sections, options in res.items():
                if section not in sections:
                    return False, "未找到section"
                elif option is None:
                    return res[section]
                elif option not in options:
                    return False, "未找到option"
                elif option in options:
                    return res[section][option]

    def write(self, value):
        if isinstance(value, dict):
            for k, v in value.items():
                if self.read(k)[0]:
                    with open(self.yamlpath, 'a', encoding='utf-8')as f:
                        yaml.dump(value, f)
                        print("写入成功")
                else:
                    res = self.read()
                    res[k] = v
                    with open(self.yamlpath, 'a', encoding='utf-8')as f:
                        yaml.dump(res, f)
                    print("修改成功")


if __name__ == '__main__':
    value = {'token': ['456544654', '12312312']}
    res = DoYaml().read('file_path')
    print(res)
