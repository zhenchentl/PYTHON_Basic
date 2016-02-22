__author__ = 'xiaolin'
stundents=[['zhang',84],['wang',98],['li',76]]
print float(sum([x[1] for x in stundents]))/len(stundents)

 # sum([i for i in range(1,7) if 6 % i== 0])

 #def f(a):
  #   return a[1]
#

stundents.sort(key=lambda x:x[1], reverse=True) #lambda is the definition  function
print stundents
