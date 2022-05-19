import re

pattern="\d+"
str="我的电话是：18019237601,tony's phone number is 1651198787"
# findall 匹配字符串中所有符合正则的内容，返回list
# result=re.findall(pattern,"我的电话是：18019237601")


#finditer：匹配字符串中所有的内容，返回迭代器,用.group()拿到内容
# it=re.finditer(pattern,"我的电话是：18019237601,tony's phone number is 1651198787")
#
# for i in it:
#     print(i.group())

#sreach全文检索，找到一个结果就返回
# s=re.search(pattern,"我的电话是：18019237601,tony's phone number is 1651198787")
# print(s.group())

# match从头开始匹配
# s=re.match(pattern,"18019237601我的电话是：18019237601,tony's phone number is 1651198787")
# print(.group())

# 预加载正则表达式
# obj=re.compile(pattern)
# # result=obj.finditer(str)
# result=obj.findall(str)
# for i in result:
#     print(i)

a = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
obj=re.compile("<div class='.*?'><span id='(?P<id>\d)'>(?P<wahaha>.*?)</span></div>",re.S) #re.S:让.可以匹配换行符;(?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取
result=obj.finditer(a)
for it in result:
    print(it.group("wahaha"))
    print(it.group("id"))