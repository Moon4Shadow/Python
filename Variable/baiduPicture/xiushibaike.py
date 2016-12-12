import requests
import re

page = 1
url = "http://qiushibaike.com/hot/page/"+str(page)+"/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = { 'User-Agent' : user_agent }

QSBK = requests.get(url,headers = headers)
print(QSBK.url)


#print (qsbk.text)

pattern = '<div.*?class="content">(.*?)<!--.*?-->.*?</div>'
items = re.findall(pattern,QSBK.text,re.S)
item = []
for item in items:
    print(item)
print(QSBK.url)