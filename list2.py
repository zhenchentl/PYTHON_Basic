__author__ = 'xiaolin'
nums=[]
for i in range(10):
    nums.append(float(raw_input())) #it can be input through direct input

avg=sum(nums)/len(nums)
print avg

def search(list,x):
    for i in range(len(list)):
        if list[i]==x:
            return 1
    return -1

list=[1,2,3,4,5,6,7,'apple']
print search(list,'apple')

print list.index('apple')