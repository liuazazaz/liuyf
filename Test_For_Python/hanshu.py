#!/usr/bin/env python
# encoding: utf-8
'''
@Author: Richard
@License: 
@Contact: fsrichard@vip.qq.com
@Software: PyCharm
@File: hanshu.py
@Time: 2019/10/30 14:42
@Desc:
'''


# def func(a=0, b=0):
# #     print('我叫函数')
# #     return a + b
# #
# #
# # data = func(10, 20)
# # print(data)
def Say_Hello(*args, **kwargs):
    print(kwargs)


Say_Hello(1, 2)
