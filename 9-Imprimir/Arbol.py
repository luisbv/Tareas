from random import randint, choice, random
class nodo:
    def __init__(self,valor, p=None, prof = 0, a = 1):
        self.valor = valor;
        self.padre = p
        self.izq =None
        self.der = None
        self.hoja = True
        self.prof = prof
        self.altura = a
        self.clave = None

    def recorre(self, prof):
        prefijo = ' -> ' * prof
        print ' %s %d ' % (prefijo, self.valor)
        if not self.hoja:
            if self.der is not None and self.izq is not None:
                self.izq.recorre(prof + 1)
                self.der.recorre(prof + 1)
        return

    def __str__(self):
        nombres = ''
        if not self.hoja:
            nombres += '%d' % self.izq.valor
            nombres += '%d' % self.der.valor
        return '%d: %s' % (self.valor, nombres)

    def __repr__(self):
        return str(self)

    def agregar(self, valor):
        
        if self.valor == valor:
            print '%d Rep' % valor
            return
        if self.hoja:
            #print valor,
            self.hoja = False
            if valor < self.valor:
                #print " A IZQ"
                self.izq = nodo(valor, self, prof = self.prof + 1)
            else:
                #print " A DER"
                self.der = nodo(valor, self, prof = self.prof + 1)
            print "Hubo Cambio"
            return True
            #minimo = min(valor, self.valor)
            #maximo = max(valor, self.valor)
            #self.izq = nodo(minimo, self)
            #self.der = nodo(maximo, self)
        else:
            if (valor < self.valor):
                if self.izq is not None:
                    #print self.valor,
                    #print " R IZQ"
                    cambio = self.izq.agregar(valor)
                else:
                    self.izq = nodo(valor, self)
            else:
                if self.der is not None:
                    #print self.valor,
                    #print " R DER"
                    cambio = self.der.agregar(valor)
                    print "actualizar"
                    <   º
                else:
                    self.der = nodo(valor, self)

    def actualizar(self, cambio):
        if self.padre is None:
            self.altura += 1
            return
        if cambio:
            print "Hubo Cambio"
            self.padre.altura += 1
            print "Balance"
            self.padre.padre.balance()
            self.padre.actualizar(cambio)
        return

    def balance(self):
        b = abs(self.izq.altura - self.der.altura)
        if b > 0 :
            print 'No esta balanceado'
            self.padre.balance()
        else:
            print 'Esta balanceado'
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


    def preOrden(self):
        if (self.hoja):
            print self.valor,
            return
        print self.valor,
        self.izq.preOrden()
        self.der.preOrden()
    
    def inOrden(self):
        if (self.hoja):
            print self.valor,
            return
        
        self.izq.inOrden()
        print self.valor,
        self.der.inOrden()

    def posOrden(self):
        if (self.hoja):
            print self.valor,
            return
        
        self.izq.posOrden()
        
        self.der.posOrden()
        print self.valor,
        
        
        
        
    def hermano(self):
        if self.padre.izq == self:
            return self.padre.der
        else:
            return self.padre.izq
    
    def eliminar(self, valor):
        #if self.padre is None: # soy raiz
        #    return 
        #if self.padre.padre is None: # papa es raiz
        #    return self.hermano
        if self.valor == valor:
            if self.hoja:
                print "%d Es hoja" % self.valor
                print self.padre
                if self.padre.der == self:
                    print "Hijo derecho"
                    self.padre.der = None
                    return
                else:
                    print "Hijo izquierdo"
                    self.padre.izq = None
                    return
            else:
                if self.izq is None:
                    self.padre.der = self.der
                else:
                    self.padre.der = self.der
                
        if self.hoja:
            print '%d no existe' % valor
            return False
        else:
            print "No es hoja"
            if (valor < self.valor):
                if self.izq is not None:
                    return self.izq.eliminar(valor)
            else:
                if self.der is not None:
                    return self.der.eliminar(valor)

    def RSI(self):
        u = self
        t = self.padre
        v = self.hermano
        A = v.izq
        B = v.der
        
        t.der = A
        v.izq = t
        v.der = B
        return

    def RSD(self):
        u = self
        t = self.padre
        v = self.hermano
        A = u.izq
        B = u.der
        
        t.izq = B
        t.der = v
        u.der = t
        return

    def RDID(self):
        w = self
        u = self.padre
        t = self.padre.padre
        v = t.der
        A = u.izq
        B1 = w.izq
        B2 = w.der
        

        t.izq = B2
        t.der = v
        u.der = B1
        w.izq = u
        w.der = t

        return

    def RDID(self):
        w = self
        u = self.padre.hermano
        t = self.padre.padre
        v = t.der
        A1 = w.izq
        A2 = w.der
        B = v.der

        t.izq = u
        t.der = A1
        v.der = B
        v.izq = A2
        w.izq = t
        w.der = v
        

        return


raiz = nodo(5)
raiz.agregar(7)
raiz.agregar(6)
raiz.agregar(8)
raiz.agregar(3)
raiz.agregar(4)
raiz.agregar(1)
raiz.agregar(0)
raiz.agregar(2)

print
print "Arbol"
raiz.recorre(0)

print
print
print "Arbol preOrden"
raiz.preOrden()

print
print
print "Arbol inOrden"
raiz.inOrden()

print
print
print "Arbol posOrden"
raiz.posOrden()

print
print
print "Eliminar %d" % 8
print raiz.eliminar(8)

print
print "Arbol"
raiz.recorre(0)

print 'Profundidad de la raiz %d' % raiz.prof
print 'Altura de raiz %d' % raiz.altura
#print 'Clave de raiz %d' % raiz.clave