from random import randint, choice, random

class nodo:
    def __init__(self, valor, p=None, prof=0):
    	self.valor = valor
        self.altura = None
        self.prof = prof
        self.claves = None
        self.padre = p
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
            print 'R %d -> I %d :: D %d' % (self.valor, minimo, maximo)
            self.izq = nodo(minimo, self,self.prof+1)
            self.der = nodo(maximo, self,self.prof+1)
        else:
            if (valor < self.valor):
                self.izq.agregar(valor)
            else:
                self.der.agregar(valor)
                
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
    '''            
    def recorre(self, prof=0):
    	if not self.hoja:
        	prefijo = ' -> ' * prof
        	print ' %s %d ' % (prefijo, self.valor)
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
    ''' 	
    def recorre(self, prof=0):
    	if not self.hoja:
    		print 'R %d -> I %d :: D %d' % (self.valor, self.izq.valor, self.der.valor)
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
        	
raiz = nodo(10)
print 'Raiz %d ' % raiz.valor
from random import randint
for i in xrange(20):
    valor = randint(1, 100)
    #print raiz.buscar(valor)
    raiz.agregar(valor)
    
    #print raiz.buscar(valor)
print
print 'Recorrer'
raiz.recorre()
