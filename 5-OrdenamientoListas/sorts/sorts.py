from random import shuffle
maximo = 200

def selsort(lista):
    global maximo
    for i in xrange(0, len(lista)):
        k = None
        menor = maximo + 1
        for p in xrange(i, len(lista)):
            if lista[p] < menor:
                k = p
                menor = lista[p]
        if k is not None:
            (lista[i], lista[k]) = (lista[k], lista[i])
    return

def mergesort(lista):
    if len(lista) < 2:
        return lista
    else:
        mitad = len(lista) / 2
        primero = mergesort(lista[0:mitad])
        segundo = mergesort(lista[mitad:len(lista)])
        nueva = list()
        while len(primero) > 0 or len(segundo) > 0:
            if len(primero) == 0:
                return nueva + segundo
            elif len(segundo) == 0:
                return nueva + primero
            elif primero[0] < segundo[0]:
                nueva.append(primero.pop(0))
            else:
                nueva.append(segundo.pop(0))
        return nueva

def indexquicksort(lista, desde, hasta):
    if hasta == desde:
        return
    d = desde
    h = hasta
    pivote = lista[d] # hay que congelar esto por ahora
    desde += 1
    while desde < hasta:
        while desde < hasta and not lista[desde] >= pivote:
            desde += 1
        while desde < hasta and not lista[hasta] < pivote:
            hasta -= 1
        if desde < hasta:
            (lista[desde], lista[hasta]) = (lista[hasta], lista[desde])
    if lista[h] < pivote:
        (lista[d], lista[h]) = (lista[h], lista[d]) # si pivote es el maximo (caso especial)
    indexquicksort(lista, d, desde - 1)
    indexquicksort(lista, hasta, h)
    return

def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivote = lista[0]
        primero = list()
        segundo = list()
        for elemento in lista[1:]:
            if elemento <= pivote:
                primero.append(elemento)
            else:
                segundo.append(elemento)
        if len(primero) == 0:
            primero.append(pivote)
        elif len(segundo) == 0:
            segundo.append(pivote)
        else:
            primero.append(pivote)            
        primero = quicksort(primero)
        segundo = quicksort(segundo)
        return primero + segundo

lista = range(1, maximo)
print "ord", lista
shuffle(lista)
print "mix", lista
selsort(lista)
print "ord", lista
shuffle(lista)
print "mix", lista
print "ord", mergesort(lista)
shuffle(lista)
print "mix", lista
print "ord", quicksort(lista)
shuffle(lista)
print "mix", lista
indexquicksort(lista, 0, len(lista) - 1)
print "ord", lista
