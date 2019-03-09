# -*- coding: utf-8 -*-
"""
Script for plotting basic gaussian function.
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussian_func(mu, sigma, a):
    y = a * np.exp(-(x-mu)**2/sigma**2)
    return y

x = np.linspace(-4, 6, 100)

plt.figure(figsize=(4, 4))
plt.plot(x, gaussian_func(0, 1, 1), 'black', linewidth=3)
plt.plot(x, gaussian_func(3, 2, 0.3), 'gray', linewidth=3)
plt.ylim(-0.5, 1.5)
plt.xlim(-4, 6)
plt.grid(True)
plt.show()

