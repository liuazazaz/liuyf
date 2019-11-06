# -*- coding:utf-8 -*-
# coding=utf-8

# @学习Python，
# @Time ：2019年10月28日
# @Author ：liuyf
# @File ：Test_01.py
# @Software ：PyCharm


# # #传统赋值
# name = 'liuyf'
# print(name)
#
# # #链式赋值
# name = user = 'liuyf02'
# print(name,user)
# #del(name)
# #del(user)
# print(id(name))
# print(id(user))
#
# # #序列解包赋值
# name,age = 'liuyf01',10
# print(name,age)
#
# age,name = name,age
# print(name,age)
# print(name + 6)
#
# # #python2的方法
# # # raw input() 会把用户输入的任何值都作为字符串来对待
#
# # #python3的方法
# # #没有raw input()，只有input()
# # name = input('请输入你的姓名：')
# print(name)
# print(id(name))
#
# #Ctrl+? 批量注释
#
# print(type(3//2))
# print(3//2)
# print(type(3/2))
# # 俩个//是除取整，一个/是除
#
# #Python内健函数讲解
# #内建数值型函数
# # abs(x) 取x的绝对值
# # round(number，ndigits=0) 对数值进行‘四舍五入’，ndigits是小数向右取整的位数，负数表示向左取整。
#
# c = pow(2,10)
# print(c)
#
# d = 4**2.5%1.5
# print(d)
#
# #字符串类型
# print("liuyf's name is 刘宇峰")
# #"双引号，区分英语中的'用的
#
# # 三单引号  三双引号
# a ='''
# 1
# 2
# 3
# '''
# print(a)
#
#
#
# #字符串的拼接
# a = "Liuyf "
# b = "is "
# c = "the very important "
# e = "preson."
#
# d = a + b + c + e
# print(d)
#
#
#
# # 特殊字符
# # "\" （在尾行时）续行符，
# # "\\" 反斜杠，
# # "\'" 单引号，
# # "\"" 双引号，
# # "\a" 响铃，
# # "\b" 退格（Backspace），
# # "\000" 空，
# # "\n" 换行，
# # "\v" 纵向制表符，
# # "\t" 横向制表符，
# # "\r" 回车，
# # "\f" 换页。
#
# # print("全世界都响ba \a \a \a \a ")
# #这个\a 并不响
#
# # %s 字符串占位符
# # %d 数字占位符
# # %f 浮点型数字占位符
# # %.2f 控制浮点型数字占位符
print('Hi %s , your score is %d.' % ("liuyf", 100))
print('%.3f.' % (1.76))
#
# a = 'hello world'
# print(len(a))
# # print(a[0:10])
# #字符串的隔取
# print(a[::1])
# # print(a[1:9:2])
# print(a[::-1])
# print(a[1:9:-1])
# print(a[9:1:-1])
# #字符串截取，包头不包尾
# #python 下标从0开始
#
#
#
# str_test = 'hello world world'
# #print(str_test.count(l)) NameError: name 'l' is not defined
# print(str_test.count('l'))
#
# print(str_test.find('w'))
# print(str_test.rfind('w'))
# print(str_test.rfind('l'))
# print(str_test.rfind('world'))
# print(str_test.index('world'))
# print(str_test.find('worlld'))


# 字符串的分割
# partition 把mystr以str分割成三部分，str前，str自身和str后。
# rpartition 类似于partition（）函数，不过是从右边开始
# splitlines 按照行分割，返回一个包含各行作为元素的列表，按照换行符分割

# str_test = 'hello world'
# print(str_test.partition('o'))
# print(str_test.rpartition('o'))
#
# str_test01 = 'hello\n world\n python\n'
# print(str_test01.splitlines())
#
# #字符串的替换 replace 从左到右替换指定元素，可以指定替换的个数，默认全部替换
# print(str_test.replace('l','a',2))


# 字符串的修饰center、ljust、rjust、zfill、fromat、strip、rstrip、lstrip

# str_test = '   liuyf   '
# print(str_test.center(19,'x'))
# print(str_test.center(19))
#
# print(str_test.ljust(19,'x'))
# print(str_test.rstrip())
#
# python = "{1} is {0}"
# print(python.format('liuyf','cool'))


# print('hello'.upper())
# print('HELLO'.lower())
# print('Hello'.swapcase())
# print('Hello_world'.title())
# print('hello_world'.capitalize())
# print('hello \t world \t'.expandtabs(20))


# print('123abc'.isalnum())
# print('abc'.isalpha())
# print('abc1'.isalpha())
# print('ABC'.isupper())
# print('abc'.islower())
# print('Abc'.istitle())
# print('  '.isspace())
#
#
# print(ord('A'))
# print(chr(65))
#
# u = '刘宇峰'
# str1 = u.encode('gbk')
# print(str1)
#
# str2 = u.encode('utf-8')
# print(str2)
#
# u1 = str1.decode('gbk')
# print(u1)
#
# u2 = str2.decode('utf-8')
# print(u2)
