#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Richard
@License: 
@Contact: fsrichard@vip.qq.com
@Software: PyCharm
@File: 01_test.py
@Time: 2019/11/3 12:22
@Desc:
"""
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


path = r"D:\Python37\chromedriver.exe"
url = "http://www.shengyazhidao.com/szpx"
browser = webdriver.Chrome(path)
browser.get(url)

'''
身份证：前6位出生地，
21：辽宁01，沈阳，02，和平区
1990 年份
01：月份，01：日期
00（0（性别码））：顺序码，0：校验码
'''


def Persons_ID():
    addr = {'shenyang': 210102, 'beijing': 110111}
    check_id = int(random.randint(1000, 10000))

address = 210102
for year in range(1981, 1990):
    for month in range(1, 13):
        for days in range(1, 31):
            # 随机取一个4位数
            check = int(random.randint(1000, 10000))
            id_numbers = address * 1000000000000 + year * 100000000 + month * 1000000 + days * 10000 + check
            id_name = browser.find_element_by_id("id")
            id_name.click()
            id_name.send_keys('%d' % id_numbers)
            data = browser.find_element_by_xpath("//*[@class = 'btn btn-danger']")
            data.click()
            # query = browser.find_element_by_id('query')
            # query.send_keys(Keys.ENTER)
            # time.sleep(1)
            browser.switch_to.alert().accept()
            # alter.accrpt()

