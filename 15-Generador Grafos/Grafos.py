from random import choice, random, randint
from math import sqrt
from itertools import product
import os

def shell(script):
    ''' lol '''
    os.system("bash -c '%s'" % script)


def Gnp(n = 10, p = 0.5):
    E = list()
    for i in xrange(0,n):
        for j in xrange(i+1,n):
            if random() < p:
                E.append((i,j))
    return E

def Gnm(n = 10, m = 10):
    E = list()
    while len(E) < m:
        i = randint(0,n)
        j = randint(0,n)
        if i != j and (i,j) not in E:
            E.append((i,j))

    return E

def Coordenadas(n=10):
    coord = list()
    while (len(coord) < n):
        x = random()
        y = random()
        if (x, y) not in coord:
            coord.append((x, y))
    return coord



def Euclidiana(v, w):
    (x1,y1) = v
    (x2,y2) = w
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def geom(n=10, r=0.5, complete=True):
    coord = Coordenadas(n)
    raw = list()
    for i in xrange(0,n):
        v = coord[i]
        for j  in xrange(i+1,n):
            w = coord[j]
            d = Euclidiana(v,w)
            if complete or d < r:
                raw.append(((i,j), d))
    E = list()
    for (e, d) in sorted(raw, key = lambda x: -x[1]):
        E.append(e)
    return E, coord

def NotIguales(arreglo):
    val = arreglo[0]
    noIguales = 0
    for i in xrange(1,len(arreglo)):
        if arreglo[i] != val:
            noIguales += 1
    
    if noIguales != 0:
        return True
    else:
        return False

def unionFind(n=10, C=list()):
    nodo = range(0, n)
    E = list()
    while sum(nodo) > 0 and len(C) > 0:
        (i, j) = C.pop(0)
        if i != j and nodo[i] != nodo[j]:
            maximo = max(nodo[i],nodo[j])
            minimo = min(nodo[i],nodo[j])
            for p in xrange(n):
                if nodo[p] == maximo:
                    nodo[p] = minimo
            E.append((i,j))
    return E

        
def Prim(n=10):
    coord = Coordenadas(n)
    d = dict()
    for i in xrange(0,n):
        d[i]=list()
        v = coord[i]
        for j  in xrange(i+1,n):
            w = coord[j]
            d[i].append((j,Euclidiana(v,w)))
        d[i] = sorted(d[i], key = lambda x: x[1])

    E = list()
    m = n-1

    while(len(E) <= m):
        i = randint(0,n-1)
        if len(d[i]) > 0:
            j = d[i][0][0]
        if (i,j) not in E and (j,i) not in E and i != j:
            E.append((i,j))
    return E, coord


def hipergrafo(dim=3):

    hiper = list(product('01',repeat=dim))
    for i in xrange(0,len(hiper)):
        hiper[i] = ''.join(hiper[i])
    return hiper


#si xor >0 pot 2 ex no son potencia:
#xor == 0 es el mismo

def nodosDat(Coord):
    file = open('nodos.dat', 'w')
    for i in xrange(0,len(Coord)):
        print >>file, '%d %.5f %.5f' % (i, Coord[i][0], Coord[i][1])
    file.close()

def aristasDat(E, Coord):
    file = open('aristas.dat', 'w')
    for i in xrange(0,len(E)):
        x1 = Coord[E[i][0]][0]
        y1 = Coord[E[i][0]][1]
        x2 = Coord[E[i][1]][0]
        y2 = Coord[E[i][1]][1]
        dx = (x2 - x1)
        dy = (y2 - y1)
        print >>file, '%.5f %.5f %.5f %.5f' % (x1, y1, dx, dy)
    file.close()

def NodosAdyacentes(E,Coord):
    Ady = list()
    for i in xrange(len(Coord)):
        temp=list()
        for arista in E:
            if arista[0] == i:
                temp.append(arista[1])
            elif arista[1] == i:
                temp.append(arista[0])
            else:
                continue
        Ady.append(temp)
    return Ady

def acomodarNodos(E, Coord):
    #nodos que tienen aristas en comun tienden a estar 
    #cerca y nodos que no tienen arista en comun lejos
    #distancia de vecino y distancia de no vecino
    #si me encuentro cerca de la distancia repelo
    #hacer como suma de fuerzas
    #alfa F alfa entre 0 y 1

    n = 20 # distancia de no adyacencia
    v = 10 # distancia de adyacencia

    nodosAdyacentes = NodosAdyacentes(E,Coord)

    epsilon = 1
    stop = True
    iter = 0
    maxiter = 500
    while stop:
        iter += 1
        i = 0
        error = 0
        while i < len(Coord):
            dv = 0
            dn = 0
            xv = 0
            yv = 0
            xn = 0
            yn = 0
            for j in nodosAdyacentes[i]:
                d = Euclidiana(Coord[i],Coord[j]) #distancia entre nodos
                xv += Coord[j][0] - Coord[i][0]
                yv += Coord[j][1] - Coord[i][1]
                error += abs(d-v)
                if d > v:
                    dv -= d - v
        
            temp = list()
            for j in xrange(len(Coord)):
                if j not in nodosAdyacentes[i]:
                    temp.append(j)

            for j in temp:
                d = Euclidiana(Coord[i],Coord[j]) #distancia entre nodos
                xn += Coord[j][0] - Coord[i][0]
                yn += Coord[j][1] - Coord[i][1]
                if d < n:
                    dn += n - d

        
            alfax = random() * float(yv - yn)/(xv - xn)
            alfay = random() * float(yv - yn)/(xv - xn)
            x = Coord[i][0] + alfax
            y = Coord[i][1] + alfay
            Coord[i] = (x,y)
        
            i += 1
        if error <= epsilon or iter == maxiter:
            stop = False
        

    return Coord
#vector
#x y dx dy
#head flechas
#no head puras lineas

# print "Gnp"
# print Gnp()
# 
# print
# print
# print "Gnm"
# print Gnm()
# 
# print
# print
# print "geom"
# C,a = geom()
# print C
# 
# 
# print 
# print
# print "unionFind"
# print unionFind(len(C),C)
# 
# 
# print
# print
# 
# print "PRIM"
# print Prim()
# 
# print
# print
# print hipergrafo()
nodos = 10
aristas, Coord = Gnp(nodos), Coordenadas(nodos)

nodosDat(Coord)
aristasDat(aristas, Coord)

#Desacomodados
print Coord
shell('gnuplot plotDes.gnu')

#Acomodados
Coord = acomodarNodos(aristas, Coord)
print Coord
nodosDat(Coord)
aristasDat(aristas, Coord)
shell('gnuplot plotO.gnu')

shell('open GraficaDes.eps')
shell('open GraficaO.eps')