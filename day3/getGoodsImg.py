#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib import request


url= "http://shop.freebuf.com"

web =request.urlopen(url)
soup = BeautifulSoup(web.read())
print("Parsing……………………")

itemList = soup.findAll(name="div",attrs={'class':'col-sm-6 col-md-4 col-lg-4 mall-product-list'})
for item in itemList:
    #加载图片
    #if item.img:
    #    fname = item.img['alt'].replace('(','').replace(')','')
    #    if len(fname) > 10:
    #        fname = fname[:10]
    #    request.urlretrieve(url=item.img['src'],filename=fname+item.img['src'][-4:]) 
    #生成csv

    






