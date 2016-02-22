__author__ = 'xiaolin'
num=int(raw_input('input:'))
num_p=0
num_t=num
is_palin=False
is_prime=False
while num_t !=0:
    num_p=num_p*10+num_t%10
    num_t=num_t/10

if  num == num_p:
    is_palin=True

for i in range(2,num):
    if num % i == 0:
        break
else:
        is_prime=True

if is_prime and is_palin:
    print 'OK'
else:
    print'NO'

