# -*- coding: utf-8 -*-
"""
Script for plotting basic softmax function.
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def softmax(x_0, x_1, x_2):
    u = np.exp(x_0) + np.exp(x_1) + np.exp(x_2)
    y_0 = np.exp(x_0)/u
    y_1 = np.exp(x_1)/u
    y_2 = np.exp(x_2)/u
    return y_0, y_1, y_2

n = 20
x_0 = np.linspace(-4, 4, n)
x_1 = np.linspace(-4, 4, n)

y = np.zeros((n, n, 3))
for i_0 in range(n):
    for i_1 in range(n):
        y[i_1, i_0, :] = softmax(x_0[i_0], x_1[i_1], 1)

xx_0, xx_1 = np.meshgrid(x_0, x_1)

plt.figure(figsize=(8, 3))
for i in range(2):
    axes = plt.subplot(1, 2, i+1, projection='3d')
    axes.plot_surface(xx_0, xx_1, y[:, :, i],
                      rstride=1, cstride=1, alpha=0.3,
                      color='blue', edgecolor='black')
    axes.set_xlabel('$x_0$', fontsize=14)
    axes.set_ylabel('$x_1$', fontsize=14)
    axes.view_init(40, -125)

plt.show()