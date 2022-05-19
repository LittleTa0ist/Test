import re
import requests
import csv
url="https://movie.douban.com/top250?start=25&filter="
n=0
while n<250:
    url="https://movie.douban.com/top250?start={}&filter=".format(n)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    resp = requests.get(url, headers=header)

    obj = re.compile(
        r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?(?P<year>\d+).*?</p>.*?<span property="v:best" content="10.0"></span>.*?<span>(?P<count>.*?)</span>',
        re.S)
    result = obj.finditer(resp.text)
    with open("data.csv", mode='a+', newline='',encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        for it in result:
            dic = it.groupdict()
            csvwriter.writerow(dic.values())
    n = n + 25

