import pandas as pd


# ------------ lectura de datos -------------------
r_cols = ['user_id','movie_id','rating']
ratings = pd.read_csv('C:/Users/ediso\Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/ml-100k/u.data', sep='\t', names=r_cols,usecols=range(3))

m_cols = ['movie_id','title']
movies = pd.read_csv('C:/Users/ediso\Desktop/Python Projects/Data Science/Curso DataScience/DataScience-Python3-Resources/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding='latin-1')

print(ratings.head())
print(movies.head())

# ------------------ merge data --------------------

ratings = pd.merge(movies,ratings)

print(ratings.head())

# --------------------table merged and ordered ---------------------------------

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(userRatings.head())

# ------------ encontrar la correlacion ---------------------------

corrMatrix = userRatings.corr()
print(corrMatrix.head())

# -------------- encontrar la correlacion de las peliculas que han sido evaluadas mas de 100 veces
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
print(corrMatrix.head())

# ----- crear una persona para crear recomendaciones para esa persona
myRatings = userRatings.loc[0].dropna()
print(myRatings)

# ---- buscar las peliculas que se adecuen al perfil -------
simCandidates = pd.Series()
for i in range(0,len(myRatings.index)):
    print('Adding sims for ' + myRatings.index[i]+ "...")
    sims= corrMatrix[myRatings.index[i]].dropna()
    sims = sims.map(lambda x: x* myRatings[i])
    simCandidates = simCandidates.append(sims)

print('sorting...')
simCandidates.sort_values(inplace=True,ascending=False)
print(simCandidates.head(10))

# ----- agrupar peliculas repetidas ----------
simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace=True, ascending=False)
print(simCandidates.head(10))

# ---- drop movies already seen----------

filteredSims = simCandidates.drop(myRatings.index)
print(filteredSims.head(10))

