import os
import requests
import urllib
import re
import time

singleCharDict = { 'w':"a", 'k':"b", 'v':"c", '1':"d", 'j':"e", 'u':"f", '2':"g", 'i':"h",
                   't':"i", '3':"j", 'h':"k", 's':"l", '4':"m", 'g':"n", '5':"o", 'r':"p",
                   'q':"q", '6':"r", 'f':"s", 'p':"t", '7':"u", 'e':"v", 'o':"w", '8':"1",
                   'd':"2", 'n':"3", '9':"4", 'c':"5", 'm':"6", '0':"7", 'b':"8", 'l':"9",
                   'a':"0" }
mutiCharDict = { '_z\&e3B':".", 'AzdH3F': "/", '_z2C\$q':":" }

def parseBaiduPicSearchUrl( url ):
    '根据字符映射,解析加密的图片url'
    objURL = url
    for key, value in mutiCharDict.items():
        patt = re.compile(key)
        objURL = patt.sub(value, objURL)
    l = list(objURL)
    objURL = ''
    for c in l:
        if (c in singleCharDict.keys()):
            c = singleCharDict[c]
        objURL += c
    return objURL

# queryWord 搜索关键词
# word 搜索关键词
# pn （0,30,60，...）偏移值为30
def baiduPicSearchUrlBuild( keyWord, offSet ):
    '构建百度图片搜索url(已简化)'
    keyWord = urllib.parse.quote(keyWord)
    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&queryWord=' + keyWord + '&word=' + keyWord +'&&pn=' + str(offSet) + '&rn=30'
    return url

"""
header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
          "Host":"image.baidu.com",
          "Referer":"http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1481341409974_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BD%90%E5%8A%A9&f=3&oq=zuozhu&rsp=0",
         }
req = requests.get(url, header)
hData= urllib.request.urlopen(req.url).read()
"""
print('请输入搜索关键字：')
keyWord = '广工' #input()
print('请输入爬取页数：')
pageNum = 20 #int(input())
while pageNum <= 0:
    print('爬取页数错误，请重新输入：')
    pageNum = int(input())

i = 0
j = 1
while i < pageNum:
    url = baiduPicSearchUrlBuild(keyWord, i * 30)
    hData = urllib.request.urlopen(url).read()
    # 不直接用json.load()解析,可能会因格式出错
    # 故，选择直接对获取的数据进行正则筛选，获取目标数据
    restr = "\"objURL\":\"(ippr[^,]*)"
    urlList = re.findall(restr, hData.decode(), re.S)

    for x in urlList:
        objURL = parseBaiduPicSearchUrl(x)
        l = list(objURL.split('&url='))  # 特殊处理：url中提取包含的url
        if len(l) > 1:
            objURL = l[-1]
        print('objURL ' + str(j) + ':' + objURL)
        j += 1
    i += 1
    time.sleep(0.3)

