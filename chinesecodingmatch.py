#coding=utf-8
import re


ss='<sd>中文：123aaanfkfkdfjdkfjdk</sd>'
sss=re.compile('<sd>(中文：.*?)aa.*?</sd>')

result=re.findall(sss,ss)
result
print result
