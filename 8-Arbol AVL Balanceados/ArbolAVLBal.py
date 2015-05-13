from random import randint, choice, random

class nodo:
    def __init__(self, valor, p=None, a=1):
        self.valor = valor
        self.altura = a
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
            print 'R %d @ %d  ---> I %d :: D %d' % (self.valor, self.prof, self.izq.valor, self.der.valor)
            self.izq.recorre(self.izq.prof)
            self.der.recorre(self.izq.prof)
            return
        else:
            if self.padre.izq == self:
                if self.padre.der.hoja:
                    return
                else:
                    self.padre.der.recorre(self.padre.der.prof)
            else:
                if self.padre.izq.hoja:
                    return
                else:
                    self.padre.izq.recorre(self.padre.izq.prof)
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
        print self.valor
        if self.valor == valor:
            print '%d Rep' % valor
            return
        if self.hoja:
            self.hoja = False
            if valor < self.valor:
                self.izq = nodo(valor, self)
            else:
                self.der = nodo(valor, self)
            return True #Hubo cambios en la hoja
        else:
            if (valor < self.valor):
                c = self.izq.agregar(valor)
                #Aqui puedo poner algo y me quedo en donde esta el return
            else:
                c = self.der.agregar(valor)
            self.balancear()
            self.actualizar(c)

    def actualizar(self, cambio):
        if cambio is None: 
            return
        if cambio:
            self.altura = max(alturaN(self.izq), alturaN(self.der))
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

    
    def balancear(self):
        if self is None: return


        b = abs(alturaN(self.izq) - alturaN(self.der))
        minimo = min(alturaN(self.izq), alturaN(self.der))
        maximo = max(alturaN(self.izq), alturaN(self.der))
    
        if b > 1 :
            print 'No esta balanceado'
            if alturaN(self.izq) == maximo:
                if alturaN(self.izq.izq) >= alturaN(self.izq.der):
                    self.rotarS(True)
                else:
                    self.rotarD(True)
            else:
                if alturaN(self.der.der) >= alturaN(self.der.izq):
                    self.rotarS(False)
                else:
                    self.rotarD(False)
        else:
            print 'Esta balanceado'
            return



    def rotarD(self, Nizq):
        if Nizq:
            self.izq.rotarS(False)
            self.rotarS(True)
        else:
            self.der.rotarS(True)
            self.rotarS(False)
        return

    def rotarS(self, Nizq):
        x = None
        c = None
        if Nizq:
            x = self.izq
            self.izq = x.der
            x.der = self
            c = True
        else:
            x = self.der
            self.der = x.izq
            x.izq = self.der
            c = True
        self.actualizar(c)
        x.actualizar(c)
        return x

def alturaN(nodo):
        if nodo is None:
            return -1
        else:
            return nodo.altura

raiz = nodo(10)
print 'Raiz %d ' % raiz.valor
from random import randint
for i in xrange(5):
    valor = randint(1, 100)
    print 'A %d' % valor
    #print raiz.buscar(valor)
    raiz.agregar(valor)

raiz.recorre()

print "Eliminar: ", valor
raiz.eliminar(valor)

raiz.recorre()

#raiz.CalcularAltura()
print 'Profundidad de la raiz %d' % raiz.prof
print 'Altura de raiz %d' % raiz.altura
#print 'Clave de raiz %d' % raiz.clave