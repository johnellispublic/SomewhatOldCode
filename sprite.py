import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation

BOARD_SIZE = 20
G = 0.01

def get_r(x,y):
    return (x**2 + y**2)**0.5

class Sprite:

    def __init__(self, position_x, position_y, velocity_x, velocity_y, character):
        self.pos_x = position_x
        self.pos_y = position_y
        self.vel_x = velocity_x
        self.vel_y = velocity_y
        self.character = character

    def get_avg_distance(self, other, timestep=1):
        v1 = np.array([self.vel_x, self.vel_y])
        v2 = np.array([other.vel_x, other.vel_y])

        x1 = np.array([self.pos_x, self.pos_y])
        x2 = np.array([other.pos_x, other.pos_y])

        r = (v2 - v1)*timestep/2 + x1 - x2
        return r + 1e-100

    def get_distance(self,other):
        return get_r(self.pos_x - other.pos_x, self.pos_y - other.pos_y)

    def reflect_x(self, x):
        self.pos_x = 2*x - self.pos_x
        self.vel_x = -self.vel_x

    def reflect_y(self, y):
        self.pos_y = 2*y - self.pos_y
        self.vel_y = -self.vel_y

    def reflect(self, minx, maxx, miny, maxy):
        if self.pos_x < minx:
            self.reflect_x(minx)
        elif self.pos_x > maxx:
            self.reflect_x(maxx)

        if self.pos_y < miny:
            self.reflect_y(miny)
        elif self.pos_y > maxy:
            self.reflect_y(maxy)

    def collide(self, other,G=G,timestep=1):

        r = self.get_avg_distance(other, timestep)
        F = G/np.linalg.norm(r)**2
        a = F * r/np.linalg.norm(r) * timestep
        self.vel_x += a[0]
        self.vel_y += a[1]

    def stop(self):
        self.vel_x = 0
        self.vel_y = 0

    def move(self, timestep=1, reflect=True, minx=0, maxx=BOARD_SIZE, miny=0, maxy=BOARD_SIZE):
        self.pos_x += self.vel_x * timestep
        self.pos_y += self.vel_y * timestep

        if reflect:
            self.reflect(minx, maxx, miny, maxy)

    def get_pos(self):
        return self.pos_x, self.pos_y

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def get_char(self):
        return self.character

    def draw(self, placeholder="#",height=BOARD_SIZE,width=BOARD_SIZE):
        output = ""
        for y in range(height):
            for x in range(width):

                if y == self.pos_y and x == self.pos_x:
                    output += self.character
                else:
                    output += placeholder
            output += "\n"

        print(output)

    def __repr__(self):
        return f"<Sprite at ({self.pos_x},{self.pos_y}) ({self.vel_x},{self.vel_y})>"

class Board:
    def __init__(self, height, width, placeholder, sprites):
        self.height = height
        self.width = width
        self.placeholder = placeholder
        self.sprites = sprites

    def init_ani(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.scatter = self.ax.scatter([],[])

    def create_sprite_at(self, x, y, vx, vy):
        sprite = Sprite(x, y, vx, vy, "@")
        self.sprites.append(sprite)

    def get_sprite_pos(self):
        pos = np.ndarray((len(self.sprites),2))
        for s in range(len(self.sprites)):
            pos[s,0] = self.sprites[s].get_x()
            pos[s,1] = self.sprites[s].get_y()
        return pos

    def update(self,t, timestep=1):
        self.tick(timestep)
        data = self.get_sprite_pos()
        self.scatter.set_offsets(data)
        return self.scatter


    def animate(self, timestep, frame_num=1000, fps=60, filename=""):
        self.init_ani()
        self.ani = FuncAnimation(self.fig, self.update, frame_num, fargs=(timestep,), interval=10)
        if not filename:
            plt.show()
        else:
            writervideo = animation.FFMpegWriter(fps=fps)
            self.ani.save(filename, writer=writervideo)

    def draw(self):
        out = []
        for y in range(self.height):
            out.append([])
            for x in range(self.width):
                out[-1].append(self.placeholder)

        for sprite in self.sprites:
            x,y = sprite.get_pos()
            char = sprite.get_char()
            if y < self.height and x < self.width:
                out[y][x] = char

        for row in range(len(out)):
            out[row] = "".join(out[row])

        out = "\n".join(out)
        print(out)

    def sprite_at(self,x,y):
        for sprite in self.sprites:
            if (x,y) == sprite.get_pos():
                return sprite

        return None

    def tick(self,timestep=1, reflect=True):
        for sprite in self.sprites:
            sprite.move(timestep, reflect=reflect, maxx=self.width, maxy=self.height)

        for sprite in self.sprites:
            for other in self.sprites:
                if sprite != other and Sprite.get_distance(sprite, other) < 2:
                    sprite.collide(other,timestep=timestep)

    def __repr__(self):
        return f"<Board {repr(self.sprites)}>"
