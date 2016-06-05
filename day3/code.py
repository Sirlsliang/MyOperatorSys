#coding:utf-8
#图像尺寸太小的话无法识别
#导入pillow
from PIL import Image
from bs4 import BeautifulSoup
import pytesseract
import cStringIO

import urllib2
web = urllib2.urlopen("http://www3.tust.edu.cn/yjs/sj_vote_16/inc/code.asp")

im = Image.open(cStringIO.StringIO(web.read()))

#gImage = im.convert("L")
#gImage.show()


rImage = im.resize((180,45))
gImage = rImage.convert("L")
vcode = pytesseract.image_to_string(gImage)
print vcode
#out = gImage.point(lambda i:i*1.2+10)
gImage.show()
