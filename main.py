# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:27 2020

@author: James
"""
import detectface as df
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
    
def get_angles():
    face, eye = df.get_coordinate_pair()
    angle_horizontal, angle_vertical = df.calculate_angles(eye, face)
    print(angle_horizontal, angle_vertical)
    return angle_horizontal, angle_vertical


x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)

xgrid, ygrid = np.meshgrid(x, y)
zgrid = 1 / np.square(xgrid * ygrid)


fig = plt.figure("Eye of Sauron")
ax = fig.gca(projection="3d")
ax.set_axis_off()
surface = ax.plot_surface(zgrid, ygrid, xgrid, cmap=cm.hsv)
fig.show()
while True:
    horizontal, vertical = get_angles()
    ax.view_init(horizontal, vertical)
    plt.draw()
    plt.pause(0.01)