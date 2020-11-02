#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2020/7/4 16:13
# @File      : tool.py
# @desc      :

import time, os
from common.logger import Mylog
from common.DoConfig import Get_path
from io import BytesIO
from sys import version_info
import base64
# import cairosvg

# cairosvg.svg2png(url=svg_path, write_to=png_path)

logger = Mylog()


def load_img(img_path):
    '''
    图片处理为Base64
    :param img_path:
    :return:
    '''
    # res = request.Request(img_path)
    # data = request.urlopen(res, timeout=10).read()
    # img_path = img_path.split(',')[1]
    path = '../Data/img/test.svg'
    jpg_img_path=Get_path.get_coed_img_path()
    imgdata = base64.b64decode(img_path)
    with open(path, 'wb') as file:
        file.write(imgdata)
        file.close()
    # cairosvg.svg2png(url=path, write_to=jpg_img_path)
    os.remove(path)
    # buffered = BytesIO()
    # if version_info.major >= 3:
    #     b64 = str(base64.b64encode(imgdata), encoding='utf-8')
    # else:
    #     b64 = str(base64.b64encode(buffered.getvalue()))
    # return b64
    #
    # else:
    # logger.error('不支持该图片地址:{}'.format(img_path))


def del_data_img(folderpath):
    path = os.path.dirname(folderpath)
    num = 0
    for x, y, z in os.walk(path):
        for i in z:
            a = int(nowtimestr()[:-6])
            b = int(i[:10])
            ya = int(str(a)[:5])
            yb = int(str(b)[:5])
            ma = int(str(a)[4:-2])
            mb = int(str(b)[4:-4])
            da = int(str(a)[-2:])
            db = int(str(b)[-4:-2])
            if (ma - mb) >= 2 and ya >= yb:
                os.remove(os.path.join(path, i))
                num += 1
            elif (ma - mb) == 1 and ya >= yb and da > db:
                os.remove(os.path.join(path, i))
                num += 1
            else:
                pass
    logger.info('清理一个月前的历史图片数量:{}'.format(num))


def nowtimestr():
    strtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return strtime


def upload(filePath, browser_type="chrome"):
    '''
    通过pywin32模块实现文件上传的操作
    :param filePath: 文件的绝
    对路径
    :param browser_type: 浏览器类型（默认值为chrome）
    :return:
    '''
    import win32con
    import win32gui
    logger.info("上传文件地址：{}".format(filePath))
    if browser_type.lower() == "chrome":
        title = "打开"
    elif browser_type.lower() == "firefox":
        title = "文件上传"
    elif browser_type.lower() == "ie":
        title = "选择要加载的文件"
    else:
        title = ""  # 根据其它不同浏览器类型来修改

    # 找元素
    # 一级窗口"#32770","打开"
    dialog = win32gui.FindWindow("#32770", title)
    # 向下传递
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

    # 输入文件的绝对路径，点击“打开”按钮
    time.sleep(0.5)
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
    time.sleep(0.5)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
    logger.info('-----文件上传完成：{}'.format(filePath))


if __name__ == '__main__':
    # load_img(
    #     'http://192.168.200.104:9900/api-uaa/validata/code/1242764A-783B-4374-B24E-077B6ECB2737?t=1593853142000')
    a = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MCIgaGVpZ2h0PSIzMCIgdmlld0JveD0iMCwwLDgwLDMwIj48cGF0aCBkPSJNOCAxMCBDMjYgMTgsNTYgMjMsNjkgMjYiIHN0cm9rZT0iIzIyMiIgZmlsbD0ibm9uZSIvPjxwYXRoIGQ9Ik0xOSAxMCBDMzQgMjEsNDAgMjEsNjcgOSIgc3Ryb2tlPSIjNTU1IiBmaWxsPSJub25lIi8+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTMwLjI3IDI0LjY5TDMwLjQ0IDI0Ljg2TDMwLjQzIDI0Ljg1UTI5LjIwIDI0Ljc3IDI4LjEzIDI1LjE0TDI4LjA1IDI1LjA3TDI4LjAzIDI1LjA0UTI4LjM3IDIyLjcyIDI4LjQ1IDIwLjcxTDI4LjQyIDIwLjY4TDI4LjU4IDIwLjg1UTI4LjYyIDE4Ljg2IDI4LjQ4IDE2LjUxTDI4LjUwIDE2LjUzTDI4LjM4IDE2LjQxUTI3LjUzIDE2LjIzIDI3LjA0IDE1Ljk4TDI3LjAwIDE1Ljk0TDI2LjgyIDE0LjA3TDI2Ljc5IDE0LjA1UTI3LjE4IDE0LjM2IDI4LjIxIDE0LjcyTDI4LjI2IDE0Ljc4TDI4LjI4IDE0LjgwUTI4LjI0IDEzLjUzIDI3Ljk3IDExLjc3TDI3Ljg3IDExLjY3TDI3Ljg3IDExLjY3UTI5LjI2IDEyLjAzIDMwLjMyIDExLjk0TDMwLjQ3IDEyLjA5TDMwLjI3IDE0LjkyTDMwLjQxIDE1LjA3UTMxLjE0IDE0Ljg0IDMxLjk5IDE0LjUyTDMyLjA4IDE0LjYwTDMyLjAxIDE0LjUzUTMyLjE0IDE1LjI4IDMxLjk5IDE2LjQwTDMxLjgyIDE2LjIzTDMxLjg0IDE2LjI2UTMwLjkyIDE2LjUzIDMwLjI2IDE2LjUzTDMwLjE4IDE2LjQ1TDMwLjM3IDE2LjY0UTMwLjI1IDE3LjkyIDMwLjI1IDIwLjY2TDMwLjIzIDIwLjY0TDMwLjMxIDIwLjcyUTMwLjM5IDIzLjQ3IDMwLjQ0IDI0Ljg2Wk0zMi4yNSAxNC4xNEwzMi40NSAxNC4zNEwzMi4zMCAxNC4xOVEzMi4xNiAxNC4zMCAzMS43NyAxNC40NUwzMS44MSAxNC40OUwzMi4wMyAxMi42N0wzMi4wNCAxMi42OVEzMS40MyAxMi43OCAzMC41MiAxMi45M0wzMC42MSAxMy4wMkwzMC41OSAxMy4wMFEzMC41OCAxMi41NCAzMC42OCAxMS42NkwzMC42MSAxMS42MEwzMC42NCAxMS42MlEzMC4yNiAxMS42OCAyOS44OSAxMS42OEwyOS45MiAxMS43MUwzMC4wMiAxMS44MVEyOC41MiAxMS42OSAyNy40NyAxMS4yMkwyNy41NSAxMS4zMEwyNy40NCAxMS4xOVEyNy43NiAxMi43OCAyNy45MyAxNC4zN0wyOC4wNSAxNC41MEwyOC4wMCAxNC40NFEyNy40NSAxNC4yMyAyNi40NyAxMy41N0wyNi40MyAxMy41NEwyNi4zOSAxMy40OVEyNi44MCAxNC41MSAyNi45NCAxNi4yNUwyNi44MyAxNi4xNEwyNi44MSAxNi4xMVEyNy4xMSAxNi4yNyAyNy44NyAxNi41NEwyNy44MyAxNi41MEwyNy45NSAxNi42MlEyNy45NyAxNy4wMyAyNy45OSAxNy45NEwyNy45MiAxNy44NkwyOC4xNiAxNy44OEwyOC4zNCAxOC4wMkwyOC4yMyAxNy45MFEyOC4zNiAxOC43OSAyOC4zNiAxOS41NUwyOC4zNiAxOS41NUwyOC4yNSAxOS40NFEyOC4yNCAyMi42MSAyNy43MiAyNS40MEwyNy43NiAyNS40M0wyNy44MCAyNS40OFEyNy45MSAyNS4zOSAyOS4xNiAyNS4wNUwyOS4xMyAyNS4wMkwyOS4xOSAyNS4wOFEyOS4xNCAyNS40NSAyOS4wNyAyNi4zM0wyOS4wMCAyNi4yNkwyOS4wNyAyNi4zM1EyOS42NiAyNi4zNiAzMC4xOCAyNi4zNkwzMC4yMSAyNi4zOUwzMC4xNSAyNi4zM1EzMS4xNSAyNi4yMyAzMi4yMCAyNi41OUwzMi4yNiAyNi42NUwzMi4zNCAyNi43NFEzMS4zNiAyMi45NCAzMS40OCAxNy44NUwzMS41NSAxNy45MkwzMy4wNSAxNy42M0wzMy4xMiAxNy43MVEzMy4xNCAxNy4wOSAzMy4xOSAxNi40M0wzMy4xNyAxNi40MUwzMy4zNyAxNS4xOUwzMy4yNCAxNS4wNVEzMi44OSAxNS4yNSAzMi4xNCAxNS41NEwzMi4xOCAxNS41OUwzMi4xMiAxNS41M1EzMi40NSAxNC44MCAzMi40MCAxNC41OEwzMi4yMyAxNC40MUwzMi40MCAxNC41OFEzMi4zNyAxNC40MyAzMi40MSAxNC4zMVoiLz48cGF0aCBmaWxsPSIjMTExIiBkPSJNNDguNzQgMjUuMzVMNDguNjEgMjUuMjNMNDguNzAgMjUuMzJRNDcuNjggMjQuMDYgNDYuODUgMjIuMDhMNDYuOTggMjIuMjFMNDUuNjIgMTguOTFMNDUuNTcgMTguODZRNDQuNjMgMjEuNTIgNDQuMjQgMjIuMzVMNDQuMTUgMjIuMjdMNDQuMTAgMjIuMjFRNDMuMTUgMjQuMDggNDIuMTIgMjUuMzBMNDIuMzIgMjUuNTBMNDIuMTUgMjUuMzNRNDEuOTYgMjUuMzggNDEuNDcgMjUuNDZMNDEuNDEgMjUuMzlMNDEuNDIgMjUuNDFRNDEuNDUgMjAuNjcgMzcuNzEgMTYuODVMMzcuNzMgMTYuODdMMzcuODEgMTYuOTVRMzYuNjEgMTUuNzAgMzUuMzEgMTQuNzRMMzUuNDAgMTQuODNMMzUuMjkgMTQuNzJRMzYuNTEgMTUuMTIgMzcuNzEgMTUuMzFMMzcuNjIgMTUuMjJMMzcuNzIgMTUuMzJRNDEuNjMgMTguNTIgNDIuNTYgMjIuNTNMNDIuNjEgMjIuNThMNDIuNTYgMjIuNTNRNDMuMjIgMjEuNDMgNDMuOTggMTkuMzdMNDMuODcgMTkuMjdMNDMuOTQgMTkuMzNRNDQuODMgMTYuOTUgNDUuMjAgMTYuMTJMNDUuMTIgMTYuMDNMNDUuOTcgMTUuOThMNDYuMDUgMTYuMDZRNDYuNTEgMTcuMDYgNDcuMjcgMTkuMTZMNDcuNDMgMTkuMzNMNDcuMzQgMTkuMjNRNDguMDggMjEuNDcgNDguNDkgMjIuMzdMNDguNjEgMjIuNDlMNDguNjYgMjIuNTNRNDkuNzIgMTguMzggNTMuMjQgMTUuNDVMNTMuMzcgMTUuNTdMNTMuMzQgMTUuNTVRNTQuMDcgMTUuNDUgNTUuODQgMTUuMDhMNTUuODggMTUuMTJMNTUuODMgMTUuMDdRNTAuMjkgMTguOTUgNDkuNTMgMjUuMzdMNDkuNTkgMjUuNDJMNDkuMTEgMjUuMjlMNDkuMTcgMjUuMzRRNDguODUgMjUuMjIgNDguNjMgMjUuMjVaTTUwLjYwIDI2Ljg3TDUxLjkwIDI2Ljk3TDUxLjg1IDI2LjkzUTUxLjYyIDI1LjkyIDUxLjYyIDI0Ljk0TDUxLjYxIDI0LjkzTDUxLjcwIDI1LjAyUTUxLjYwIDIyLjg0IDUyLjUxIDIwLjc2TDUyLjYzIDIwLjg4TDUyLjQ4IDIwLjczUTUzLjgyIDE3Ljg5IDU2LjQ3IDE1LjkxTDU2LjU0IDE1Ljk4TDU2LjQxIDE1Ljg1UTU1LjYzIDE2LjAyIDU0LjQzIDE2LjI0TDU0LjYwIDE2LjQyTDU0LjQxIDE2LjIyUTU1Ljc4IDE1LjI3IDU2LjYxIDE0LjY4TDU2LjcxIDE0Ljc3TDU0Ljk0IDE0LjkyTDU1LjA0IDE1LjAyUTU0LjIxIDE1LjEyIDUzLjM2IDE1LjIyTDUzLjMyIDE1LjE4TDUzLjI3IDE1LjEzUTUwLjAxIDE3LjkxIDQ4Ljc2IDIxLjE0TDQ4Ljc5IDIxLjE3TDQ4LjcwIDIxLjA5UTQ4LjMzIDE5Ljc0IDQ3LjQ1IDE3LjAwTDQ3LjM5IDE2Ljk0TDQ3LjU1IDE3LjEwUTQ3LjI3IDE3LjA0IDQ3LjEwIDE3LjA0TDQ3LjA5IDE3LjAyTDQ2LjY5IDE2Ljk3TDQ2Ljc0IDE3LjAyUTQ2LjY2IDE2LjgxIDQ2LjE0IDE1LjY5TDQ2LjIwIDE1Ljc1TDQ0Ljg3IDE1Ljc0TDQ0LjgxIDE1LjY4UTQ0LjIzIDE3LjUyIDQyLjg4IDIxLjE0TDQyLjg3IDIxLjEzTDQyLjkxIDIxLjE2UTQyLjA2IDE4LjgwIDQwLjA4IDE2LjcwTDQwLjE2IDE2Ljc4TDQwLjAzIDE2LjY0UTM5LjkyIDE2LjcxIDM5LjcyIDE2LjY5TDM5LjcyIDE2LjY5TDM5LjI3IDE2LjUzTDM5LjI4IDE2LjU0UTM4LjgyIDE2LjEwIDM3LjY3IDE1LjA3TDM3LjcyIDE1LjEzTDM3LjY2IDE1LjA2UTM1LjYxIDE0LjYzIDM0LjU0IDE0LjMxTDM0LjQ4IDE0LjI2TDM0LjU4IDE0LjM2UTQxLjQ1IDE5LjEyIDQxLjIxIDI1Ljc2TDQxLjIyIDI1Ljc2TDQxLjIxIDI1Ljc2UTQxLjIzIDI1LjY2IDQxLjQ3IDI1LjYzTDQxLjQ1IDI1LjYyTDQxLjU0IDI1LjcxUTQxLjcwIDI1LjYxIDQxLjgyIDI1LjYxTDQxLjgzIDI1LjYyTDQxLjgzIDI1LjYyUTQxLjgyIDI1LjUxIDQxLjk0IDI2Ljg2TDQyLjEzIDI3LjA0TDQzLjI1IDI2LjgyTDQzLjE4IDI2Ljc1UTQ0Ljk4IDI1LjA4IDQ2LjQzIDIxLjM4TDQ2LjM5IDIxLjM1TDQ2LjM1IDIxLjMxUTQ3LjQzIDIzLjkxIDQ4LjYzIDI1LjYyTDQ4LjYxIDI1LjYwTDQ4LjU2IDI1LjU1UTQ4Ljc3IDI1LjU0IDQ4Ljk1IDI1LjU1TDQ4Ljg2IDI1LjQ2TDQ4Ljg1IDI1LjQ1UTQ5LjAyIDI1LjQ3IDQ5LjIwIDI1LjQ3TDQ5LjI5IDI1LjU2TDUwLjQ3IDI2Ljc1WiIvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0xMy4xNSAxNy4yN0wxMy4xMCAxNy4yM0wxMy4zMCAxNy40MlExMS4zMCAxNy4yNCAxMC44MiAxOC42OEwxMC45MSAxOC43OEwxMC45NyAxOC44NFExMC43MCAxOS4xOCAxMC42MyAxOS42MEwxMC42OSAxOS42NUwxMC43NCAxOS43MFExMi4yNyAxOS42OSAxMy4zMiAxOS42OUwxMy40NyAxOS44NEwxMy40OCAxOS44NVExNC41NiAxOS44OCAxNi4yMyAxOS44MUwxNi4yMSAxOS43OUwxNi4xMSAxOS42OVExNi4wNCAxOC41OSAxNS4xMyAxNy45MUwxNS4xNSAxNy45MkwxNS4yNiAxOC4wM1ExNC40MCAxNy4zNyAxMy4yNSAxNy4zN1pNMTMuMjcgMjUuNDJMMTMuMzUgMjUuNTBMMTMuMzQgMjUuNDlRMTAuNTEgMjUuMzggOS42OCAyNC40OEw5LjY2IDI0LjQ2TDkuNzQgMjQuNTNROS4wNyAyMy41NCA4Ljk3IDIxLjQ0TDkuMDEgMjEuNDhMOS4wMCAyMS40N1E4LjkyIDIxLjI0IDguODcgMjAuMzZMOS4wMSAyMC41MEw4Ljk0IDIwLjQzUTguODggMTguOTggOC44OCAxOC41MUw4Ljc5IDE4LjQyTDguNzkgMTguNDJROC45MCAxNy4zNCA5LjM3IDE2LjYzTDkuMjUgMTYuNTBMOS4zNSAxNi42MFExMC4xNSAxNS41OSAxMi4wNiAxNS41OUwxMi4xOSAxNS43M0wxMy4xOCAxNS43MUwxMy4xMCAxNS42M1ExNC40NCAxNS42NSAxNS40MiAxNS44NUwxNS4zNSAxNS43OEwxNS41MiAxNS45NVExNi43NiAxNi4xNiAxNy4zOSAxNi45NEwxNy40MiAxNi45NkwxNy40NCAxNi45OVExNy43OSAxNy42MyAxNy44NCAxOC45OEwxNy43OCAxOC45MkwxNy45NCAxOS4wN1ExNy44NiAxOS43MyAxNy44OCAyMS4xM0wxNy45MCAyMS4xNEwxNy43NiAyMS4wMFExNS45NCAyMS4wNCAxNC4xNiAyMS4wNEwxNC4yOCAyMS4xNkwxMC42MSAyMS4wOUwxMC42MCAyMS4wOVExMC42NSAyMy44OCAxMy4yNyAyMy43M0wxMy4yNiAyMy43M0wxMy40MyAyMy44OVExNS43NyAyMy42OSAxNi41NSAyMi41MUwxNi41NiAyMi41MUwxNi42MCAyMi41NVExNy4wNyAyMi44MCAxOC4wOSAyMy41NkwxOC4xNCAyMy42MUwxOC4wNyAyMy41NFExNy4yNyAyNS4xNiAxNC42MCAyNS4zM0wxNC42NyAyNS40MEwxNC41MyAyNS4yNlExNC4xMyAyNS4zNiAxMy4yNSAyNS40MFpNMTQuNjkgMjYuODZMMTQuNjUgMjYuODJMMTQuNjUgMjYuODJRMTUuMzUgMjYuNzkgMTYuMTQgMjYuODRMMTYuMTQgMjYuODVMMTYuMjMgMjYuOTNRMTkuMzcgMjYuOTkgMTkuOTYgMjUuMjFMMjAuMDQgMjUuMjlMMjAuMTAgMjUuMzVRMTkuMDMgMjQuNTIgMTguMzIgMjQuMDNMMTguMTggMjMuOTBMMTguMzIgMjQuMDRRMTguMzcgMjMuNzIgMTguNTAgMjMuNTdMMTguMzkgMjMuNDdMMTguMzkgMjMuNDdRMTcuOTkgMjMuMjQgMTcuMTEgMjIuNjJMMTcuMjEgMjIuNzNMMTcuMDUgMjIuNTdRMTcuODkgMjIuNzQgMTkuMjEgMjIuOTRMMTkuMTkgMjIuOTNMMTkuMjEgMjIuOTRRMTkuMDAgMjEuOTcgMTguOTUgMjEuNTNMMTkuMTAgMjEuNjhMMTguOTAgMjAuMzNMMTguOTUgMjAuMzhRMTguNzggMTguNzkgMTguMzcgMTcuODRMMTguMzYgMTcuODNMMTguNDUgMTcuOTNRMTguMjAgMTcuNjIgMTcuODMgMTcuMjNMMTcuODkgMTcuMjlMMTcuOTUgMTcuMzVRMTcuNzIgMTcuMDIgMTcuNTcgMTYuNjVMMTcuNjYgMTYuNzRMMTcuNjUgMTYuNzNRMTYuNDcgMTUuNDUgMTMuMjEgMTUuNDVMMTMuMDMgMTUuMjdMMTIuMDEgMTUuMzNMMTEuOTggMTUuMzBRMTAuMDMgMTUuNDIgOS4xMCAxNi4zOEw5LjEyIDE2LjQwTDkuMTQgMTYuNDJROC41MSAxNi45NCA4LjUzIDE4LjI2TDguNjcgMTguNDBMOC41NiAxOC4yOVE4LjU4IDE4Ljg5IDguNjUgMjAuMzRMOC43NyAyMC40Nkw4LjY2IDIwLjM1UTguNzQgMjEuNDAgOC44MSAyMi43Mkw4Ljc5IDIyLjcwTDguODYgMjIuNzdROS4wOSAyNC4yOCA5LjY1IDI0Ljk2TDkuNTYgMjQuODdMOS42NyAyNC45OFE5LjcyIDI1LjAzIDkuODQgMjUuMTBMOS43NiAyNS4wMkwxMC4xMSAyNS41OEwxMC4xMSAyNS41OVExMC41MCAyNi42NiAxNC43MyAyNi45MFpNMTMuMzAgMjMuNDlMMTMuNDMgMjMuNjJMMTMuNDMgMjMuNjNRMTIuNTQgMjMuNTQgMTEuOTYgMjMuMjVMMTEuOTggMjMuMjdMMTEuOTggMjMuMjdRMTIuMTAgMjMuMTcgMTEuOTggMjIuNzNMMTEuOTEgMjIuNjZMMTEuNzkgMjIuNTVRMTMuMDQgMjIuNjUgMTQuMDcgMjIuNjVMMTMuODkgMjIuNDdMMTQuMDQgMjIuNjJRMTQuOTggMjIuNDkgMTYuMDYgMjIuNTZMMTYuMTYgMjIuNjZMMTYuMDggMjIuNThRMTUuMjQgMjMuNDMgMTMuMzEgMjMuNTBaTTE0LjQ0IDE4Ljg2TDE0LjQyIDE4Ljg0TDE0LjQxIDE4LjgzUTE0LjkzIDE4Ljk2IDE1Ljc5IDE5LjIwTDE1LjY1IDE5LjA2TDE1Ljg4IDE5LjQxTDE1LjgwIDE5LjQ1TDE1LjgyIDE5LjQ3UTE0LjkzIDE5LjU1IDE0LjM1IDE5LjUyTDE0LjI3IDE5LjQ1TDE0LjQ1IDE5LjYyUTEyLjgwIDE5LjQyIDEyLjc4IDE5LjQyTDEyLjc3IDE5LjQxTDEyLjg2IDE5LjUxUTEzLjQ0IDE5LjAwIDE0LjUxIDE4LjkzWiIvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik02MC4wMyAxOC4wNkw2MC4xMiAxOC4xNUw2MC4wOCAxOC4xMVE1OS45MiAxOC4xMCA1OS43MiAxOC4xMEw1OS43OSAxOC4xNkw1OS42OCAxOC4wNVE1OC44MiAxOC4wNiA1Ny44OSAxOC41OUw1OC4wMSAxOC43MUw1Ny45MSAxOC42MVE1Ny4xNSAxOS40MiA1Ny4xNSAyMC42NEw1Ny4wOSAyMC41OEw1Ny4xNCAyMC42M1E1Ny4wNCAyMi43MyA1OC4wMiAyMy41OUw1OC4wOCAyMy42NUw1OC4wNiAyMy42NFE1OC42NyAyNC4zOSA2MC4xNCAyNC4zOUw2MC4yMyAyNC40OEw2MC4xNyAyNC40MlE2MC4zNSAyNC40NiA2MC41NSAyNC40Nkw2MC40OCAyNC4zOUw2MC41MSAyNC40MlE2MS43MSAyNC41MSA2Mi40NCAyMy40Nkw2Mi4yNSAyMy4yN0w2Mi40NCAyMy40NlE2Mi45OSAyMi4zNyA2Mi45NCAyMS4yMUw2Mi44NyAyMS4xNUw2Mi45MiAyMS4yMFE2My4wOSAyMS4wMiA2My4wOSAyMC43NUw2Mi45MiAyMC41OUw2Mi45NyAyMC42M1E2My4wMiAxOS41NCA2Mi4xNCAxOC43OUw2Mi4yMSAxOC44Nkw2Mi4wOSAxOC43NFE2MS4yMCAxNy45OCA2MC4wNSAxOC4wOFpNNjIuOTYgMjQuNjRMNjIuOTMgMjQuNjFMNjIuOTUgMjQuNjNRNjIuMzUgMjUuOTEgNTkuOTUgMjUuOThMNjAuMDUgMjYuMDlMNjAuMDQgMjYuMDhRNTcuNjcgMjUuOTYgNTYuNjQgMjQuOTNMNTYuNjUgMjQuOTRMNTYuNjUgMjQuOTNRNTUuNzMgMjMuODIgNTUuMjIgMjAuNzRMNTUuMzAgMjAuODJMNTUuMzQgMjAuODZRNTUuMDkgMTkuNjggNTUuMDkgMTguODdMNTUuMTAgMTguODlMNTUuMTEgMTguODlRNTUuMDYgMTcuNzAgNTUuNTMgMTcuMDFMNTUuNDcgMTYuOTVMNTUuNjMgMTcuMTFRNTYuMzkgMTYuMTEgNTguMzAgMTYuMTFMNTguMzcgMTYuMThMNTguMjggMTYuMDlRNjIuMzcgMTYuMTIgNjMuNTkgMTcuNzhMNjMuNjcgMTcuODZMNjMuNzAgMTcuODlRNjMuNzggMTcuMzQgNjQuMDUgMTYuMzFMNjQuMDcgMTYuMzJMNjQuMDEgMTYuMjZRNjQuODAgMTYuMDUgNjYuMzYgMTUuNTRMNjYuNDYgMTUuNjNMNjYuMzQgMTUuNTFRNjQuODIgMTkuMTggNjQuNjcgMjMuMjVMNjQuNTkgMjMuMTdMNjQuNzEgMjMuMjhRNjQuNTAgMjcuMTggNjUuODcgMzAuOTNMNjUuODQgMzAuODlMNjUuODkgMzAuOTVRNjQuNzQgMzAuNTEgNjMuNTkgMzAuMzRMNjMuNjcgMzAuNDFMNjMuNjYgMzAuNDFRNjMuMTUgMjcuOTQgNjMuMDggMjQuNzZaTTYzLjQ2IDMwLjU3TDYzLjQ5IDMwLjYwTDYzLjM4IDMwLjQ5UTY0LjA0IDMwLjc5IDY0Ljk1IDMwLjk4TDY0Ljg3IDMwLjkwTDY0LjkwIDMwLjk0UTY1LjA3IDMxLjQyIDY1LjQ0IDMyLjMzTDY1LjQzIDMyLjMyTDY1LjQ2IDMyLjM1UTY3LjEyIDMyLjgxIDY4LjU4IDMzLjY0TDY4LjUzIDMzLjU5TDY4LjQwIDMzLjQ2UTY1LjkxIDI5LjMzIDY1LjkxIDIzLjg1TDY1Ljk0IDIzLjg3TDY1Ljk1IDIzLjg5UTY1LjkwIDE5Ljc0IDY3LjQ5IDE2LjAyTDY3LjU1IDE2LjA5TDY3LjQzIDE1Ljk3UTY2Ljk2IDE2LjE0IDY2LjA4IDE2LjU1TDY2LjI2IDE2Ljc0TDY2LjEyIDE2LjU5UTY2LjM2IDE2LjEyIDY2Ljc4IDE1LjEyTDY2Ljc1IDE1LjA5TDY2LjcxIDE1LjA1UTY1LjgxIDE1LjUwIDYzLjc1IDE2LjA2TDYzLjgzIDE2LjE0TDYzLjY3IDE1Ljk4UTYzLjU4IDE2LjMzIDYzLjM5IDE3LjA5TDYzLjQxIDE3LjExTDYzLjQyIDE3LjEyUTYyLjE1IDE1LjkzIDU4LjIxIDE1LjgzTDU4LjE4IDE1LjgwTDU4LjMyIDE1Ljk0UTU2LjE5IDE1LjgyIDU1LjMxIDE2Ljc3TDU1LjI5IDE2Ljc1TDU1LjI0IDE2LjcwUTU0Ljg2IDE3LjU0IDU0Ljg5IDE4Ljc3TDU0LjkzIDE4LjgxTDU0LjgyIDE4LjcwUTU0Ljk5IDIwLjczIDU1LjYzIDIzLjE1TDU1LjU1IDIzLjA4TDU1LjU5IDIzLjEyUTU2LjAxIDI0LjY2IDU2LjU5IDI1LjI3TDU2LjUyIDI1LjIwTDU2Ljg2IDI1LjU0TDU2LjgzIDI1LjUxUTU3LjYxIDI3LjMyIDYxLjExIDI3LjQ2TDYxLjEzIDI3LjQ4TDYxLjAxIDI3LjM2UTYxLjgxIDI3LjUyIDYyLjk4IDI3LjMzTDYyLjk5IDI3LjM0TDYyLjk2IDI3LjMxUTYzLjA1IDI5LjA4IDYzLjQ0IDMwLjU1Wk02MS4zNCAxOS42NEw2MS4zOSAxOS42OUw2MS4zMiAxOS42MlE2Mi4wMSAxOS42MyA2Mi41NSAxOS44Mkw2Mi42NCAxOS45MUw2Mi40NyAxOS43NFE2Mi42NSAyMC4xNSA2Mi43MiAyMC41NEw2Mi43MCAyMC41MUw2Mi44MCAyMC42MlE2Mi43NyAyMC44NyA2Mi43MiAyMS4yNkw2Mi42OSAyMS4yNEw2Mi43NiAyMS4zMVE2Mi44MiAyMi41OSA2Mi4xNiAyMy40Mkw2Mi4wMCAyMy4yNkw2Mi4xNCAyMy40MVE2MS40MyAyNC4zNiA2MC4yMyAyNC4yM0w2MC4xNyAyNC4xN0w2MC4yMSAyNC4yMVE1OS4yOSAyNC4xMyA1OC42OCAyMy44Nkw1OC43MyAyMy45MUw1OC43MCAyMy44OFE1OC40NSAyMy4zNCA1OC40NSAyMi41NUw1OC40MyAyMi41M0w1OC41MyAyMi42M1E1OC41MiAyMi40MiA1OC41MiAyMi4yM0w1OC4zNyAyMi4wOEw1OC41MiAyMi4yM1E1OC40MSAyMC45OSA1OS4yNiAyMC4yNEw1OS4yNSAyMC4yM0w1OS4zNyAyMC4zNVE2MC4xNiAxOS41NCA2MS4yOSAxOS41OVoiLz48L3N2Zz4='
    load_img(a)
