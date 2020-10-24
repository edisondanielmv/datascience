# -------COMO USAR IF STATEMENT -----------------------------------------------------

# listOfNumbers = [1,2,3,4,5,6]
# for number in listOfNumbers:
#     if(number %2 == 0):
#         print (number,'is even')
#     else:
#         print (number,'is odd')
# print("All Done")

# -------HACER UNA FUNCION NORMAL RANDOM Y GRAFICARLE-------------------------------------------------------

# import numpy as np
# A=np.random.normal(100.0,30.0,10000)
# print(A)
# print(type(A))
# list1=A.tolist()
# print(list1)

# import matplotlib.pyplot as plt
# plt.hist(list1, bins=30, cumulative=False, density=True)
# plt.ylabel('Numero')
# plt.xlabel('Funcion Normal Random')
# plt.show()

# ------ESTRUCTURA DE DATOS  ------------------------
# ////LISTA////
x=[1,2,3,4,5,6,7]
print(len(x))

print(x[:3])
print(x[3:])
print(x[-2:])
print(x.extend([8,9]))