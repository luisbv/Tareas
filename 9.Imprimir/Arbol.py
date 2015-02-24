from random import randint, choice, random
class nodo:
    def __init__(self,valor, p=None):
        self.valor = valor;
        self.padre = p
        self.izq =None
        self.der = None
        self.hoja = True
        

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
                self.izq = nodo(valor, self)
            else:
                #print " A DER"
                self.der = nodo(valor, self)
            #minimo = min(valor, self.valor)
            #maximo = max(valor, self.valor)
            #self.izq = nodo(minimo, self)
            #self.der = nodo(maximo, self)
        else:
            if (valor < self.valor):
                if self.izq is not None:
                    #print self.valor,
                    #print " R IZQ"
                    self.izq.agregar(valor)
                else:
                    self.izq = nodo(valor, self)
            else:
                if self.der is not None:
                    #print self.valor,
                    #print " R DER"
                    self.der.agregar(valor)
                else:
                    self.der = nodo(valor, self)

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