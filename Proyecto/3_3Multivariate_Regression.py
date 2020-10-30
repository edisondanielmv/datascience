import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

df=pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
print(df.head())

import statsmodels.api as sm

df['Model_ord']=pd.Categorical(df.Model).codes #convierte categorias a numeros
x=df[['Mileage','Model_ord','Doors']]
y=df[['Price']]

x1=sm.add_constant(x)
est=sm.OLS(y,x1).fit()

print(est.summary())
print(y.groupby(df.Doors).mean())