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
print('')
print('-----------------Lists = se puede variar los elemntos----------------')
x=[1,2,3,4,5,6]
print(len(x))

print(x[:3])
print(x[3:])
print(x[-2:])
x.extend([7,8])
x.append(9)
print(x)
y=[10,11,12]
listoflists=[x,y]
print(listoflists)
print(y[1])
z=[3,2,1]
z.sort()
print(z)

# /////TUPLES///////
print('')
print('-----------------Tuples = no son variables----------------')
x=(1,2,3)
print(len(x))
y=(4,5,6)
print(y[1])
listoftuples=[x,y]
print(listoftuples)
(age,income)='32,12000'.split(',')
print(age)
print(income)


# /////DICTIONARIES///////
print('')
print('-----------------Disctionaries = son variables----------------')
captains={}
captains['Enterprise']='Kirk'
captains['Enterprise D']='Picard'
captains['Deep Space Nine']='Sisko'
captains['Voyager']='Janeway'

print(captains['Voyager'][0])
print(captains)
print(captains.get('Enterprise'))

for ship in captains:
    print(ship + ':' + captains[ship] )




# ////FUNCTIONS /////////////

print('')
print('-----------------Functions----------------')
def squareIt(x):
    return x*x
print(squareIt(9))

def DoSomething(f,x):
    return f(x)
print(DoSomething(squareIt,2))


print(DoSomething(lambda x:x*x*x,3))




# ////FUNCTIONS /////////////

print('')
print('-----------------Boolean Expression----------------')

print(1==3)
print (True or False)
print (1 is 3)

if 1 is 3:
    print("hoe did that happen")
elif 1>3:
    print('yikes')
elif 1<3:
    print('All is well with the world')

# //// LOOPING /////////////

print('')
print('----------------- Looping ----------------')
for x in range(10):
    print (x)

print('')

for x in range(10):
    if x==1:
        continue
    if x>5:
        break
    print (x)

print('')

x=0
while (x<10):
    print(x)
    x+=1 

# //// LOOPING /////////////

print('')
print('----------------- Activity ----------------')
for x in range(10):
    if x%2 > 0:
        continue
    else:
        print(x)


listofnumbers=[1,2,3,4,5,6]

for number in listofnumbers:
    if (number%2==0):
        print(number, 'is even')
    else:
        print(number, 'is odd')
print('horray!')