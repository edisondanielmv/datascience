# -------GENERACION DE UNA FUNCION NORMAL DE LA DISTRIBUCION DE SALARIOS -----------

import numpy as np
incomes= np.random.normal(27000,15000, 10000)
print(np.mean(incomes))


# --------- GRAFICAR -------------

import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()

print(np.median(incomes))


# ----------- INCLUIR UN OUTLIER--------

incomes=np.append(incomes,[100000000])

print(np.median(incomes))   #  SE VERIFICA QUE LA MEDIANA NOCAMBIA MUCHOA PESAR DE QUE SE A;ADIO UN  VALOR EXTREMO

