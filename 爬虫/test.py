import requests
from urllib.request import urlopen
url='http://www.baidu.com'
resp=urlopen(url)
with open('baidu.html',encoding='utf-8',mode='w') as f:
    f.write(resp.read().decode('utf-8'))
    print('over')
