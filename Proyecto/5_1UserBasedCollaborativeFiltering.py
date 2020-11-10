# -----------Recomender systems : dependiendo de lo que se haya visitado comprado o visto se realiza una recomendacion

import pandas as pd
import numpy as np

r_cols = ['user_id','movie_id','rating']
ratings = pd.read_csv('C:/Users/ediso\Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/ml-100k/u.data', sep='\t', names = r_cols, usecols=range(3))

m_cols = ['movie_id','title']
movies = pd.read_csv('C:/Users/ediso\Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/ml-100k/u.item', sep='|', names = m_cols, usecols=range(2), encoding='latin-1')

ratings = pd.merge(movies, ratings)

# print(ratings.head())


movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'], values=['rating'])

movieRatings = pd.DataFrame(movieRatings.rating)
# print(movieRatings)

starWarsRatings = movieRatings['Star Wars (1977)']
# print(starWarsRatings)

corrStars = movieRatings.corrwith(starWarsRatings)
# print(corrStars)
movieRatings=movieRatings.T
# print(movieRatings)
movieRatings['correl']=corrStars
corrStars.dropna(inplace=True)
recomended=movieRatings.sort_values('correl',ascending=False)['correl']
# print(recomended.head(30))


# print(ratings)
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
# print(movieStats.head())

popularMovies = movieStats['rating']['size'] >=100

popularMovies=movieStats[popularMovies].sort_values([('rating','mean')], ascending=False)
popularMovies=pd.DataFrame(popularMovies)
popularMovies['correl']=corrStars
popularMovies=popularMovies.sort_values('correl',ascending=False)[:15]
print(popularMovies)
