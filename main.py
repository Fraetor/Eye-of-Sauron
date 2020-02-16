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
    #print(angle_horizontal, angle_vertical)
    return angle_horizontal, angle_vertical

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

fig = plt.figure("Eye of Sauron")
ax = fig.gca(projection="3d")
ax.set_axis_off()
surface = ax.plot_surface(x, y, z, cmap=cm.Set1)
fig.show()

while True:
    plt.draw()
    horizontal, vertical = get_angles()
    print(horizontal, vertical)
    ax.view_init(azim=horizontal, elev=vertical)
    plt.pause(0.01)
