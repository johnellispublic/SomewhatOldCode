import operator as op
from functools import reduce
import numpy as np

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

x = np.float128(2)

nIn = [1,1/2,1/6,0,-1/30,0,1/42,0,-1/30,0]

for r in np.arange(len(nIn),50,dtype=np.float128):
    S = np.sum(np.arange(0,x+1)**r,dtype=np.float128)
    k = np.zeros(int(r),dtype=np.float128)

    for n in np.arange(r,dtype=np.float128):
        #print(nIn[n]*ncr(n,r) / (r-n))
        k[int(n)] = nIn[int(n)]*ncr(int(r),int(n))
        k[int(n)] /= (r-n+1)
        #print(k[n], end=" ")

    aprox = np.float128(0)
    for n in np.arange(r,dtype=np.float128):
        aprox += x**(r+1-n)*k[int(n)]
        #print(x**(r+1-n))

    #print("|", S, aprox)
    if -1e-5 < (S-aprox)/x < 1e-5:
        nIn.append(0)
    else:
        nIn.append((S-aprox)/x)

print("\n".join([str(i) for i in nIn]))
