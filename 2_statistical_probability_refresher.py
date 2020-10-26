# -------GENERACION DE UNA FUNCION NORMAL DE LA DISTRIBUCION DE SALARIOS -----------

# -------------MEAN------------

import numpy as np
incomes= np.random.normal(27000,15000, 10000)
print(np.mean(incomes))


# --------- GRAFICAR -------------

import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()

print(np.median(incomes))


# ----------- INCLUIR UN OUTLIER--------

incomes=np.append(incomes,[1000000000])



# ------------- MEDIAN---------------------

print(np.median(incomes))   #  SE VERIFICA QUE LA MEDIANA NOCAMBIA MUCHOA PESAR DE QUE SE A;ADIO UN  VALOR EXTREMO

print(np.mean(incomes))

# -----------MODE -----------------

ages =np.random.randint(18, high=90, size=500)
print(ages)

from scipy import stats
print(stats.mode(ages))


# ------------------PRACTICE ------------------
incomes=np.random.normal(100.0,90.0,10000)
plt.hist(incomes, 50)
plt.show()

print(np.mean(incomes))
from scipy import stats
print(stats.mode(incomes))