import matplotlib.pyplot as plt
import numpy as np

FOV = 35

def f_x(t):
    return np.cos(t*10)

def f_y(t):
    return np.sin(t*10)

def f_z(t):
    return t

def f(t):
    x = f_x(t)
    y = f_y(t)
    z = f_z(t)
    out = np.empty(t.shape+(3,))
    out[:, 0] = x
    out[:, 1] = y
    out[:, 2] = z
    return out

def perspective(out, FOV=FOV):
    persp_x = out[:, 0]/out[:, 2]
    persp_y = out[:, 1]/out[:, 2]

    persp_x[(out[:, 2] <= 0)] = np.nan
    persp_y[(out[:, 2] <= 0)] = np.nan

    return persp_x, persp_y

def calc_screen_width(FOV=FOV):
    screen_width = np.tan(FOV * np.pi/180)
    return screen_width

def rotate(out, y=0, p=0, r=0): #y is yaw, p is pitch, r is roll
    yaw_matrix = np.array([
        [np.cos(y),  -np.sin(y),    0],
        [np.sin(y),   np.cos(y),    0],
        [0,           0,            1]
    ])
    pitch_matrix = np.array([
        [np.cos(p),   0,            np.sin(p)],
        [0,           1,            0],
        [-np.sin(p),  0,            np.cos(p)]
    ])
    roll_matrix = np.array([
        [1,           0,            0],
        [0,           np.cos(r),    -np.sin(r)],
        [0,           np.sin(r),    np.cos(r)]
    ])
    rotation_matrix = yaw_matrix @ pitch_matrix @ roll_matrix
    out[:] = out[:] @ rotation_matrix
    return  out

def translate(out, x=0, y=0, z=0):

    out[:,0] += x
    out[:,1] += y
    out[:,2] += z

    return out

def display(x, y, screen_width):
    ax = plt.gca()
    ax.plot(x, y)
    plt.xlim(-screen_width, screen_width)
    plt.ylim(-screen_width, screen_width)
    ax.set_aspect('equal')
    plt.show()

def main():
    t = np.arange(-100, 500, 0.01)
    out = f(t)
    out = translate(out, 10, 0, 0)
    out = rotate(out, 0, 1.57, 0)
    x, y = perspective(out)
    screen_width = calc_screen_width()
    display(x, y, screen_width)

if __name__ == "__main__":
    main()
