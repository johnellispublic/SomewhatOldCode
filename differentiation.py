import numpy as np

def diff(x, f, n=1,dx=1e-2):
    out = np.zeros(np.shape(x), dtype=np.float128)
    for r in range(0,n+1):
        out += (-1)**r * np.math.comb(n,r) * f(x + (n-r)*dx)

    return out / dx**n
