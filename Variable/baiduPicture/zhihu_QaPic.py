# -*-coding:utf-8-*-
import requests
import time
import json
import sys
import os
from bs4 import BeautifulSoup

#reload(sys)
#sys.setdefaultencoding('utf-8')

email = '454989772@qq.com'
password = 'Moon4Shadow'
head = {'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://www.zhihu.com',
        'Accept-Language': 'zh-CN',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Host': 'www.zhihu.com'}
url = "http://www.zhihu.com"
s = requests.session()
html = s.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
xrsf = soup.find('input')
#print(xrsf.get('value'))

# 验证码
yanzhen_url = 'https://www.zhihu.com/captcha.gif?r=' + str(int(time.time() * 1000))
haha = s.get(yanzhen_url, headers=head)

with open('code.jpg', 'wb') as f:
    f.write(haha.content)
print('请输入验证码')
yanzhen = input()

print('验证码:' + yanzhen)

login_data = {'_xsrf': xrsf,
              'password': password,
              'captcha': yanzhen,
              'email': email,
              'remember_me': 'true'}

r = s.post('https://www.zhihu.com/login/email', data=login_data, headers=head)
print
r.text
jsonre = json.loads(r.text)
print
jsonre["msg"]
# 验证一下是否登录成功
question = "30137203"
question_url = "http://www.zhihu.com/question/" + question
res = s.get(question_url)
# print res.text
soup = BeautifulSoup(res.text, 'html.parser')
# 找出所有的回答包括的div
answer_num = soup.find('h3', attrs={"id": "zh-question-answer-num"})['data-num']
title = soup.find('h2', class_="zm-item-title zm-editable-content").text
divs = soup.findAll('div', class_="zm-item-answer")
div_list = []
for each in divs:
    div_list.append(each)

xsrf = soup.find("input", attrs={"name": "_xsrf"})['value']
pagesize = 50
offset = 50

while offset < int(answer_num):
    more_url = "https://www.zhihu.com/node/QuestionAnswerListV2"
    more_data = {
        "method":"next",
        "params":"{\"url_token\":"+question+",\"pagesize\":"+str(pagesize)+",\"offset\":"+str(offset)+"}",
        "_xsrf":xsrf
    }
    res = s.post(more_url,data = more_data,headers = head)
    more_json = json.loads(res.text)
    more_msg = more_json["msg"]
    #将list转换为字符串类型
    more_msg = "".join(more_msg)
    soup = BeautifulSoup(more_msg,"html.parser")
    divs = soup.findAll('div',class_="zm-item-answer")
    for each in divs:
        div_list.append(each)
    offset = offset + pagesize


def downloadImg(div_list):
    answer_count = 0
    dir = os.path.join(os.path.abspath("."), question)
    for each in div_list:
        imgs = each.find('div', class_="zm-editable-content clearfix").findAll('img',
                                                                               class_="origin_image zh-lightbox-thumb")
        author = each.find('div', class_="zm-item-answer-author-info")
        # 对匿名用户的处理
        if len(author) == 3:
            author = str(answer_count)
        else:
            author = author.find('a', class_="author-link")
            author = author.text
        img_count = 0
        print
        "正在下载第" + str(answer_count) + "/" + str(answer_num) + "名用户：" + author + "的答案"
        for img in imgs:
            img_url = img['src'].encode("utf-8")
            if img_url[0] == 'h':
                print
                "正在下载第" + str(img_count) + "张图片"
                ss = requests.session()
                img_content = ss.get(img_url)
                name = img_url.split(".")
                with open(os.path.join(dir, author + "_" + str(img_count) + "." + name[-1]), 'wb') as f:
                    f.write(img_content.content)
                img_count = img_count + 1
        answer_count = answer_count + 1

        # 创建目录


path = os.path.join(os.path.abspath("."), question)
if not os.path.isdir(path):
    os.mkdir(path)
downloadImg(div_list)