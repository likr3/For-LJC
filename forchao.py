#coding=utf-8
import urllib
import re
import os



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html,path,offset):
    reg = r'src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = offset
    for imgurl in imglist:

        urllib.urlretrieve(imgurl,path+'\%s.jpg' % x)
        x+=1


index='C:\Users\liker\PycharmProjects\untitled\pic'

if os.path.exists(index) == False:
        os.mkdir(index)

htmllist=["http://www.tongxinimage.com/?cat=5"]

base="http://bbs.fengniao.com/forum/pic/slide_540_8997412_815584"

for i in range(0,15):
    htmllist.append(base+str(43+i)+".html")


'''
path1=[]
for i in range(len(htmllist)):
    direction=index+str(i)
    if os.path.exists(direction) == False:
        os.mkdir(direction)
    path1.append(direction)
'''


for j in range(len(htmllist)):
   getImg(getHtml(htmllist[j]),index,100*j)


print("Done!")