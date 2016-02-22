__author__ = 'xiaolin'
import random
def parking(low,high):
    if high-low < 1:
        return 0
    else:
        x=random.uniform(low,high-1)
        return parking(low,x)+1+parking(x+1,high)



s=0
for i in range(100000):
    s+=parking(0,10)

print s/100000.