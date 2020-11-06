import sklearn.datasets as datasets
from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# check for the sklearn version, it has to be 0.21
import sklearn
print(sklearn.__version__)


breast_cancer = datasets.load_breast_cancer()

clf = DecisionTreeClassifier(max_depth=5) #max_depth is maximum number of levels in the tree
clf.fit(breast_cancer.data, breast_cancer.target)

plt.figure(figsize=(30,15))
a = plot_tree(clf, 
              feature_names=breast_cancer.feature_names, 
              class_names=breast_cancer.target_names, 
              filled=True, 
              rounded=True, 
              fontsize=14)
plt.show()