from random import *
from copy import *

N = 100
NumeroPermutaciones = 30
vector = range(0, N)


#Crear permutaciones
Permutaciones = []

i = 0
while i < NumeroPermutaciones:
    temp = []
    
    #Desordenar vector
    shuffle(vector)
    temp = copy(vector)
    if temp not in Permutaciones:
        Permutaciones.append(temp)
        i += 1
        temp = []

ContadorPermN = []

for i in xrange(0,N):
    
    temp = []
    for perm in Permutaciones:
        oper = 0
        for p in perm:
            if i != p:
                oper += 1
            else:
                oper += 1
                temp.append(oper)
                break

    ContadorPermN.append(temp)


PromCont = []
for i in xrange(0,N):
    suma = 0
    for perm in xrange(0,len(Permutaciones)):
        #print ContadorPermN[i][perm],
        suma += ContadorPermN[i][perm]
    #print
    PromCont.append(float(suma)/NumeroPermutaciones)

#print PromCont

archivo = open("Permutaciones.csv", 'w')

for perm in xrange(0,len(Permutaciones)):
    a=""
    for i in xrange(0,N):
        if i == N - 1:
            a += str(ContadorPermN[i][perm])
            #print >>archivo, ContadorPermN[i][perm]
        else:
            a += str(ContadorPermN[i][perm]) + ","
            #print >>archivo, "%d" % ContadorPermN[i][perm],
    print >>archivo, a
archivo.close()
