#coding=utf-8

import re
f=open('emma.txt','r')
count=0
for s in f.readlines(): # readlines函数返回的是数据的列表，数据较多时候可以使用
    result=re.findall('do',s)
    if len(result)>0:
        count=count+len(result)
print count
f.close()
#下面的操作具有相同的效果
import re
f=open('emma.txt','r')
s=0
pattern='do'
for line in f:
    name=line.strip() #strip函数用来删除空白符，吃醋实际上可以删除掉
    result=re.findall(pattern,name)
    f.wirte(name.replace('do','doo'))# 替换do为doo
    if len(result)>0:
        s=s+len(result)
print s
f.close()      

l=['one\n','two\n']
f=open('emma.txt','a') #此处意思在文件的末尾写入
f.writelines(l)
f.close()

l=['one\n','two\n']
f=open('emma.txt','r+')
f.seek(0,2)# 从文章开头添加数字，若是seek(0,2)则表示指针指向末尾
f.writelines(l)
# f.flush()
f.close()
