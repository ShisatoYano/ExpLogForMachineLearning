# -*- coding: utf-8 -*-
"""
Script for plotting differential of exponential function.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0001, 4, 100)
y = np.log(x)
dy = 1/x

plt.figure(figsize=(4, 4))
plt.plot(x, y, 'black', linestyle='--', linewidth=3, label='$log x$')
plt.plot(x, dy, 'cornflowerblue', linewidth=3, label='$1/x$')
plt.legend(loc='lower right')
plt.ylim(-8, 8)
plt.xlim(-1, 4)
plt.grid(True)
plt.show()