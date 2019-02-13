# -*- coding: utf-8 -*-
"""
Script for plotting basic logarithm function.
"""

import numpy as np
import matplotlib.pyplot as plt

x_1 = np.linspace(-8, 8, 100)
x_2 = np.linspace(0.001, 8, 100)

y_1 = 2**x_1
y_2 = np.log(x_2)

plt.figure(figsize=(5, 5))
plt.plot(x_1, y_1, 'black', linewidth=3, label='$y=2^x$')
plt.plot(x_2, y_2, 'cornflowerblue', linewidth=3, label='$y=log_{2}x$')
plt.plot(x_1, x_1, 'black', linestyle='--', linewidth=1, label='$y=x$')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.legend(loc='lower right')
plt.grid(True)
plt.show()