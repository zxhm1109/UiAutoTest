#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/3 18:32
# @File      : img_code.py
# @desc      :


import pytesseract, tesserocr
import tesserocr
import json
import requests
import base64
from PIL import ImageEnhance
from io import BytesIO
from PIL import Image
from sys import version_info


def analyseImage(path):
    img = Image.open(path)
    results = {
        'size': img.size,
        'mode': 'full',
    }
    try:
        while True:
            if img.tile:
                tile = img.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != img.size:
                    results['mode'] = 'partial'
                    break
            img.seek(img.tell() + 1)
    except EOFError:
        pass
    return results


def processImage(path):
    imgpath = []
    mode = analyseImage(path)['mode']
    im = Image.open(path)
    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')
    try:
        while True:
            if not im.getpalette():
                im.putpalette(p)
            new_frame = Image.new('RGBA', im.size)
            if mode == 'partial':
                new_frame.paste(last_frame)
            new_frame.paste(im, (0, 0), im.convert('RGBA'))
            imgp = '../Data/img/%s-%d.png' % ('testImg', i)
            new_frame.save(imgp, 'PNG')
            i += 1
            imgpath.append(imgp)
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        return imgpath


def read_text(path):
    imglist = processImage(path)
    for img in imglist:
        im = Image.open(img)
        image = im.convert('L')
        threshold = 127
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        image = image.point(table, '1')
        result = tesserocr.image_to_text(image)
        print(result)


def xxxx():
    i2 = Image.open('../Data/img/testImg-0.png')
    imgry = i2.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    i3 = sharpness.enhance(3.0)  # 3.0为图像的饱和度
    i3.save("../Data/img/image_code.png")
    i4 = Image.open("../Data/img/image_code.png")
    text = pytesseract.image_to_string(i4)  # 使用image_to_string识别验证码
    print(text)


#
#
#
# if __name__ == "__main__":
#     # a = read_text(r'C:\Users\admin\Desktop\2AF56E5B-EBCD-4C7F-AE72-1B8279E2A96A.gif')
#     # print(a)
#     xxxx()


from common.DoConfig import ReadConfig

reg = ReadConfig.read_config_options_list('img_code')

username = reg[0]
password = reg[1]


def base64_api(img):
    with open(img,'rb') as f:
        img=f.read()
    # img = img.convert('RGB')
    buffered = BytesIO()
    # img.save(buffered, format="GIF")
    if version_info.major >= 3:
        b64 = str(base64.b64encode(img), encoding='utf-8')
    else:
        b64 = str(base64.b64encode(buffered.getvalue()))
    data = {"username": username, "password": password, "image": b64,"typeid":"4"}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

def get_accountinfo():
    data={'username':username,'password':password}
    res=requests.get(url='http://api.ttshitu.com/queryAccountInfo.json',data=data)
    print(res.json())

if __name__ == "__main__":
    # a = base64_api(r'C:\Users\admin\Desktop\2AF56E5B-EBCD-4C7F-AE72-1B8279E2A96A.gif')
    # print(a)
    get_accountinfo()