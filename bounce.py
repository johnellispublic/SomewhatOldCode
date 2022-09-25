import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

MINX = -10
MAXX = 10
MINY = -10
MAXY = 10

fps = 30
t = 1000
g = -1
D = 0.99

class Ball:
    def __init__(self,vx,vy):
        self.x = 5
        self.y = 0
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx / fps
        self.y += self.vy / fps
        self.calc_grav()
        while not (MINX <= self.x <= MAXX) or not (MINY <= self.y <= MAXY):
            print(self.x, self.y, end=" | ")
            self.bounce()
            print(self.x, self.y)

    def calc_grav(self):
        r = (self.x**2 + self.y**2)**0.5
        self.vx += g * self.x / (r**3) / fps
        self.vy += g * self.y / (r**3) / fps

    def bounce(self):
        if self.x > MAXX:
            self.x = 2 * MAXX - self.x
            self.vx *= -1
        if self.x < MINX:
            self.x = 2*MINX - self.x
            self.vx *= -1
        if self.y > MAXY:
            self.y = 2*MAXY - self.y
            self.vy *= -1
        if self.y < MINY:
            self.y = 2*MINY - self.y
            self.vy *=-1

x_data = []
y_data = []
ball = Ball(1, 1)
fig, ax = plt.subplots()
line, = ax.plot([],[])
dot = ax.scatter(0,0)
plt.xlim(MINX, MAXX)
plt.ylim(MINY, MAXY)

def update(tick):
    x_data.append(ball.x)
    y_data.append(ball.y)
    line.set_data(x_data, y_data)
    dot.set_offsets([x_data[-1],y_data[-1]])
    ball.move()
    #print(x_data)

ani = FuncAnimation(fig, update, frames=(fps*t), interval=(1000/fps))
writervideo = FFMpegWriter(fps=fps)
ani.save("bounce.mp4", writer=writervideo)
