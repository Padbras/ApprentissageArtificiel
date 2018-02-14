import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix




def main():

	data = pd.read_csv("winequality-red.csv")
	(train, test) = train_test_split(data, test_size = 0.3333)

	x_train = train
	y_train = train['quality']
	del x_train['quality']

	x_test = test
	y_test = test['quality']
	del x_test['quality']


	classifier = tree.DecisionTreeRegressor(max_depth = 50, min_samples_leaf = 10, min_impurity_decrease = 0.02)
	model = classifier.fit(x_train, y_train)
	ypred = model.predict(x_test)

	print("R2 SCORE:")
	print(r2_score(y_test, ypred))
	print("MAE:")
	print(mean_absolute_error(y_test, ypred))
	print("MSE:")
	print(mean_squared_error(y_test, ypred))

	#confmat = confusion_matrix(y_test, ypred)
	#print(confmat)

	
	tree.export_graphviz(classifier, out_file='tree3.dot',
		feature_names=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol' ])

if __name__ == '__main__':
	main()


