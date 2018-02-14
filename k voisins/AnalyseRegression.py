#!/usr/bin/python3

import pandas as p
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler 


dataf = p.read_csv('auto-mpg.csv')
del(dataf['name'])


def get_info():
	print("INFO:")
	dataf.info() # resume rapide
	print("SHAPE:")
	print(dataf.shape) #dimensions du df
	print("DESCRIBE:")
	print(dataf.describe()) # stats sur les tendances
	print("HEAD:")
	print(dataf.head()) # premieres lignes
	#print("VALUES COUNT:")
	#dataf.value_counts() # nb occurences chaque valeur
	#print(dataf['Species'].value_counts())



def plot_data(x,y):
	plt.figure()
	plt.title("Plot 1")
	plt.xlabel("Repartition uniforme")
	plt.ylabel("10*sin(x)/x")
	plt.scatter(x, y, color = 'black', marker = 'o', label = "points")
	plt.axis([-5,15,-5,15])
	plt.grid(True)
	plt.show()


def main():

	#Normalisation importante qd notion de distance
	get_info()
	ss = StandardScaler()
	(train, test) = train_test_split(dataf, test_size= 0.3333)
	ytrain = train['mpg']
	xtrain = train
	del(xtrain['mpg'])
	xtrain = ss.fit_transform(xtrain)
	
	ytest = test['mpg']
	xtest = test
	del(xtest['mpg'])
	xtest = ss.fit_transform(xtest)
	
	
	knd = KNeighborsRegressor(n_neighbors=11)
	model = knd.fit(xtrain, ytrain )
	
	ypred = model.predict(xtest)
	print("R2 SCORE:")
	print(r2_score(ytest, ypred))
	print("MAE:")
	print(mean_absolute_error(ypred, ytest))
	print("MSE:")
	print(mean_squared_error(ypred, ytest))

	#confmat = confusion_matrix(ytest, ypred)

	#print(confmat)
	

main()
