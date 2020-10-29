import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


#  DATA
pageSpeeds=np.random.normal(3.0,1.0,1000)
purchaseAmount=np.random.normal(50.0,10.0,1000)/pageSpeeds
plt.scatter(pageSpeeds,purchaseAmount)
# plt.show()



# REGRESION POLINOMICA
x=np.array(pageSpeeds)
y=np.array(purchaseAmount)

p4=np.poly1d(np.polyfit(x,y,5))

xp= np.linspace(0,7,100)
plt.scatter(x,y)
plt.plot(xp,p4(xp), c='r')
plt.show()


from sklearn.metrics import r2_score

r2=r2_score(y,p4(x))
print(r2)