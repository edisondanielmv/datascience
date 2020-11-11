import pandas as pd
import numpy as np

r_cols = ['userr_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/ediso\Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))
print(ratings.head())
movieProperties = ratings.groupby('movie_id').agg({'rating':[np.size,np.mean]})
print(movieProperties.head())

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
print(movieNormalizedNumRatings.head())

movieDict = {}
with open(r'C:/Users/ediso\Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/ml-100k/u.item', encoding = "ISO-8859-1") as f:
    temp=''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name=fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        # movieDict[movieID] = (name, genres, movieNormalizedNumRatings.loc[movieID].get('size'),movieProperties.loc[movieID].rating.get('mean'))
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))
print(movieDict[1])


from scipy import spatial

def ComputeDistance(a,b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA -popularityB)
    return genreDistance + popularityDistance

print(ComputeDistance(movieDict[2], movieDict[4]))
print(movieDict[2])
print(movieDict[4])

import operator

def getNeighbors(movieID, k):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie,dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range (k):
        neighbors.append(distances[x][0])
    return neighbors

k=10
avgRating = 0
neighbors = getNeighbors(1,k)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print ( movieDict [neighbor][0] + " " + str(movieDict[neighbor][3]))

avgRating /= float(k)

print(avgRating)