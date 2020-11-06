import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# Lectura del archivo
input_file = 'C:/Users/ediso/Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/PastHires.csv'
df = pd.read_csv(input_file, header = 0)
# print(df)

# Cambio de valores alfanimericos a numericos por columna
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
# print(df)

# Construccion del arbol de decision
features = list(df.columns[:6])
# print(features)

y = df["Hired"]
X = df[features]

clf = tree.DecisionTreeClassifier(max_depth=10, random_state=0)
clf = clf.fit(X,y)

fig, axes=plt.subplots(nrows=1, ncols=1, figsize=(4,4), dpi=300)
tree.plot_tree(clf, feature_names=features)  
# fig.savefig('img1.png')
# plt.show()

# Siel coeficiente gini (entropy) es mayor a cero aun se pueden dividir las ramas del arbol

# --------------------------------  RANDOM FOREST -----------------------------------------------


#  usamos un random forest de 10 decision trees para predecir el empleo de un candidato especifico
from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(n_estimators=10)
clf = clf.fit(X,y)

# Predict employment of an employed 10-year veteran
print(clf.predict([[10,1,4,0,0,0]]))

# Predict employment of an unemployed 10-year veteran
print(clf.predict([[10,0,4,0,0,0]]))