from random import randint, choice, random

class nodo:
    def __init__(self, valor, p=None, a=1):
        self.valor = valor
        self.altura = a
        self.claves = None
        self.padre = p
        if self.padre is None:
            self.prof = 0
        else:
            self.prof = self.padre.prof + 1
        self.izq = None
        self.der = None
        self.hoja = True


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
            minimo = min(valor, self.valor)
            maximo = max(valor, self.valor)
            if self.padre is not None:
                self.prof = self.padre.prof + 1


            self.izq = nodo(minimo, self)
            self.der = nodo(maximo, self)
            return True #Hubo cambios en la hoja
        else:
            if (valor < self.valor):

                cambio = self.izq.agregar(valor)
                self.actualizar(cambio)
                #Aqui puedo poner algo y me quedo en donde esta el return
            else:

                self.der.agregar(valor)

    def actualizar(self, cambio):
        if self.padre is None:
            self.altura += 1
            self.clave = max(self.izq.altura, self.der.altura)
            return
        if cambio:
            self.padre.altura += 1
            #self.padre.padre.balance()
            self.clave = max(self.padre.izq.altura, self.padre.der.altura)
            self.padre.actualizar(cambio)
        return

    def hermano(self):
        if self.padre.izq == self:
            return self.padre.der
        else:
            return self.padre.izq

    def eliminar(self, valor):
        if self.padre is None: # soy raiz
            return None
        if self.padre.padre is None: # papa es raiz
            return self.hermano
        elif self.valor == valor:
            if self.padre.padre.izq == self.padre:
                self.padre.padre.der = self.hermano
                return self
            else:
                self.padre.padre.izq = self.hermano
                return self
            if self.padre.padre.der == self.padre:
                self.padre.padre.izq = self.hermano
                return self
            else:
                self.padre.padre.der = self.hermano
                return self
        if self.hoja:
            print '%d no existe' % valor
            return self
        else:
            if (valor < self.valor):
                return self.izq.eliminar(valor)
            else:
                return self.der.eliminar(valor)


    def balance(self):
    	b = abs(self.izq.altura - self.der.altura)
    	minimo = min(self.izq.altura, self.der.altura)
    	maximo = max(self.izq.altura, self.der.altura)
    	if b > 1 :
    		print 'No esta balanceado'
    		#self.padre.balance()
    	else:
    		print 'Esta balanceado'
    		return


raiz = nodo(10)
print 'Raiz %d ' % raiz.valor
from random import randint
for i in xrange(5):
    valor = randint(1, 100)
    print 'A %d' % valor
    #print raiz.buscar(valor)
    raiz.agregar(valor)


    #print raiz.buscar(valor)
#print
#print 'Recorrer'
#raiz.recorre()

#print 
#print 'Altura'

#raiz.CalcularAltura()
print 'Profundidad de la raiz %d' % raiz.prof
print 'Altura de raiz %d' % raiz.altura
#print 'Clave de raiz %d' % raiz.clave