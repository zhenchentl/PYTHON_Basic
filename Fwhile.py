__author__ = 'xiaolin'
import time

for i in range(1,11):
    print i
    time.sleep(1)
    if i==3:
        pass
    if i==2:
        continue
    #if i==5:
     #   exit()   #jump out of the whole loop
    if i==6:
        break


for i in range(3):
    print '->'*10,i

while True:
    print 'hello'
    x= raw_input("input q:")
    if x=='q':
        break

x=''
while x!='q':
    print 'hello'
    x= raw_input("input q:")
    if not x:        #directly input enter can also stop
        break
