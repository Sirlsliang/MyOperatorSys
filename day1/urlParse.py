#!/usr/bin/python3

from urllib import parse

url = set()
url.add('javascript:void(0)')
url.add('http://freebuf.com/geek')
url.add('https://freebuf.com:443/geek?id=1#sid')
url.add('ftp://freeme.com/ss/s/s')
url.add('sssfadea://sss.ss')
url.add('//freebuf.com/s/s/s')
url.add('/freebuf.com/s/s/s/')
url.add('//freebuf.com/s/s/s/')
url.add('path/me')
url.add('path?ss=1')
url.add('path?ss=1&s=1')
url.add('path?ss=1#arch')
url.add('?ss=1')
url.add('#atch')
for item in url:
    print(item)
    #将一个url字符串分解为6个元素，并以元组的形式返回，这与url的基本结构相关：scheme://netloc/path:parameters?query#fragment
    o = parse.urlparse(item)
    #返回的元组里面应该是每个对象，所以可以使用元组.对象名的方式来读取数据
    print("你好："+o.path)
    print()
