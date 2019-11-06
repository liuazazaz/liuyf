#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Richard
@License:
@Contact: fsrichard@vip.qq.com
@Software: PyCharm
@File: Test_liebaotuidao.py
@Time: 2019/10/30 13:23
@Desc:
"""

# result = []
# for i in range(1, 11):
#     result.append(i)
# print(result)

# 列表推导式
# result = [i for i in range(11) if i % 2 == 0]
# print(result)

# 取出1/4/7和1/5/9元素
L = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(L[0][2])

# result = [i[0] for i in L]
# print(result)
result = [L[i][i] for i in range(len(L))]
print(result)
