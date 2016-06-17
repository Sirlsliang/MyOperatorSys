from urllib import request
from bs4 import BeautifulSoup
import pymysql # 注意在python3中的mysql包

#获取连接对象，注意后面的charset最好写上，在本机测试时默认为latin-1编码，出现了编码错误的问题
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='myscratch',charset="utf8")

#获取游标对象
cur = conn.cursor()

#执行sql语句，这个语句是指定使用的库
cur.execute('USE myscratch')
url = "http://shop.freebuf.com/"
print("Prepare&reading to read the web")
data = request.urlopen(url).read()
print("parsing...............")
soup = BeautifulSoup(data)
itemlist = soup.findAll(name='div',attrs={'class':'col-sm-6 col-md-4 col-lg-4 mall-product-list'})

for item in itemlist:
    name = item.find(name='h4').string
    price = item.find(name='strong').string

    query = "insert into scraping(name,price) values("+"\'"+name+"\',"+price +");"
    print("query="+query)
    #执行上面的数据库语句
    cur.execute(query)
conn.commit()
print("Success to update the database")

print("Preparing to read the data from database")

query = "Select * from scraping;"
#执行上面的数据库语句
cur.execute(query)
#打印获取的数据库对象，此时可以发现，获取的数据对象也是存在游标对象里面的。
print(cur.fetchall())

#关闭连接，清理资源，注意顺序
cur.close()
conn.close()
#根据以上我们可以看到，python3中连接数据库时，首先要获取到其连接对象conn
#然后利用连接对象获取游标对象cur
#利用游标对象cur进行sql操作，
#利用游标对象获取数据
#清理资源，关闭连接


