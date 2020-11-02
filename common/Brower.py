#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/3 14:14
# @File      : Brower.py
# @desc      :


from selenium import webdriver
import time

class brower:
    @staticmethod
    def chrome(url):
        driver = webdriver.Chrome('..\Data\chromedriver.exe')
        driver.get(url)
        # driver.maximize_window()
        driver.implicitly_wait(10)
        driver.refresh()
        time.sleep(2)
        return driver

    @staticmethod
    def firefox(url):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.refresh()
        time.sleep(2)
        return driver

    @staticmethod
    def ie(url):
        driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.refresh()
        time.sleep(2)
        return driver

    @staticmethod
    def safari(url):
        driver = webdriver.Safari()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.refresh()
        time.sleep(2)
        return driver
