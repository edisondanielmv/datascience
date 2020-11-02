import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
import pandas as pd

np.random.seed(2)
pageSpeeds=np.random.normal(3.0,1.0,100)
purchaseAmount =np.random.normal(50.0,30.0,100)/pageSpeeds

# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()

trainx = pageSpeeds[:80]
testx=pageSpeeds[80:]

trainy=purchaseAmount[:80]
testy=purchaseAmount[80:]

# plot test data

# plt.scatter(testx,testy)
# plt.show()


# plot train data

# plt.scatter(trainx,trainy)
# plt.show()



# -------------------- Plot Train Data --------------------

x=np.array(trainx)
y=np.array(trainy)
plt.scatter(x,y)

p4=np.poly1d(np.polyfit(x,y,8))
xp=np.linspace(0,7,100)
axes=plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([-100,200])
plt.plot(xp,p4(xp),c='r')

plt.show()

r2train=r2_score(trainy, p4(trainx))
print(r2train)


# --------------------- PlotTest Data ----------------------

x=np.array(testx)
y=np.array(testy)
plt.scatter(x,y)

p4=np.poly1d(np.polyfit(x,y,8))
xp=np.linspace(0,7,100)
axes=plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([-100,200])
plt.plot(xp,p4(xp),c='r')

plt.show()

r2test=r2_score(testy,p4(testx))
print(r2test)