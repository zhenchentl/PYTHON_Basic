__author__ = 'xiaolin'
def vowles_count(s):
    count=0
    for c in s:
        if c in 'aeiouAEIOU':
            count+=1

    return count

print vowles_count('hello world, nice to meet you')

name='appleasdsdsfdsf'
'apple' in name

print name[0:5]
print name[0:5:2]
name='appleapple'
print len(name)
print name[:len(name)/2]

print name[:1]+'a'+'b'+name[2:] #infact this means to insert ab to between 1and 2
print name.replace('pp','nn')


ss='123123123123'
print ss.replace('1','x',2)

ip='135.252.208.183'
print ip.split('.')

def f(x):
    if x>5:
        return True

l=range(10)
filter(f,l)