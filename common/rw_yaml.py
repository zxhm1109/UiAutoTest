#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/3 16:19
# @File      : rw_yaml.py
# @desc      :

import yaml, os
from common.DoConfig import *
from common.logger import Mylog

logger = Mylog()


class DoYaml:

    def __init__(self):
        self.yamlpath = Get_path.get_yaml_path()

    def read(self, section=None, option=None):
        parh = self.yamlpath
        with open(parh, encoding='utf-8')as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
        if section is None:
            return res
        else:
            if len(res) < 2:
                for sections, options in res.items():
                    if section not in sections:
                        return False, "未找到section"
                    elif option is None:
                        return res[section]
                    elif option not in options:
                        return False, "未找到option"
                    elif option in options:
                        return res[section][option]
            else:
                return res[section]

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


def get_case_data(casesuite):
    casedata = []
    url = None
    res = DoYaml().read(casesuite)
    for k, v in res.items():
        if isinstance(v, dict):
            casedata.append(v)
        else:
            url = v
    logger.info('测试用例数据：{} - url:{}'.format(casedata, url))
    return casedata, url


if __name__ == '__main__':
    import json
    a = DoYaml().read('token')
    print(json.dumps(a))
