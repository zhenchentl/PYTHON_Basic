__author__ = 'xiaolin'
#coding=utf-8
def is_palindrome(name):
    low=0
    high=len(name)-1
    while low<high:
        if name[low]!=name[high]:
            return False
        low+=1
        high-=1
    return True

def is_palinrome_rec(name):
    if len(name)<=1:
        return True
    else:
        if name[0]!=name[-1]:
            return False
        else:
            return is_palinrome_rec(name[1:-1])


f=open('names.txt','r')
for line in f:
    line=line.strip()
    if is_palindrome(line):
        print line.title()

f.close()

def is_ascending(name):
    p=name[0]
    for c in name:
        if p>c:
            return False
        p=c  #after the compare the variable is changed to the bigger one
    return  True

def is_ascending_rec(name):    #this is the cycle one
    if len(name)<2:
        return True
    if name[0]>name[1]:
        return False
    else:
        return is_palinrome_rec(name[1:])



import math
print math.pi
print 'PI is {:.4f}'.format(math.pi)


import re
f=open('names.txt')  #re which is very important
pattern='(c,a)'
for line in f:
    name=line.strip()
    result=re.search(pattern,name)
    if result:
        print 'find in {}'.format(name)

f.close()

