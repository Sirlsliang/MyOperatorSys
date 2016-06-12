from urllib import request

from bs4 import BeautifulSoup
import csv

csvFile = open("items.csv",'w+')

url = "http://shop.freebuf.com"

web = request.urlopen(url)
data = web.read()
soup = BeautifulSoup(data)

itemList = soup.findAll(name='div',attrs={"class":"col-sm-6 col-md-4 col-lg-4 mall-product-list"})
print(len(itemList))

writer = csv.writer(csvFile)
writer.writerow(('name','price'))


for item in itemList:
    name = item.find(name="h4").string
    price = item.find(name="strong").string
    writer.writerow((name,price))

csvFile.close()
 
print("Success To Create The CSVFile")
