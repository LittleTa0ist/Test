import requests
import re
import csv

url="https://m.dytt8.net/index2.htm"
domain="https://m.dytt8.net"
resp=requests.get(url)
resp.encoding='gb2312'

obj1=re.compile(r'2022新片精品.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'>",re.S)
obj3=re.compile(r'<h1><font color=#07519a>(?P<name>.*?)</font></h1>.*?'
                r'<a target="_blank" href="(?P<link>.*?)">',re.S)
result=obj1.finditer(resp.text)
for it in result:
    ul=it.group('ul')
    result2=obj2.finditer(ul)
    for itt in result2:
        if re.search(r'app',itt.group("href")):
            pass
        else:
            print(itt.group("href"))
            sub_url=domain+itt.group("href")
            sub_resp = requests.get(sub_url)
            sub_resp.encoding="gb2312"
            # print(sub_resp.text)
            result3=obj3.finditer(sub_resp.text)
            f = open("data.csv", mode="+a",encoding="utf-8")
            csvwriter = csv.writer(f)
            for ittt in result3:
                dic=ittt.groupdict()
                csvwriter.writerow(dic.values())
resp.close()
sub_resp.close()