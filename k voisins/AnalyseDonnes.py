#!/usr/bin/python3

import pandas as p
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

dataf = p.read_csv('iris.csv')


def get_info():
	print("INFO:")
	dataf.info() # resume rapide
	print("SHAPE:")
	print(dataf.shape) #dimensions du df
	print("DESCRIBE:")
	print(dataf.describe()) # stats sur les tendances
	print("HEAD:")
	print(dataf.head()) # premieres lignes
	print("VALUES COUNT:")
	dataf.value_counts() # nb occurences chaque valeur
	print(dataf['Species'].value_counts())


def plot_data(x,y):
	plt.figure()
	plt.title("Plot 1")
	plt.xlabel("Repartition uniforme")
	plt.ylabel("10*sin(x)/x")
	plt.scatter(x, y, color = 'black', marker = 'o', label = "points")
	plt.axis([-5,15,-5,15])
	plt.grid(True)
	plt.show()

#REPONSES AUX QUESTIONS
# Combien de classes?
#3


# Combien de carac descriptives? Quel types? 
# 4 de types float (64bits)

# Combien d'exemple? 
#150

# Cb d'ex de chaque classe? 
# 50


# Comment sont organisés les ex? 
# dans l'ordre des iris

##########################################

# INFLUENCE DE K
# Ne pas avoir k = nb de point ! (en general, sqrt(nbpoints) ) 

def main():
	(train, test) = train_test_split(dataf, test_size = 0.3333)
	ytrain = train['Species']
	xtrain = train
	del(xtrain['Species'])
	del(xtrain['Id'])
	ytest = test['Species']
	xtest = test
	del(xtest['Species'])
	del(xtest['Id'])
	
	knd = KNeighborsClassifier(n_neighbors=5)
	model = knd.fit(xtrain, ytrain )
	print("PRECISION DU FIT TRAIN:")
	print(model.score(xtrain, ytrain))
	
	ypred = model.predict(xtest)
	print("PRECISION DU FIT TRAIN:")
	print(model.score(xtest, ytest))

	confmat = confusion_matrix(ytest, ypred)

	print(confmat)
	

main()
