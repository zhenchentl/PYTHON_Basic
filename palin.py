__author__ = 'xiaolin'
def is_palin(num,num_p=0):

num_t=num
while num_t !=0:
    num_p=num_p*10+num_t%10
    num_t=num_t/10

if  num == num_p:
   print 'YES'
else:
   print 'NO'
return num

