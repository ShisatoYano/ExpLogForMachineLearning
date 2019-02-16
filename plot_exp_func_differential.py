# -*- coding: utf-8 -*-
"""
Script for plotting differential of exponential function.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-4, 4, 100)
e = math.e
a = 2
y = a**x
dy = np.log(a) * y
print(np.log(a))

plt.figure(figsize=(4, 4))
plt.plot(x, y, 'black', linestyle='--', linewidth=3, label='$a^x$')
plt.plot(x, dy, 'cornflowerblue', linewidth=3, label='$a^x log a$')
plt.legend(loc='lower right')
plt.ylim(-1, 8)
plt.xlim(-4, 4)
plt.grid(True)
plt.show()