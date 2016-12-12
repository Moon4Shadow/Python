import os
import json
import requests
import urllib

# queryWord 搜索关键词
# word 搜索关键词
# pn （0,30,60，...）偏移值为30
def BaiduPicSearchUrlBuild(keyWord, offSet):
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

url = BaiduPicSearchUrlBuild('佐助', 0)
print(url)
hData= urllib.request.urlopen(url).read()
JData = json.loads(hData.decode())
i = 0
for x in JData['data']:
    if len(x) != 0:
        if len(x['replaceUrl']) == 2:
            print(str(i) + ':', x['replaceUrl'][1]['ObjURL'])
        i += 1