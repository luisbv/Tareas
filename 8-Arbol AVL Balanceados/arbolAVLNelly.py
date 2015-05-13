#!/bin/python
#coding:utf-8
import random

class Nodo :
        def __init__(self, dato, izq=None, der=None):
                self.dato = dato
                self.altura = 0
                self.izq = izq
                self.der = der

def altura(nodo): 
        if(nodo):
                return nodo.altura
        else:
                return -1  #si es vacio tendra una altura negativa, cuando es hoja tendra valor de cero 

def actualizarAltura(nodo):
        if (not nodo): return
        nodo.altura = max(altura(nodo.izq), altura(nodo.der)) + 1

def rotarS(nodo, a_izq): #rotaciones y actualizacion de las alturas
        #Rotar simple
        n2 = None
        if (a_izq):#rotacion izquierda si (izq==True)
                n2 = nodo.izq
                nodo.izq = n2.der
                n2.der = nodo
        else:#rotacion derecha, si (izq==False)
                n2 = nodo.der #guardo el subarbol con mayor altura, ahora sera el padre
                nodo.der = n2.izq #el hijo izq del subarbol desbalanceado sera ahora hijo derecho del anterior padre
                n2.izq = nodo #nodo izq sdel padre es ahora hijo 
        actualizarAltura(nodo) #nodo que se ha vuelto hijo 
        actualizarAltura(n2) #nodo que se ha vuelto padre
        return n2 #regreso nodo rotado

def rotarD(nodo, a_izq):
        if(a_izq):
                nodo.izq = rotarS(nodo.izq, False)
                nodo = rotarS(nodo, True)
        else:
                nodo.der = rotarS(nodo.der, True)
                nodo = rotarS(nodo, False)
        #la actualización de las alturas se realiza en las rotaciones simples
        return nodo
        
def balancear(nodo):
        #print nodo
        if (not nodo): return
        print "Dato",nodo.dato
        if altura(nodo.izq) - altura(nodo.der) == 2:
                print "desequilibrio hacia la izquierda"
                #desequilibrio hacia la izquierda
                if altura(nodo.izq.izq) >= altura(nodo.izq.der):
                        print "desequilibrio simple a la izq"
                        #desequilibrio simple a la izq
                        
                        nodo = rotarS(nodo, True)
                else:
                        print "desequilibrio doble a la izquierda"
                        #desequilibrio doble a la izquierda
                        nodo = rotarD(nodo, True)
        elif altura(nodo.der) - altura(nodo.izq) == 2:
                #desequilibrio hacia la derecha
                print "desequilibrio hacia la derecha"
                if altura(nodo.der.der) >= altura(nodo.der.izq): 
                        print "desequilibrio simple hacia la derecha"
                        #desequilibrio simple hacia la derecha
                        nodo = rotarS(nodo, False)
                else:
                        print "desequilibrio doble hacia la derecha"
                        #desequilibrio doble hacia la derecha
                        nodo = rotarD(nodo, False)
        return nodo

def insertar(nodo, dato):
        if (not nodo) :
                nodo = Nodo(dato, None, None)
        else:
                if (dato < nodo.dato):
                        nodo.izq = insertar(nodo.izq, dato)
                else:
                        nodo.der = insertar(nodo.der, dato)
                nodo = balancear(nodo)
                actualizarAltura(nodo)
        return nodo

space = 5

def lvlnode(nodo, dlvl, lvl =0):
        if (lvl == dlvl): 
                return [nodo]#Si no es nodo regresara None
        #regresara vacio si no es el nivel que estoy buscando 
        if (lvl < dlvl):
                nodes = []
                izq = nodo and nodo.izq #agrega un None cuando el nodo no exise y hay otro nivel 
                der = nodo and nodo.der
                nodes += lvlnode(izq, dlvl, lvl+1)
                nodes += lvlnode(der, dlvl, lvl+1)
                return nodes 

def mostrar(raiz):
        p = sys.stdout.write
        width = (2**(raiz.altura))*space
        for i in range(raiz.altura+1):
                cnodes = 2**i
                spaces = (width/cnodes)
                for n in lvlnode(raiz, i):
                        t = str(n and n.dato or "")#returns "" if n is None
                        tspaces = (spaces -len(t))/2
                        p(" " *tspaces)
                        p(t)
                        p(" " *tspaces)
                p("\n")
                


raiz = None
import sys
def sins(dato): #insertar dato 
        global raiz
        raiz = insertar(raiz, dato)
        
#for i in xrange(12):
#        sins(random.randint(5,1000))

valores = [10,52,94,45,40,14,11,41,48]
for i in xrange(len(valores)):
    if i != 0:
        print "A %d" % valores[i]
    sins(valores[i])
    if i != 0:
        mostrar(raiz)


