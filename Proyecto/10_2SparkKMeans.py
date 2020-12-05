from pyspark.mllib.clustering import KMeans
from numpy import array, random
from math import sqrt
from pyspark import SparkConf, SparkContext
from sklearn.preprocessing import scale

K=5

conf= SparkConf().setMaster("local").setAppName("SparkMeans")
sc=SparkContext(conf=conf)

def createClusteredData(N,k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X=[]
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X=array(X)
    return X

data = sc.parallelize(scale(createClusteredData(100,K)))

clusters = KMeans.train(data, K, maxIterations=10, initializationMode="random")

resultRDD=data.map(lambda point: clusters.predict(point)).cache()
print ("Count by value")
counts = resultRDD.countByValue()
print(counts)
print("Cluster assigments:")
results=resultRDD.collect()
print(results)

def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = data.map(lambda point: error(point)).reduce(lambda x, y: x+y)
print("Within Set Sum of Squared Error = " + str(WSSSE))