#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:46
# @Author  : Xuegod Teacher For
# @File    : 01_bs_test.py
# @Software: PyCharm
#pip install bs4
from bs4 import BeautifulSoup as BS

text =  '''
<html>
<head>
    <meta = charset='UTF-8' >
    <title id =1 href = 'http://example.com/elsie' class = 'title'>Test</title>
</head>
<body>
   <div class = 'ok'>
       <div class = 'nice'>
           <p class = 'p'>
               Hello World
           </p>
            <p class = 'e'>
               风一般的男人
           </p>
       </div>
   </div>
</body> 
</html>
'''

#bs4 文本解析
soup = BS(text,'lxml')
print(soup.title)
print(soup.title.name)
print(soup.title.text)
print(soup.title.attrs)
print(soup.title.get('class'))
# print(soup.p)

# print(type(soup))
