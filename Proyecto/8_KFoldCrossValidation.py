import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
# print(iris)

# Se distribuye la data en trainy test

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)


# Se realiza el modelo predictivo lineal 
print('----------------Linear--------------------')
clf = svm.SVC(kernel='linear', C=1).fit(x_train,y_train)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print(scores.mean())
print(clf.score(x_test, y_test)) 

# una vez que ya se tiene el modelo se puede evaluar 5 veces como se ejecuta el modelo predictivo
# se puede evaluar si el modelo mejora siendo una funcion polinomica

print('-----------Polinomial ------------------')
clf=svm.SVC(kernel='poly',degree=3, C=1).fit(x_train, y_train)
scores=cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print(scores.mean())
print(clf.score(x_test, y_test))