from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from numpy import array

conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
sc=SparkContext(conf=conf)

def binary(YN):
    if (YN == 'Y'):
        return 1
    else:
        return 0

def mapEducation(degree):
    if(degree =='BS'):
        return 1
    elif (degree == 'MS'):
        return 2
    elif (degree == 'PhD'):
        return 3
    else:
        return 0

def createLabelPoints (fields):
    yearsExperience = int(fields[0])
    employed = binary(fields[1])
    previousEmployers = binary (fields[2])
    educationLevel = mapEducation(fields[3])
    interned =binary(fields[4])
    topTier = binary(fields[5])
    hired = binary(fields[6])
    return LabeledPoint(hired, array([yearsExperience, employed, previousEmployers, educationLevel, topTier, interned]))

rawData = sc.textFile("C:/Users/ediso/Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/PastHires.csv")
header = rawData.first()
rawData = rawData.filter(lambda x: x !=header)

cvsData = rawData.map(lambda x: x.split(","))

trainingData = cvsData.map(createLabelPoints)

testCandidates = [array([10,1,3,1,0,0])]
testData = sc.parallelize(testCandidates)

model = DecisionTree.trainClassifier(trainingData,numClasses=2,categoricalFeaturesInfo={1:2, 3:4, 4:2, 5:2},impurity='gini',maxDepth=5,maxBins=32)


predictions = model.predict(testData)
print('Hire Prediction')
results = predictions.collect()
for result in results:
    print(result)

print('Learned classification tree model:')
print(model.toDebugString())