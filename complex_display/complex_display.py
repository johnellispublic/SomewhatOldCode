import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

MINX = -10
MINY = -10
MAXX = 10
MAXY = 10

XSTEPCOUNT = 1000
YSTEPCOUNT = 1000

BRIGHTNESS = 0.1

x = np.linspace(MINX,MAXX,XSTEPCOUNT)
y = np.linspace(MINY,MAXY,YSTEPCOUNT)

X,Y = np.meshgrid(x,y)
C = np.zeros(Y.shape, dtype=np.complex128)
C = X + Y*1j
print(C)
def g(z):
    return z*np.sqrt(z.real**2 + z.imag**2)**-3

def f(z):
    m1 = 1
    m2 = -10
    return m1*g(z-(0+2j))+m2*g(z-(0-2j))

C = f(C)
C_H = np.arctan(C.imag/C.real) / (2*np.pi)
C_H[(C.real < 0)] += 1/2
C_H[((C.real > 0) & (C.imag < 0))] += 1

C_S = np.zeros(C.shape) + 1
C_V = np.sqrt(C.real**2 + C.imag**2)
C_V *= BRIGHTNESS
#C_V /= np.max(C_V)
C_V[(C_V > 1)] = 1
print(X[0,0]+Y[0,0]*1j, C[0,0])


C_hsv1 = np.ndarray((len(x),len(y),3))
C_hsv1[:,:,0] = C_H
C_hsv1[:,:,1] = C_S
C_hsv1[:,:,2] = C_V

C_hsv2 = np.zeros(C_hsv1.shape)
C_hsv2 += 1
C_hsv2[:,:,0] = C_H

C_rgb1 = hsv_to_rgb(C_hsv1)
C_rgb2 = hsv_to_rgb(C_hsv2)

plt.subplot(221)
plt.imshow(C_rgb1)

plt.subplot(222)
plt.imshow(C_rgb2)

plt.subplot(223)
plt.imshow(C_V)
plt.show()
