from random import choice, random, randint
from math import sqrt
from itertools import product

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
    return E


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



#vector
#x y dx dy
#head flechas
#no head puras lineas

print "Gnp"
print Gnp()

print
print
print "Gnm"
print Gnm()

print
print
print "geom"
C,a = geom()
print C


print 
print
print "unionFind"

print unionFind(len(C),C)


print
print

print "PRIM"
print Prim()

print
print
print hipergrafo()

nodos, Coord = geom()
nodosDat(Coord)
aristasDat(nodos, Coord)


