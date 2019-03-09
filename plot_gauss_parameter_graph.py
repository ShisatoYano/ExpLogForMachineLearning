# -*- coding: utf-8 -*-
"""
Script for plotting graph of gaussian function with parameters.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def gaussian(x, mu, sigma):
    col_num, row_num = x.shape
    a_1            = 1/(2*np.pi)
    a_2            = 1/(np.linalg.det(sigma)**(1/2))
    inv_sigma      = np.linalg.inv(sigma)
    xmu            = x - mu
    xmu_sigma      = np.dot(xmu, inv_sigma)
    xmu_sigma_xmut = np.zeros(col_num)
    for r in range(row_num):
        xmu_sigma_xmut = xmu_sigma_xmut + xmu_sigma[:, r] * xmu[:, r]
    y = a_1 * a_2 * np.exp(-xmu_sigma_xmut/2)
    return y

def show_2d_gauss_contour(x_0, x_1, mu, sigma):
    xx_0, xx_1 = np.meshgrid(x_0, x_1)
    xxx_0      = np.reshape(xx_0, 40*40, 1)
    xxx_1      = np.reshape(xx_1, 40*40, 1)
    x          = np.c_[xxx_0, xxx_1]
    y          = gaussian(x, mu, sigma)
    y          = y.reshape(40, 40)
    y          = y.T
    cont = plt.contour(xx_0, xx_1, y, 15, colors='k')

def show_3d_gauss_surface(ax, x_0, x_1, mu, sigma):
    xx_0, xx_1 = np.meshgrid(x_0, x_1)
    xxx_0      = np.reshape(xx_0, 40*40, 1)
    xxx_1      = np.reshape(xx_1, 40*40, 1)
    x          = np.c_[xxx_0, xxx_1]
    y          = gaussian(x, mu, sigma)
    y          = y.reshape(40, 40)
    y          = y.T
    ax.plot_surface(xx_0, xx_1, y,
                    rstride=2, cstride=2, alpha=0.3,
                    color='blue', edgecolor='black')

x_0   = np.linspace(-3, 3, 40)
x_1   = np.linspace(-3, 3, 40)
mu    = np.array([1, 0.5])
sigma = np.array([[2, 1], [1, 1]])

Fig = plt.figure(1, figsize=(7, 3))
Fig.add_subplot(1, 2, 1)
show_2d_gauss_contour(x_0, x_1, mu, sigma)
plt.ylim(-3, 3)
plt.xlim(-3, 3)
plt.xlabel('$x_0$', fontsize=14)
plt.ylabel('$x_1$', fontsize=14)
plt.grid(True)
Ax = Fig.add_subplot(1, 2, 2, projection='3d')
show_3d_gauss_surface(Ax, x_0, x_1, mu, sigma)
Ax.set_xlabel('$x_0$', fontsize=14)
Ax.set_ylabel('$x_1$', fontsize=14)
Ax.view_init(40, -100)
plt.show()

