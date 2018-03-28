#!/usr/bin/python3

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as p
import numpy as np

data = p.read_csv('hour.csv')

def label_encode(data):
	# Transforme un type catégorie en entier
	le = LabelEncoder()
	le2 = LabelEncoder()
	# On récupère tous les noms de catégories possibles
	unique_values_dteday = list(data['dteday'].unique())
	le_fitted_dteday = le.fit(unique_values_dteday)
	# On liste l'ensemble des valeurs
	values_dteday = list(data['dteday'].values)
	# On transforme les catégories en entier
	values_transformed_dteday = le.transform(values_dteday)
	# On fait le remplacement de la colonne dans le dataframe d'origine
	data['dteday'] = values_transformed_dteday


def main():

	label_encode(data)

	(train, test) = train_test_split(data, test_size = 0.3333)
	ytrain = train['cnt']
	xtrain = train
	del(xtrain['cnt'])

	ytest = test['cnt']
	xtest = test
	del(xtest['cnt'])

	neurones = MLPRegressor()
	model = neurones.fit(xtrain, ytrain)

	ypred = model.predict(xtest)

	print("R2 SCORE:")
	print(r2_score(ytest, ypred))
	print("MAE:")
	print(mean_absolute_error(ypred, ytest))
	print("MSE:")
	print(mean_squared_error(ypred, ytest))
	
main()
