from random import randint# Hacer el algoritmo de n^3 y n^log pg 744 diapositivasdef mult(A,B, n):    C = list()    for i in xrange(n):        temp = list()        for j in xrange(n):            temp.append(0)        C.append(temp)    for i in xrange(n):        for k in xrange(n):            for j in xrange(n):                C[i][j] += A[i][k] * B[k][j]    return Cdef suma(A, B, n):    C = list()    for i in xrange(n):        temp = list()        for j in xrange(n):            temp.append(A[i][j]+B[i][j])        C.append(temp)    return Cdef resta(A, B, n):    C = list()    for i in xrange(n):        temp = list()        for j in xrange(n):            temp.append(A[i][j]-B[i][j])        C.append(temp)    return Cdef zeros(n):    A = list()    for i in xrange(n):        temp = list()        for j in xrange(n):            temp.append(0)        A.append(temp)    return Adef Strassen3(A, B, n):    if n == 1:        return mult(A,B,n)    else:                m = n/2        A11, A12, A21, A22 = zeros(m), zeros(m), zeros(m), zeros(m)        B11, B12, B21, B22 = zeros(m), zeros(m), zeros(m), zeros(m)        for i in xrange(m):            for j in xrange(m):                A11[i][j] = A[i][j]                A12[i][j] = A[i][j+m]                A21[i][j] = A[i+m][j]                 A22[i][j] = A[i+m][j+m]                B11[i][j] = B[i][j]                B12[i][j] = B[i][j+m]                B21[i][j] = B[i+m][j]                 B22[i][j] = B[i+m][j+m]        X1 = Strassen3(A11, B11, m)        X2 = Strassen3(A12, B21, m)        X3 = Strassen3(A11, B12, m)        X4 = Strassen3(A12, B22, m)        X5 = Strassen3(A21, B11, m)        X6 = Strassen3(A22, B21, m)        X7 = Strassen3(A21, B12, m)        X8 = Strassen3(A22, B22, m)                C11 = suma(X1, X2, m)        C12 = suma(X3, X4, m)        C21 = suma(X5, X6, m)        C22 = suma(X7, X8, m)                C = zeros(n)            for i in xrange(m):            for j in xrange(m):                C[i][j] = C11[i][j]                C[i][j+m] = C12[i][j]                C[i+m][j] = C21[i][j]                C[i+m][j+m] = C22[i][j]                        return Cdef Strassen(A, B, n):    if n == 1:        return mult(A,B,n)    else:        m = n/2        A11, A12, A21, A22 = zeros(m), zeros(m), zeros(m), zeros(m)        B11, B12, B21, B22 = zeros(m), zeros(m), zeros(m), zeros(m)        for i in xrange(m):            for j in xrange(m):                A11[i][j] = A[i][j]                A12[i][j] = A[i][j+m]                A21[i][j] = A[i+m][j]                 A22[i][j] = A[i+m][j+m]                B11[i][j] = B[i][j]                B12[i][j] = B[i][j+m]                B21[i][j] = B[i+m][j]                 B22[i][j] = B[i+m][j+m]        S1 = Strassen(resta(A12,A22,m),suma(B21,B22,m),m) #(A12 - A22) * (B21 + B22)        S2 = Strassen(suma(A11,A22,m),suma(B11,B22,m),m) #(A11 + A22) * (B11 + B22)        S3 = Strassen(resta(A11,A21,m), suma(B11, B12, m), m) #(A11 - A21) * (B11 + B12)        S4 = Strassen(suma(A11,A12,m), B22, m) #(A11 + A12) * B22        S5 = Strassen(A11 , resta(B12,B22,m),m) #A11 * (B12 - B22)        S6 = Strassen(A22, resta(B21, B11, m),m) #A22 * (B21 - B11)        S7 = Strassen(suma(A21, A22, m), B11,m) #(A21 + A22) * B11        C11 = suma(suma(S1, resta(S2, S4, m),m),S6,m) #S1 + S2 - S4 + S6        C12 = suma(S4, S5, m) #S4 + S5        C21 = suma(S6, S7, m) #S6 + S7        C22 = suma(resta(S2, S3,m),resta(S5, S7, m),m) #S2 - S3 + S5 - S7        C = zeros(n)            for i in xrange(m):            for j in xrange(m):                C[i][j] = C11[i][j]                C[i][j+m] = C12[i][j]                C[i+m][j] = C21[i][j]                C[i+m][j+m] = C22[i][j]                        return Cn = 4A = list()B = list()for i in xrange(n):        tempA = list()        tempB = list()        for j in xrange(n):            tempA.append(randint(0,10*n))            tempB.append(randint(0,10*n))        A.append(tempA)        B.append(tempB)print "A", Aprint "B", Bprint Strassen3(A, B, n)print Strassen(A, B, n)