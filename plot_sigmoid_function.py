# -*- coding: utf-8 -*-
"""
Script for plotting basic sigmoid function.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = 1 / (1 + np.exp(-x))

plt.figure(figsize=(5, 5))
plt.plot(x, y, 'black', linewidth=3)
plt.xlim(-10, 10)
plt.ylim(-1, 2)
plt.grid(True)
plt.show()