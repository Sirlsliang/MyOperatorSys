#!/usr/bin/python3

#fileName:bs4Simple文件

from bs4 import BeautifulSoup

import urllib.request

import re

web = urllib.request.urlopen("http://www.freebuf.com")
#构建了一个类
soup = BeautifulSoup(web.read(),"html5lib")
#调用findAll函数，该函数有两个参数，name属性指定了表签名，
#attrs属性传入了一个字典，字典的key是属性，value是一个正则表达式，标明了属性的限制,最后的返回值是一个字典，我们可以通过
tags_a = soup.findAll(name="a",attrs={'href':re.compile("^https?://")})

for tag_a in tags_a:
    print(tag_a)
    print(tag_a["href"])

