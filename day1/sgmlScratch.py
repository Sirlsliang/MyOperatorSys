# coding:utf-8
#!/usr/bin/python
#Filename:simpleScratch.py

import urllib
import sgmllib

class handle_html(sgmllib.SGMLParser):
    #unknown_starttag 这个方法在任意的标签开始被解析时调用
    #tag 表签名
    #attrs 表示标签的参数
    def unknown_starttag(self,tag,attrs):
        print("------"+ tag+" start --------------")
        print(attrs)

    #unknown_endtag 这个方法在任意标签结束被解析时调用
    def unknown_endtag(self,tag):
        print("----------"+ tag +" end -----------")


web = urllib.urlopen("http://freebuf.com/")
web_handler = handle_html()
web_handler.feed(web.read())
