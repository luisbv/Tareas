from random import randint, choice, random

class nodo:
    def __init__(self, valor, p = None):
        self.valor = valor
        self.altura = 0
        self.padre = p
        if self.padre is None:
            self.prof = 0
        else:
            self.prof = self.padre.prof + 1
        self.izq = None
        self.der = None
        self.hoja = True

    def recorre(self, prof=0):
        if not self.hoja:
            if self.der is not None and self.izq is not None:
                #print "Entro izq der"
                print 'R %d @ %d  ---> I %d :: D %d' % (self.valor, self.prof, self.izq.valor, self.der.valor)
                self.izq.recorre(self.izq.prof)
                self.der.recorre(self.der.prof)
                return
            if self.der is None and self.izq is not None:
                #print "Entro der"
                print 'R %d @ %d  ---> I %d' % (self.valor, self.prof, self.izq.valor)
                self.izq.recorre(self.izq.prof)
                return
            if self.der is not None and self.izq is None:
                #print "Entro izq"
                print 'R %d @ %d  ---> D %d' % (self.valor, self.prof, self.der.valor)
                self.der.recorre(self.der.prof)
                return
        
            
    def buscar(self, valor):
        if self.valor  == valor:
            return True
        elif self.hoja:
            return False
        elif (valor < self.valor):
            return self.izq.buscar(valor)
        else:
            return self.der.buscar(valor)

    def agregar(self, valor):
        if self.valor == valor:
            print '%d Rep' % valor
            return
        if self.hoja:
            self.hoja = False
            if valor < self.valor:
                self.izq = nodo(valor, self)
            else:
                self.der = nodo(valor, self)
        else:
            if (valor < self.valor):
                if self.izq is not None:
                    self.izq = self.izq.agregar(valor)
                else:
                    self.hoja = False
                    self.izq = nodo(valor, self)
            else:
                if self.der is not None:
                    self.der = self.der.agregar(valor)
                else:
                    self.hoja = False
                    self.der = nodo(valor,self)
            self = self.balancear()
            self.actualizar()
        return self

    def actualizar(self):
        if self is None: 
            return
        else:
            self.altura = max(alturaN(self.izq), alturaN(self.der)) + 1

    def balancear(self):
        #print self
        if self is None: return
        print "Valor",self.valor
        if alturaN(self.izq) - alturaN(self.der) == 2:
            print "desequilibrio hacia la izquierda"
            if alturaN(self.izq.izq) >= alturaN(self.izq.der):
                print "desequilibrio simple a la izq"
                self = self.rotarS(True)
            else:
                print "desequilibrio doble a la izquierda"
                self = self.rotarD(True)
        elif alturaN(self.der) - alturaN(self.izq) == 2:
            print "desequilibrio hacia la derecha"
            if alturaN(self.der.der) >= alturaN(self.der.izq):
                print "desequilibrio simple hacia la derecha"
                self = self.rotarS(False)
            else:
                print "desequilibrio doble hacia la derecha"
                self = self.rotarD(False)
        return self

    
    def rotarS(self, Nizq):
        x = None
        if Nizq:
            x = self.izq
            self.izq = x.der
            x.der = self
        else:
            x = self.der
            self.der = x.izq
            x.izq = self
        self.actualizar()
        x.actualizar()
        return x

    def rotarD(self, Nizq):
        if Nizq:
            self.izq = self.izq.rotarS(False)
            self = self.rotarS(True)
        else:
            self.der = self.der.rotarS(True)
            self = self.rotarS(False)
        return self

def alturaN(nodo):
        if nodo is None:
            return -1
        else:
            return nodo.altura



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
        width = (2**(raiz.altura))*space
        for i in range(raiz.altura+1):
                cnodes = 2**i
                spaces = (width/cnodes)
                for n in lvlnode(raiz, i):
                        t = str(n and n.valor or "")#returns "" if n is None
                        tspaces = (spaces -len(t))/2
                        print " "*tspaces
                        print t
                        print " "*tspaces
                print "\n"



raiz = nodo(10)
#print 'Raiz %d ' % raiz.valor


from random import randint
# for i in xrange(5):
#     valor = randint(1, 100)
#     print 'A %d' % valor
#     #print raiz.buscar(valor)
#     raiz.agregar(valor)

valores = [52,94,45,40,14,11,41,48]
for i in xrange(len(valores)):
    print "A %d" % valores[i]
    raiz.agregar(valores[i])
    raiz.recorre()

