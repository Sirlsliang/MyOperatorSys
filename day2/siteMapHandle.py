#!/usr/bin/python3

from urllib import request,parse

from bs4 import BeautifulSoup
import time

url = "http://eshu.tust.edu.cn"
domain = "eshu.tust.edu.cn"
deep =0
tmp =""
vTime =2
#存储所有的网页链接的集合
sites = set()
visited = set()

def get_local_pages(url,domain):
    global deep
    global sites
    global tmp
    repeat_time = 0
    pages = set()
    
    #打开一个url
    #防止url读取卡住,使用了一个循环，如果读取不到就一直对网站发出请求，发出5次请求还不成功后就不再请求了
    while True:
        try:
            print("Read to Open the Web")
            time.sleep(vTime)
            print("Opening the url: "+ url)
            web = request.urlopen(url=url,timeout=3)
            print("Success to Open the web")
            break
        except:
            print("Open url failed !!! Repeat")
            time.sleep(vTime)
            repeat_time = repeat_time+1
            if repeat_time ==5:
                #如果5次请求之后该网站还不能打开就放弃
                return
        
    print("Readint the web ...")
    #创建解析器，并取名为soup
    soup = BeautifulSoup(web.read())
    print("............")
    #获取页面中所有的a标签,并放入tags中
    tags = soup.findAll(name="a")
    for tag in tags:
        #避免参数异常
        try:
            #读取a标签中的href属性值，操作方法和字典一样。属性可以被添加、删除或修改
            ret = tag['href']
        except:
            print("Maybe not the attr: href")
            #continue 关键字是继续进行循环的下一步操作
            continue
        #解析依次获取到的url:返回的格式为：scheme://netloc/path;parameters?query#frament
        u = parse.urlparse(ret)

        #处理相对路径
        if u[0] is "" and u[1] is "":
            print("Relative page: "+ret)
            #web.geturl()方法，获取爬取的页面传入的url
            url_obj =  parse.urlparse(web.geturl())
            #将相对的url地址拼接成一个完整的url
            ret = url_obj[0]+"://"+url_obj[1]+url_obj[2]+ret
            #保持url的干净,处理url，使url的后面不会出现"//"
            ret = ret[:8]+ret[8:].replace("//","/")

            #继续处理url
            u = parse.urlparse(ret)
            #u[2]是指的path,下面时去除掉url中的../
            if '../' in u[2]:
                paths = u[2].split('/')
                for i in range(len(paths)):
                    if paths[i] == '..':
                        paths[i] =''
                        if paths[i-1]:
                            paths[i-1] = ''
                tmp_path = ''
                for path in paths:
                    if path == '':
                        continue
                    tmp_path = tmp_path+'/'+path
                ret = ret.replace(u[2],ret_path)
            print(" FixedPage:" +ret)
        #处理完的地址就变成绝对地址了，绝对地址的协议
        #协议处理
        if 'http' not in u[0]:
            print("Bad Page: " + ret)
            continue
        #url合理性检验
        if u[0] is "" and u[1] is not "":
            print("Bad page:" + ret)
            continue
        #域名检验
        if domain not in u[1]:
            print("Bad Page:"+ret)
            continue

        #整理，输出
        newPage = ret
        if newPage not in sites:
            print("Add New Page:"+newPage)
            pages.add(newPage)
    return pages


#dfs 算法遍历全站
def dfs(pages):
    if not pages:
        return 
    global url
    global domain
    global sites
    global visited

    global deep
    #返回一个新的set，该site 包含s，和t中的每一个元素。
    sites = sites.union(pages)
    for page in pages:
        if page not in visited:
            print("Visiting: "+page)
            visited.add(page)
            url = page
            pages = get_local_pages(url,domain)
            dfs(pages)
    print("Success")

pages = get_local_pages(url,domain)
dfs(pages)
print("所有的site为:")
for i in sites:
    print(i)
