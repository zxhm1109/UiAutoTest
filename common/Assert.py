#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/15 11:45
# @File      : Assert.py
# @desc      :

class Assert:

    @staticmethod
    def equal(result, expect):
        if result is None:
            return 'result为None，无法比较！'
        elif '$' in expect:
            pass
