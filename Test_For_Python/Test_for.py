#!/usr/bin/env python
# encoding: utf-8
'''
@Author: Richard
@License: 
@Contact: fsrichard@vip.qq.com
@Software: PyCharm
@File: Test_for.py
@Time: 2019/10/30 9:46
@Desc:
'''

# for i in range(2, 10, 2):
#     print(i, end=':')

# name = 'liuyufeng'
# print(name, end='-')
# for i in name:
#     print(i)
#     print(name, end='-')
# 9x9乘法表
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9

# 我自己写的
# for i in range(1, 10):
#     print('-')
#     for a in range(1, i + 1):
#         # print(a*i, end='-')
#         print('%d*%d=%d' % (a, i, a * i), end=';')
# 老师写的
for i in range(1, 10):
    for a in range(1, i + 1):
        # print(a*i, end='-')
        print('%d x %d = %d\t' % (a, i, a * i), end='')
    print()