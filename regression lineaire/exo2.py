#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[6], [8], [10], [14], [18]])
Y = [7,9,13,17.5,18]



regr = LinearRegression()
regr.fit(X,Y)
prediction = regr.predict(X)

plt.plot(X,Y, '.')
plt.plot(X,prediction)
plt.axis([0, 25, 0, 25])
plt.show()
