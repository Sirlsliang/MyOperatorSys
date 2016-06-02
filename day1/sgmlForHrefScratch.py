# coding:utf-8
#!/usr/bin/python
#Filename:simpleScratch.py
#解析href 标签
import urllib
import sgmllib

class handle_html(sgmllib.SGMLParser):
    #使用try 与 except 来避免报错。但不推荐
    def unknown_starttag(self,tag,attrs):
        try:
            for attr in attrs:
                if attr[0] == "href":
                    print(attr[0]+":"+attr[1].encode('utf-8'))
        except:
            pass

web = urllib.urlopen("http://freebuf.com/")
web_handler = handle_html()
web_handler.feed(web.read())
