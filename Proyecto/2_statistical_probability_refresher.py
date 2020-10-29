# # -------GENERACION DE UNA FUNCION NORMAL DE LA DISTRIBUCION DE SALARIOS -----------

# # -------------MEAN------------

# import numpy as np
# incomes= np.random.normal(27000,15000, 10000)
# print(np.mean(incomes))


# # --------- GRAFICAR -------------

# import matplotlib.pyplot as plt
# plt.hist(incomes, 50)
# # plt.show()

# print(np.median(incomes))


# # ----------- INCLUIR UN OUTLIER--------

# incomes=np.append(incomes,[1000000000])



# # ------------- MEDIAN---------------------

# print(np.median(incomes))   #  SE VERIFICA QUE LA MEDIANA NOCAMBIA MUCHOA PESAR DE QUE SE A;ADIO UN  VALOR EXTREMO

# print(np.mean(incomes))

# # -----------MODE -----------------

# ages =np.random.randint(18, high=90, size=500)
# print(ages)

# from scipy import stats
# print(stats.mode(ages))


# # ------------------PRACTICE ------------------
# incomes=np.random.normal(100.0,90.0,10000)
# plt.hist(incomes, 50)
# # plt.show()

# print(np.mean(incomes))
# from scipy import stats
# print(stats.mode(incomes))

# # ----------------- VARIANCE AND STANDARD DEVIATION -------------------
# incomes=np.random.normal(100.0,20.0,10000)
# plt.hist(incomes,50)
# plt.show()

# print(incomes.std())
# print(incomes.var())

# # --------------------PROBABILITY DENSITY FUNCTIONS -------------
# # 1. NORMAL ()
# # 2. PROBABILITY MASS FUNCTION (HISTOGRAM)


# # -------------------- DISTRIBUTIONS ------------------------

# # 1. UNIFORM DISTRIBUTION
# import numpy as np
# import matplotlib.pyplot as plt
# values = np.random.uniform(-10.0,10.0,100000)
# plt.hist(values,50)
# plt.show()

# # 2. NORMAL / GAUSSIAN
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# first_value=-3
# last_value = 3
# increment=0.001
# x=np.arange(first_value, last_value, increment)
# y=norm.pdf(x)
# plt.plot(x,y )
# plt.show()


# mu_mean=5.0
# sigma=2.0
# quantity_of_values=10000
# funcion_normal=np.random.normal(mu_mean,sigma,quantity_of_values)

# divisiones=50
# plt.hist(funcion_normal,divisiones)
# plt.show()


# # # 3. EXPONENTIAL
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import expon

# first_value_in_x=-0
# last_value_in_x= 10
# increment=0.001
# eje_x=np.arange(first_value_in_x, last_value_in_x, increment)
# eje_y=expon.pdf(eje_x)
# plt.plot(eje_x,eje_y )
# plt.show()

# # 4. BINOMIAL
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import binom

# n,p=10,0.5
# eje_x2=np.arange(0,10,0.001)
# eje_y2=binom.pmf(eje_x2,n,p)
# plt.plot(eje_x2,eje_y2)
# plt.show()

# # POISSON PROBABILITY MASS FUNCTION
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import poisson
# mu=500
# first_value_in_x=400
# last_value_in_x= 600
# increment=0.5
# eje_x=np.arange(first_value_in_x, last_value_in_x, increment)
# eje_y=poisson.pmf(eje_x,mu)
# plt.plot(eje_x,eje_y)
# plt.show()

# #---------------- PERCENTILES -------------------
# import numpy as np
# import matplotlib.pyplot as plt

# ejex=np.random.normal(0,0.5,10000)

# numero_divisiones=50

# plt.hist(ejex,numero_divisiones)
# plt.show()

# percentile_50=np.percentile(ejex,50)
# print(percentile_50)

# percentile_90=np.percentile(ejex,90)
# print(percentile_90)

# percentile_20=np.percentile(ejex,20)
# print(percentile_20)

# #------------------MOMENTS ----------------------
#  first moment is e mean
#  second moment is the ariance
#  third moment is the skew (cuan desviado de el centro esta)
#  and fourth moment kurtosis (cuan alto y delgado es el pico de la curva)

# import numpy as np
# import matplotlib.pyplot as plt

# ejex=np.random.normal(0,0.5,10000)

# numero_divisiones=50

# plt.hist(ejex,numero_divisiones)
# plt.show()

# mean=np.mean(ejex)
# print(mean)
# var=np.var(ejex)
# print(var)


# import scipy.stats as sp
# skew=sp.skew(ejex)
# print(skew)

# kurtosis=sp.kurtosis(ejex)
# print(kurtosis)



# #------------------------ MATPLOTLIB ------------------------------

# from scipy.stats import norm
# import matplotlib.pyplot as plt
# import numpy as np

# x=np.arange(-3,3,0.01)
# plt.plot(x,norm.pdf(x))
# plt.plot(x,norm.pdf(x,1.0,0.5))

# plt.show()






#  # SAVE TO A FILE



from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# x=np.arange(-3,3,0.01)
# plt.plot(x,norm.pdf(x))
# plt.plot(x,norm.pdf(x,1.0,0.5))
# plt.savefig('c:\\Users\\Ediso\\Desktop\\1.png', format='png')


# ADJUST THE AXIS, grid , colors, labels
# axes=plt.axes()
# axes.set_xlim([-5,5])
# axes.set_ylim([0,1.0])
# axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
# axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
# axes.grid()
# plt.xlabel('Greenbles') # labels
# plt.ylabel('Probability') # labels
# plt.plot(x,norm.pdf(x), 'b-') # colors
# plt.plot(x,norm.pdf(x,1.0,0.5), 'r--') # colors
# plt.legend(['Sneetches','Gacks'], loc=4) # labels
# plt.show()


# # --------XKCD MODE ..................

# plt.xkcd()

# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.xticks([])
# plt.yticks([])
# ax.set_ylim([-30,10])

# data=np.ones(100)
# data[70:]-=np.arange(30)

# plt.annotate(
#     'the day i realized',
#     xy=(70,1), arrowprops=dict(arrowstyle='->'),xytext=(15,-10))

# plt.plot(data)
# plt.xlabel('time')
# plt.ylabel('my overal health')
# plt.show()

# # remove XKCD mode
# plt.rodedefaults()


# # ----------------------- PIE CHART --------------------


# values=[12, 55, 4, 32, 14]
# colors=['r','g', 'b', 'c', 'm']
# explode = [0,0,0.2,0,0]
# labels=['India','United States','Russia','China','Europe']
# plt.pie(values,colors=colors,labels=labels,explode=explode)
# plt.title('Studen Locations')
# plt.show()


# # -------------------------BAR CHART -------------------
# values=[12,55,4,32,14]
# colors=['z','g','b','c','m']
# plt.bar(range(0,5),values)
# plt.show()

# # ----------------------- SCATTER PLOT ---------------------

# x=np.random.randn(500)
# y=np.random.randn(500)
# plt.scatter(x,y)
# plt.show()

# # ---------------------- HISTOGRAM --------------------------
# income=np.random.normal(27000, 15000, 10000)
# plt.hist(income,50)
# plt.show()

# --------------------- BOX AND WHISKER PLOT -----------------

# uniformSkewed=np.random.rand(100)*100-40
# high_outliers=np.random.rand(10)*50+100
# low_outliers = np.random.rand(10)*-50-100
# data=np.concatenate((uniformSkewed,high_outliers,low_outliers))
# plt.boxplot(data)
# plt.show()


# # -----------------------------------------------------------------------------------------------------------
# # --------------------------------------------VARIANCE / COVARIANCE -----------------------------------------
# # -----------------------------------------------------------------------------------------------------------

# # -------- COVARIANCE --------------------------

# def de_mean(x):
#     xmean=np.mean(x)
#     return[xi - xmean for xi in x]

# def covariance(x,y):
#     n=len(x)
#     return np.dot(de_mean(x), de_mean(y)) / (n-1)

# pageSpeeds=np.random.normal(3.0,1.0,1000)
# purchaseAmount = np.random.normal(50.0,10.0,1000)

# plt.scatter(pageSpeeds,purchaseAmount)
# plt.show()
# print(covariance(pageSpeeds,purchaseAmount))


# purchaseAmount=np.random.normal(50.0,10.0,1000)/pageSpeeds
# plt.scatter(pageSpeeds,purchaseAmount)

# print(covariance(pageSpeeds,purchaseAmount))
# print(np.corrcoef(pageSpeeds,purchaseAmount))
# plt.show()

# # --------------------------------CONDITIONAL PROBABILITY --------------------------------------
# import numpy as np
# np.random.seed(0)

# totals={20:0,30:0,40:0,50:0,60:0,70:0}
# purchases={20:0,30:0,40:0,50:0,60:0,70:0}
# totalPurchases=0
# for _ in range(100000):
#     ageDecade=np.random.choice([20,30,40,50,60,70])
#     purchaseProbability=float(ageDecade)/100
#     totals[ageDecade] +=1
#     if (np.random.rand()<purchaseProbability):
#         totalPurchases+=1
#         purchases[ageDecade]+=1

# print(totals)
# print(purchases)



# PEF=float(purchases[30])/float(totals[30])
# print('Probabilidad de comprar si se tiene 30 anos >> P(purchases | 30): ', PEF)

# PF=float(totals[30])/100000
# print('Probabilidad de tener 30 anos >> P(F): ', PF)

# PE=float(totalPurchases)/100000
# print('Probabilidad de comprar algo >> P(PE): ', PE)

# import numpy as np
# np.random.seed(0)

# totals={20:0,30:0,40:0,50:0,60:0,70:0}
# purchases={20:0,30:0,40:0,50:0,60:0,70:0}
# totalPurchases=0
# for _ in range(100000):
#     ageDecade=np.random.choice([20,30,40,50,60,70])
#     ran1=np.random.random()
#     purchaseProbability=float(ran1)
#     totals[ageDecade] +=1
#     if (np.random.rand()<purchaseProbability):
#         totalPurchases+=1
#         purchases[ageDecade]+=1

# print(totals)
# print(purchases)



# PEF=float(purchases[30])/float(totals[30])
# print('Probabilidad de comprar si se tiene 30 anos >> P(purchases | 30): ', PEF)

# PF=float(totals[30])/100000
# print('Probabilidad de tener 30 anos >> P(F): ', PF)

# PE=float(totalPurchases)/100000
# print('Probabilidad de comprar algo >> P(PE): ', PE)


# ------------------------BAYES' THEOREM -------------------------------

