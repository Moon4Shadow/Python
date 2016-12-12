import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
a = datepat.match('11/27/2012adfaer')
b = datepat.match('11/27/2012')
print(a)
print(b)