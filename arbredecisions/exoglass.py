import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def main():
	data = pd.read_csv("glass.csv")
	(train, test) = train_test_split(data, test_size = 0.3333)

	x_train = train
	y_train = train['Type']
	del x_train['Type']
	del x_train['Id']

	x_test = test
	y_test = test['Type']
	del x_test['Type']
	del x_test['Id']

	classifier = tree.DecisionTreeClassifier(criterion='entropy')
	model = classifier.fit(x_train, y_train)
	print("PRECISION DU FIT TRAIN:")
	print(model.score(x_train, y_train))

	ypred = model.predict(x_test)
	print("PRECISION DU FIT TEST:")
	print(model.score(x_test, y_test))

	confmat = confusion_matrix(y_test, ypred)

	print(confmat)

	
	tree.export_graphviz(classifier, out_file='tree2.dot',
		feature_names=['refractive index', 'Sodium', 'Magnesium', 'Aluminium','Silicon', 'Potassium', 'Calcium', 'Barium', 'Iron' ])

if __name__ == '__main__':
	main()
