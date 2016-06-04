#!/usr/bin/python3

from urllib import request
from bs4 import BeautifulSoup

import re

def get_all_url(url):
    urls=[]
    web = request.urlopen(url)

    soup = BeautifulSoup(web.read())
    #通过正则表达式过滤合理的url
    tags_a = soup.findAll(name="a",attrs={'href':re.compile("^https?://")})
    try:
        for tag in tags_a:
            urls.append(tag['href'])

    except:
        pass
    return urls

#得到freebuf网站下的url
def get_local_urls(url):
    local_urls=[]
    urls = get_all_url(url)
    for _url in urls:
        ret = _url
        if 'freebuf.com' in ret.replace('//','').split('/')[0]:
            local_urls.append(_url)
    return local_urls

#得到所有不是freebuf.com 域名的网站
def get_remote_urls(url):
    remote_urls =[]
    urls = get_all_url(url)
    for _url in urls:
        ret = _url
        if "freebuf.com" not in ret.replace('//','').split('/')[0]:
            remote_urls.append(_url)
    return remote_urls

def __main__():
    url = 'http://freebuf.com'
    rurls = get_remote_urls(url)
    print("-    -   -   -   -   -   --   -   -   -   -   -  remote_urls  -   -   -   ")
    for ret in rurls:
        print(ret)
    print("-    -   -   -   -   -   --   -   -   -   -   -  local__urls  -   -   -   ")
    lurls = get_local_urls(url)
    for ret in lurls:
        print(ret)

if __name__=="__main__":
    __main__()
