from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

conf = SparkConf().setMaster("local").setAppName("SparkTFIDF")
sc=SparkContext(conf=conf)

rawData=sc.textFile("C:/Users/ediso/Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/subset-small.tsv")
fields = rawData.map(lambda x:x.split("\t"))
documents = fields.map(lambda x:x[3].split(" "))

documentNames = fields.map(lambda x:x[1])

hashingTF = HashingTF(100000)
tf=hashingTF.transform(documents)

tf.cache()
idf = IDF(minDocFreq=2).fit(tf)
tfidf = idf.transform(tf)


gettysburgTF = HashingTF.transform(["Gettysburg"])
gettysburgHashValue = int(gettysburgTF.indices[0])

gettysburgRelevance = tfidf.map(lambda x: x[gettysburgHashValue])

zippedResults = gettysburgRelevance.zip(documentNames)

print("Best document for gettysburg is: ")
print(zippedResults.max())