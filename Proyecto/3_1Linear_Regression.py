#  1 Least Square
#  2. Gradient Descenden

# 1. Linear Regression


import numpy as np
import matplotlib.pyplot as plt

# DATA
pageSpeeds=np.random.normal(3.0,1.0,1000)
purchaseAmount = 100 - (pageSpeeds+np.random.normal(0,0.1,1000)) * 3
plt.scatter(pageSpeeds,purchaseAmount)
# plt.show()


# REGRESSION
from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds,purchaseAmount)

print('R^2 = ',r_value**2)


def predict(x):
    return slope*x+intercept

fitLine=predict(pageSpeeds)

plt.scatter(pageSpeeds,purchaseAmount)
plt.plot(pageSpeeds,fitLine, c='r')
plt.show()