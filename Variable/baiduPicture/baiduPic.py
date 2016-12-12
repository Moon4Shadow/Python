import os
import urllib
import re
import requests

url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%AE%A0%E7%89%A9"

outpath = "d:\\pic1\\p"


def getHtml(url):
    s = requests.session()
    html = s.get(url)
    print(html.content)
    return html


def getImageList(html):
    restr = '(http(s)?:\/\/[^\s,"]*\.(jpg|jpeg|png|gif|bmp))'
    # htmlurl = re.compile(restr)
    # findall(), 参数1：patternStr  参数2：网页源码str  参数3：
    imgList = re.findall(restr, html.content.decode(), re.S)
    if 0 == len(imgList):
        print('URL获取为空或失败...')
    else:
        print('URL获取成功...')
    return imgList


def download(imgList, page):
    img_num = 0
    for imgurl in imgList:
        '''
        type(imgurl) 为 str
        type(data)   为 bytes
       '''
        realurl = imgurl[0]
        data = urllib.request.urlopen(realurl).read()
        houzui = str(realurl).split(".")
        FileName = str('image/') + str(img_num) + '.' + houzui[-1]
        print('[Debug] Download file :' + str(realurl) + ' >> ' + FileName)
        with open(FileName, 'wb') as f:
            f.write(data)
        img_num += 1


def downImageNum(pagenum):
    page = 1
    pageNumber = pagenum
    while (page <= pageNumber):
        html = getHtml(url)  # 获得url指向的html内容
        imageList = getImageList(html)  # 获得所有图片的地址，返回列表
        download(imageList, page)  # 下载所有的图片
        page = page + 1


if __name__ == '__main__':
    downImageNum(1)