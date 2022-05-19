import requests

# name=input("请输入要查询的人名：")
# par={'query':'周杰伦'}
# url='https://www.sogou.com/web?'
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
# }
# resp =requests.get(url,headers=headers,params=par)
# print(resp.text)

url="https://movie.douban.com/j/chart/top_list?"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}
par={
    "type": "24",
    "interval_id":"100:90",
    "action":"",
    "start": "0",
    "limit": "20"
 }
resp=requests.get(url,params=par,headers=headers)
print(resp.json())
resp.close()