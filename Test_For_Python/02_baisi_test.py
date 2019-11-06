#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:59
# @Author  : Xuegod Teacher For
# @File    : 02_baisi_test.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests # pip install requests
import re,time

url = 'http://www.budejie.com/video/'
#浏览器的头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
#获取整页的html
def get_page(url):
    html = requests.get(url,headers=headers)
    return html.text
#获取所有的MP4
def parse_page(html):
    soup = BeautifulSoup(html,'lxml')
    mp4_lists = soup.find_all('a',href=re.compile("http://svideo.spriteapp.com/video/2019/(.*?).mp4"))
    for i in mp4_lists:
        url_href = i.get('href')
        req = requests.get(url_href)
        print('开始下载')
        with open(str(time.time())+'.mp4','wb') as file:
            file.write(req.content)
        print('下载完成')
#todo 控制下载的页码
def get_more_page(start,end):
    pass

if __name__ == '__main__':
    html = get_page(url)
    parse_page(html)

