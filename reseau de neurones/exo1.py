#!/usr/bin/python3

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as p
import numpy as np


data = p.read_csv('human_resources.csv')

def get_info(dataf):
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


def label_encode(data):
	# Transforme un type catégorie en entier
	le = LabelEncoder()
	le2 = LabelEncoder()
	# On récupère tous les noms de catégories possibles
	unique_values_sales = list(data['sales'].unique())
	unique_values_salary = list(data['salary'].unique())
	le_fitted_sales = le.fit(unique_values_sales)
	le_fitted_salary = le2.fit(unique_values_salary)
	# On liste l'ensemble des valeurs
	values_sales = list(data['sales'].values)
	values_salary = list(data['salary'].values)
	# On transforme les catégories en entier
	values_transformed_sales = le.transform(values_sales)
	values_transformed_salary = le2.transform(values_salary)
	# On fait le remplacement de la colonne dans le dataframe d'origine
	data['sales'] = values_transformed_sales
	data['salary'] = values_transformed_salary

def plot_correlation(dataf):
	corr = dataf.corr()
	#fig, ax = plt.subplots(figsize=(10, 10))
	#ax.matshow(corr)
	#plt.xticks(range(len(corr.columns)), corr.columns);
	#plt.yticks(range(len(corr.columns)), corr.columns);
	#plt.show()
	plt.figure(figsize=(15,8))
	sns.set()
	hm = sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, cmap='RdYlGn',vmax=0.5)
	plt.show()
	
def plot_anarchie(data): 
	newdata = data[data['number_project'] > data['number_project'].mean()]
	newdata = newdata[data['average_montly_hours'] > data['average_montly_hours'].mean()]
	newdata = newdata[data['time_spend_company'] > data['time_spend_company'].mean()]
	newdata = newdata[data['last_evaluation'] > data['last_evaluation'].mean()]

	plot_correlation(newdata)





def main():

	label_encode(data)
	plot_anarchie(data)

	(train, test) = train_test_split(data, test_size = 0.3333)
	ytrain = train['left']
	xtrain = train
	del(xtrain['left'])

	ytest = test['left']
	xtest = test
	del(xtest['left'])

	neurones = MLPClassifier(solver='adam')
	model = neurones.fit(xtrain, ytrain)
	print("Precision train:")
	print(model.score(xtrain, ytrain))

	ypred = model.predict(xtest)
	print("Precision test:")
	print(model.score(xtest, ytest))
	confmat = confusion_matrix(ytest, ypred)
	print("Matrice de confusion")
	print(confmat)


	#plot_correlation(data)
	
	
main()
