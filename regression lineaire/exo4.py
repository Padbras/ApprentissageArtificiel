#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[6], [8], [10], [14], [18]])
Y = [7,9,13,17.5,18]
X_test = np.array([[8], [9], [11], [16], [12]])
Y_test = [11,8.5,15,18,11]



regr = LinearRegression()
regr.fit(X,Y)
prediction = regr.predict(X)

RSS = 0

for i in range(0,len(Y)):
	RSS += (Y[i] - prediction[i])**2


print("Le RSS obtenu est : {}".format(RSS))

vari =  np.var(X, ddof = 1)
covar = np.cov(X.transpose(),Y)[0][1]
print("La variance obtenu est : {}".format(vari))
print("La covariance obtenu est : {}".format(covar))

alpha = ( covar / vari )
print("Le alpha obtenu est : {}".format(alpha))

beta= np.mean(Y)-(alpha*np.mean(X))
print("Le beta obtenu est : {}".format(beta))

square = regr.score(X_test,Y_test)
print("Le Rsquared obtenu est : {}".format(square))
#plt.plot(X,Y, '.')
#plt.plot(X,prediction)
#plt.axis([0, 25, 0, 25])
#plt.show()
