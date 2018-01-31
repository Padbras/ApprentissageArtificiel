#!/usr/bin/python3

import math as m
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures #as poly
from sklearn.metrics import r2_score, median_absolute_error, median_squared_error


def plot_data(x,y):
	plt.figure()
	plt.title("Plot 1")
	plt.xlabel("Repartition uniforme")
	plt.ylabel("10*sin(x)/x")
	plt.scatter(x, y, color = 'black', marker = 'o', label = "points")
	plt.axis([-5,15,-5,15])
	plt.grid(True)
	plt.show()


def generationpoints(nb):
	x = [np.random.uniform(-3,10) for i in range(nb)]
	x = np.sort(x)
	return x 

def calculvaleurs(ensemble): 
	x = list(map(lambda t : 10*(m.sin(t)/t) + np.random.normal(0,1,1), ensemble))
	return x
		
def training(degrees,x,y): 
	models = [make_pipeline(PolynomialFeatures(degree), Ridge()) for degree in degrees]
	for model in models:
		model.fit(x,y)
	return models

def show_polynomes(models, degrees, x, y):
	x_plot = np.linspace(-3,10,100).reshape(-1,1)
	colors = ['green', 'orange', 'red', 'blue', 'brown']
	plt.figure()
	plt.title("Plot 1")
	plt.xlabel("Repartition uniforme")
	plt.ylabel("10*sin(x)/x")
	plt.scatter(x,y,s=50, marker = 'o', label = "courbes")
	plt.axis([-5,15,-5,15])
	count = 0
	for degree in degrees: 
		y_plot = models[count].predict(x_plot)
		plt.plot(x_plot, y_plot, color=colors[count], label = 'degrees %d'%degree)
		count+=1
		plt.grid(True)
	plt.show()

def compute_errors(models,degrees, x,y ): 
	count = 0
	for model in models:
		prediction = model.predict(x)
		print('Degree %d : RSS moyen %2f'%(degrees[count], np.mean((y-prediction)**2)))
		count+=1


def print_r_squared(models, degrees,x,y):
	count = 0
	for model in models: 
		print('Degree %d, R_squared %2f'%(degrees[count], model.score(x,y)))
		count+=1

def main():
	np.random.seed(1337)
	xtrain = generationpoints(15)
	ytrain = calculvaleurs(xtrain)
	xtrain = np.asarray(xtrain).reshape(-1,1)
	plot_data(xtrain, ytrain)
	degrees = [1,3,6,9,12]
	models = training(degrees,xtrain , ytrain)
	show_polynomes(models, degrees, xtrain, ytrain)
	compute_errors(models, degrees, xtrain, ytrain)
	
	xtest = generationpoints(50)
	ytest = calculvaleurs(xtest)
	yreal = list(map(lambda t : 10*(m.sin(t)/t), xtest))
	xtest = np.asarray(xtest).reshape(-1,1)
	plot_data(xtest,ytest)

	show_polynomes(models, degrees, xtest, ytest)
	compute_errors(models, degrees, xtest,yreal)
	print_r_squared(models, degrees, xtest, yreal)

main()

