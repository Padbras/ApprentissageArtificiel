#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[6], [8], [10], [14], [18]])
Y = [7,9,13,17.5,18]

plt.plot(X,Y, '.')
plt.axis([0, 25, 0, 25])
plt.show()
