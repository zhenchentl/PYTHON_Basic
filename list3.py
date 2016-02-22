__author__ = 'xiaolin'

def search(list,x):
    for i in range(len(list)):
        if list[i]==x:
            return 1
    return -1

list=[1,2,4,3,5,6,7,'apple']
print search(list,'apple')

print list.index('apple')


def bi_search(list,x):
    #list.sort()
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)/2
        if list[mid]==x:
            return mid
        elif list[mid]>x:
            low=mid-1
        else:
            high=mid+1
    return -1
print bi_search(list,4)


