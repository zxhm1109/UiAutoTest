#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/3 18:16
# @File      : login_page.py
# @desc      :

from common.Brower import brower
from urllib import request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common.rw_yaml import DoYaml
from PIL import Image
import datetime
import pyautogui,os
import shutil
from common.img_code import base64_api
from common.tool import *

driver = brower.chrome(DoYaml().read('login', 'url'))
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@name="username"]').send_keys(DoYaml().read('login', 'username'))
driver.find_element_by_xpath("//*[@name='password']").send_keys(DoYaml().read('login', 'password'))
img_code =driver.find_element_by_xpath("//img[@class='el-image__inner']")
img_path=img_code.get_attribute('src')
res=base64_api(load_img(img_path))
print(res)
time.sleep(5)
driver.find_element_by_xpath("//input[@class='el-input__inner' and @name='validCode']").send_keys(res)
driver.find_element_by_xpath("//*[@class='el-button el-button--primary']").click()
