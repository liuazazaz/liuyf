# -*- coding:utf-8 -*-
# coding=utf-8

# @学习Python，
# @Time ：2019年10月29日 18:40:09
# @Author ：liuyf
# @File ：Test_03.py
# @Software ：PyCharm

# 非，且，或（先后顺序）

year = int(input('请输入一个年份：'))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0 :
    print('{0}是闰年'.format(year))
else :
    print('{0}不是闰年'.format(year))

