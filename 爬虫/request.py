import requests

url='https://www.sogou.com/web?query=周杰伦'
resp=requests.get(url)
print(resp.text)

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}
resp =requests.get(url,headers=headers)
with open('jay.html',mode='w',encoding='utf-8') as f:
    f.write(resp.text)