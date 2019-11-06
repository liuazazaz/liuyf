#!/usr/bin/env python
# encoding: utf-8
'''
@Author: Richard
@License: 
@Contact: fsrichard@vip.qq.com
@Software: PyCharm
@File: Test_if_01.py
@Time: 2019/10/30 9:08
@Desc:了解if语句如何执行
'''

age1 = int(input('请输入的你年龄：'))

if age1 < 5:
    print('你是个小朋友')
elif age1 <= 16:
    print('你还未成年')
elif age1 < 50:
    if age1 > 16:
        print('有身份证了')
elif age1 < 60:
    print('你已经快要退休了，加油')
elif age1 < 100:
    if age1 >= 60:
        print('你应该退休了')
else:
    print('你是一个老妖精么？')
