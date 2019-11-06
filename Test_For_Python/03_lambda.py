#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Richard
@License: 
@Contact: fsrichard@vip.qq.com
@Software: PyCharm
@File: 03_lambda.py
@Time: 2019/11/1 12:53
@Desc:
"""

# L =lambda x: x*x
# # print(L(5))
# # print(L)
# #
# # def L(x):
# #     return x*x
# # print(L(5))

# a =[1,2,3,4]
# def func(x):
#     return x *x
# a =map(func,[1,2,3,4])
# print(a)
# print(list(a))
#
# b = map(lambda x:x*x,[1,2,3,4])
# print(list(b))

import functools


def add(a=1, b=1):
    print(a)
    print(b)
    return a + b


plus3 = functools.partial(add, 3)
# plus5 = functools.partial(add, 5)

print(plus3(2))
print(add())
# print(plus5(3))
# print(add())