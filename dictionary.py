#coding=utf-8
__author__ = 'xiaolin'
my_dic={'john':1234,'bob':5678,'mike':8765,'trt':1234,'wdc':5678}
print my_dic
my_dic2={}
for name, age in my_dic.items():  #dictionary reverse
    if age in my_dic2:
        my_dic2[age].append(name)
    else:
        my_dic2[age]=[name]
print my_dic2


print my_dic['bob']
my_dic['tom']=2345
print my_dic
len(my_dic)
# bob in my_dic
for name,age in my_dic.items():
    print name
    print age


print my_dic.items()
s='asdsfdsfdsfdfdfdfwerewjoj'
lst=[0]*26

for i in s:
    lst[ord(i)-97]+=1 #ji qiao xing feichang de qiang
print lst

d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print d

f=open('emma.txt')
word_freq={}
for line in f:
    words=line.strip().split()  #is this neccessary
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1

freq_word=[]
for word,freq in word_freq.items():
    freq_word.append((freq,word))
freq_word.sort(reverse=True)
print freq_word[:10]
f.close()
#读写文件
f=open(r'd:/Xiaolin/Documents/test.txt,'a')
       f.writelines(['nihao','sb'])
       f.close()
       
