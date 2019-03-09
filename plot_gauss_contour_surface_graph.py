# -*- coding: utf-8 -*-
"""
Script for plotting gaussian contour and surface graph.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def show_2d_gauss_contour(x_0, x_1):
    xx_0, xx_1 = np.meshgrid(x_0, x_1)
    xxx_0 = np.reshape(xx_0, 40*40, 1)
    xxx_1 = np.reshape(xx_1, 40*40, 1)
    y = np.exp(-(xxx_0**2 + xxx_1**2))
    y = y.reshape(40, 40)
    y = y.T
    cont = plt.contour(xx_0, xx_1, y, 15, colors='k')

def show_3d_gauss_surface(ax, x_0, x_1):
    xx_0, xx_1 = np.meshgrid(x_0, x_1)
    xxx_0 = np.reshape(xx_0, 40*40, 1)
    xxx_1 = np.reshape(xx_1, 40*40, 1)
    y = np.exp(-(xxx_0**2 + xxx_1**2))
    y = y.reshape(40, 40)
    y = y.T
    ax.plot_surface(xx_0, xx_1, y,
                    rstride=2, cstride=2, alpha=0.3,
                    color='blue', edgecolor='black')

x_0 = np.linspace(-3, 3, 40)
x_1 = np.linspace(-3, 3, 40)

Fig = plt.figure(1, figsize=(7, 3))
Fig.add_subplot(1, 2, 1)
show_2d_gauss_contour(x_0, x_1)
plt.ylim(-3, 3)
plt.xlim(-3, 3)
plt.xlabel('$x_0$', fontsize=14)
plt.ylabel('$x_1$', fontsize=14)
plt.grid(True)
Ax = Fig.add_subplot(1, 2, 2, projection='3d')
show_3d_gauss_surface(Ax, x_0, x_1)
Ax.set_xlabel('$x_0$', fontsize=14)
Ax.set_ylabel('$x_1$', fontsize=14)
Ax.view_init(40, -100)
plt.show()

