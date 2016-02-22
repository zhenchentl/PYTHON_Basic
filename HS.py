__author__ = 'xiaolin'
def p(n):
   if n==1 or n==0:
       return 1
   else:
       return n*p(n-1)

print p(3)

def fbnq(n):
    if n==1 or n==2:
        return 1
    else:
        return fbnq(n-1)+fbnq(n-2)

print fbnq(10)