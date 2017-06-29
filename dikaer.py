import itertools
import numpy as np
x=itertools.product(test["c1"],test["c2"])
tmp=pd.DataFrame()
for i,j in x:
    tmp2=pd.DataFrame({"c1":[i],"c2":[j]})
    tmp=pd.concat([tmp,tmp2],axis=0,ignore_index=True)


print(tmp)    
print(test[["c1"]])
pd.merge(test[["c1"]],test[["c2"]],left_on="c1",right_on="c2",how="outer")
tmp

import itertools  
for i in  itertools.product([1, 2, 3], [4, 5], [6, 7]):  
    print (i ) 
  
def product(*args, **kwds):  
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy  
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111  
    pools = map(tuple, args) * kwds.get('repeat', 1)  
    result = [[]]  
    for pool in pools:  
        result = [x+[y] for x in result for y in pool]  
    for prod in result:  
        yield tuple(prod)  
  
def decare(args):  
    result = [[]]  
    for pool in args:  
        # result = [x+[y] for x in result for y in pool]  
        tmp = []  
        for x in result:  
            for pinyin in pool:  
                tmp.append(x + [pinyin])  
        result = tmp  
    print ('result: ', result ) 
    print (len(result))  
  
# name_arry = ['wang', 'liu'], ['hua', 'xue'], ['feng']  
product([1, 2, 3], [4, 5], [6, 7])  
