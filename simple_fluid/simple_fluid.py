import numpy as np
import matplotlib.pyplot as plt

R = 8.3
SCALE = 1

class Array(np.ndarray):
    def __init__(self, *args, default=0, **kwargs):
        self.default = default
        super().__init__(*args, **kwargs)

    def __getitem__(self, item, *args, **kwargs):
        if item in self:
            return super().__getitem(self, item, *args, **kwargs)
        else:
            return self.default

def P(n,T):
    return n*R*T

def cardinals_to_vector(N,S,E,W):
    return E-W, N-S

def simulate(VN,VE,VS,VW,n,T,Mr):
    pressure = P(n,T)
    DPN =



    return VN,VE,VS,VW,n,T

x = np.arange(0,10,SCALE)
Y,X = np.meshgrid(x,x)

VN = np.zeros(X.shape) + 0.01
VE = np.zeros(X.shape) + 0.01
VS = np.zeros(X.shape) + 0.01
VW = np.zeros(X.shape) + 0.001

V,U = cardinals_to_vector(VN,VS,VE,VW)

n = np.zeros(X.shape) + 1000/24
T = np.zeros(X.shape) + 300

plt.streamplot(Y,X,V,U)
plt.show()
