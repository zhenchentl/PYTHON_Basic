__author__ = 'xiaolin'

xx=float(raw_input('input:'))

low=0
high=xx
guess=(low+high)/2

while  abs(guess**2-xx)>1e-5:
    if guess**2>xx:
        high=guess
    else:
        low=guess
    guess=(low+high)/2
else:
    print guess

