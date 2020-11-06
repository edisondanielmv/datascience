import numpy as np
import matplotlib.pyplot as plt

def createClusteredData (N,k):
    pointsPerCluster = float (N)/k
    x=[]
    y=[]
    for i in range (k):
        incomeCentroid = np.random.uniform(20000.0,200000.0)
        ageCentroid = np.random.uniform(20.0,70.0)
        for j in range (int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid,10000.0), np.random.normal(ageCentroid,2.0)])
            y.append(i)
    x=np.array(x)
    y=np.array(y)
    return x,y

(x,y)=createClusteredData(100,5)

plt.figure(figsize=(8,6))
plt.scatter(x[:,0], x[:,1], c=y.astype(np.float))
plt.show()

# ----------------------------- SVM ------------------------------------------
from sklearn import svm, datasets
c=1.0
# svc = svm.SVC(kernel='linear', c=c).fit(x,y)
svc = svm.SVC(kernel='linear').fit(x,y)
def plotPredictions(clf):
    xx,yy = np.meshgrid(np.arange(0, 250000, 10), np.arange(10,70,0.5))
    z=clf.predict(np.c_[xx.ravel(), yy.ravel()])

    plt.figure(figsize=(8,6))
    z=z.reshape(xx.shape)
    plt.contourf(xx, yy, z, cmap = plt.cm.Paired, alpha=0.8)
    plt.scatter(x[:,0], x[:,1], c=y.astype(np.float))
    plt.show()
plotPredictions(svc)

# -----Make  a prediction of a person who makes 200000 a year and 40 years old

pred=svc.predict([[200000,40]])
print(pred)