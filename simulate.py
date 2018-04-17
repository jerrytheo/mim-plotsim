from environment import Environment
import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
import numpy as np


def horizontal_line(xstart, xstop, yval):
    xstop += 0.01
    return np.vstack((
        np.arange(xstart, xstop, 0.01),
        np.full(int(round((xstop - xstart) * 100)), yval),
    ))


def vertical_line(xval, ystart, ystop):
    ystop += 0.01
    return np.vstack((
        np.full(int(round((ystop - ystart) * 100)), xval),
        np.arange(ystart, ystop, 0.01),
    ))


def simple_map():
    walls = [
        # Outer walls.
        ['vertical', 0, 0, 10],
        ['vertical', 10, 0, 10],
        ['horizontal', 0, 10, 10],
        ['horizontal', 0, 4.5, 0],
        ['horizontal', 5.5, 10, 0],

        # Bottom left room.
        ['vertical', 4.5, 0, 2],
        ['vertical', 4.5, 3, 5],
        ['horizontal', 1.5, 4.5, 5],

        # Right room.
        ['vertical', 5.5, 0, 3],
        ['horizontal', 5.5, 9, 3],
        ['vertical', 9, 3, 9],
    ]

    pts = []
    for wall in walls:
        if wall[0] == 'vertical':
            xval, ystart, ystop = wall[1:]
            for x in np.arange(xval-.02, xval+.02, .01):
                pts.append(vertical_line(x, ystart, ystop))

        if wall[0] == 'horizontal':
            xstart, xstop, yval = wall[1:]
            for y in np.arange(yval-.02, yval+.02, .01):
                pts.append(horizontal_line(xstart, xstop, y))

    return np.hstack(pts).T


if __name__ == '__main__':
    print('Initializing environment => ')
    env = Environment(
        simple_map, nbot=2, center=(0, 0), radius=1.)

    max_iter = 1
    for i in range(max_iter):
        env.update()
    plt.show()

    # ani = FuncAnimation(env.fig, env, interval=50)
    # env.plot()
    # print('')
