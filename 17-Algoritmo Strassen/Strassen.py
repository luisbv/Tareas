from random import randint# Hacer el algoritmo de n^3 y n^log pg 744 diapositivasdef Strassen3(A, B):    C = list()    for i in xrange(len(A)):        temp = list()        for j in xrange(len(A)):            temp.append(0)        C.append(temp)    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]    return Cn = 2A = list()B = list()for i in xrange(n):        tempA = list()        tempB = list()        for j in xrange(n):            tempA.append(randint(0,10*n))            tempB.append(randint(0,10*n))        A.append(tempA)        B.append(tempB)print Strassen3(A, B)