# -*- coding: utf-8 -*-
"""
Script for plotting basic exponential function.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100)

y_1 = 2**x

y_2 = 3**x

y_3 = 0.5**x

plt.figure(figsize=(5, 5))
plt.plot(x, y_1, 'black', linewidth=3, label='$y=2^x$')
plt.plot(x, y_2, 'cornflowerblue', linewidth=3, label='$y=3^x$')
plt.plot(x, y_3, 'gray', linewidth=3, label='$y=0.5^x$')
plt.xlim(-4, 4)
plt.ylim(-2, 6)
plt.legend(loc='lower right')
plt.grid(True)
plt.show()