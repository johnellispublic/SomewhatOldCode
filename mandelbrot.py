import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import matplotlib as mpl

detail = 200

def mandel(c, z=0, func=lambda z,c : z**2 + c):
    out = np.zeros(np.shape(c)) - 1
    if type(z) == int:
        z = np.zeros(np.shape(c)) + z
    t = 0
    while True:
        out[((np.abs(z) >= 2) & (out < 0))] = t
        z = func(z, c)
        print("   ",t)
        yield out
        t += 1

def calc_mandel(minr, maxr, mini, maxi, detail=200, maxlvl=60):
     x = np.linspace(minr, maxr, detail)
     y = np.linspace(mini, maxi, detail)
     Y, X = np.meshgrid(y,x)
     C = X + Y*1j
     z = mandel(C)
     for i in range(maxlvl):
         next(z)
     return next(z)

def zoom_around(rc,ic,plot,rate=1/30,detail=200):
     minr = -2
     maxr = 2
     mini = -2
     maxi = 2
     while True:
         z = calc_mandel(minr,maxr,mini,maxi,detail)
         plot.set_array(z[:-1, :-1].ravel())
         yield plot
         minr = (minr - rc) * (1-rate) + rc
         maxr = (maxr - rc) * (1-rate) + rc
         mini = (mini - ic) * (1-rate) + ic
         maxi = (maxi - ic) * (1-rate) + ic

class Update:
    def __init__(self,rc, ic, plot, rate=1/60):
        self.z = zoom_around(rc, ic, plot, rate, detail=detail)

    def update(self, frame):
        print(frame)
        return next(self.z)


fig, ax = plt.subplots()
Y, X = np.meshgrid(np.linspace(-2,2,detail),np.linspace(-2,2,detail))
C = X + Y*1j

cmap = mpl.cm.viridis
norm = mpl.colors.Normalize(vmin=-1, vmax=30)

plot = plt.pcolormesh(X,Y,np.abs(C),cmap=cmap, norm=norm)
u = Update(-1.5,0,plot)

plt.axis('equal')

ani = FuncAnimation(fig, u.update, frames=1200, interval=1000/30)
writer = animation.FFMpegWriter(fps=30)
ani.save("mandel.mp4", writer=writer)
