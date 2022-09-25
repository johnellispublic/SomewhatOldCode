import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mandelbrot(c):
    out = np.zeros(c.shape)
    z = np.zeros(c.shape, dtype=np.complex128)
    for i in range(200):
        z = z**2 + c
        out[(z.real**2 + z.imag**2 < 4)] += 1
    out[(out == 200)] = 0
    return out

minx = -2
maxx = 2
miny = -2
maxy = 2

x = np.linspace(minx, maxx,1000)
y = np.linspace(miny, maxy,1000)

X,Y = np.meshgrid(x,y)
C = np.zeros(Y.shape, dtype=np.complex128)
C.real = X
C.imag = Y
out = mandelbrot(C)
centre_around = (-0.76415,-0.09515)
step = 0.9

def update(t):
    global minx, maxx, miny, maxy

    x = np.linspace(minx, maxx,1000)
    y = np.linspace(miny, maxy,1000)

    X,Y = np.meshgrid(x,y)
    C = np.zeros(Y.shape, dtype=np.complex128)
    C.real = X
    C.imag = Y

    minx = (minx-centre_around[0])*step + centre_around[0]
    maxx = (maxx-centre_around[0])*step + centre_around[0]
    miny = (miny-centre_around[1])*step + centre_around[1]
    maxy = (maxy-centre_around[1])*step + centre_around[1]


    out = mandelbrot(C)

    im.set_array(out)
    print(t)

#plt.figure()
#plt.contourf(X,Y,out)

fig = plt.figure()
im = plt.imshow(out, extent=[minx, maxx, miny, maxy])
anim = FuncAnimation(fig, update, frames=1000)
anim.save('mandel.mp4',fps=24)
#plt.show()
