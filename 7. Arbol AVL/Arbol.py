from random import randint, choice, random
class nodo:
    def __init__(self,valor):
        self.valor = valor;
        self.padre = None
        self.hijos =list()

    def recorre(self, prof):
        prefijo = ' -> ' * prof
        print ' %s %d ' % (prefijo, self.valor)
        for hijo in self.hijos:
            hijo.recorre(prof + 1)
        return

        
    def __str__(self):
        nombres = ''
        for hijo in self.hijos:
            nombres += '%d' % hijo.valor
        return '%d: %s' % (self.valor, nombre)

    def __repr__(self):
        return str(self)
        
    def agrega(self,valor,padre):
        if self.valor == padre:
            hijo = nodo(valor)
            self.hijos.append(hijo)
            hijo.padre = self
            return True
        else:
            for hijo in self.hijos:
                if hijo.agrega(valor,padre):
                    return True
            return False
        
    def buscar(self, valor,prof):
        
        if self.valor == valor:
            print '%d en prof %d'% (valor, prof)
            return
        prof += 1
        for hijo in self.hijos:
            #print hijo.valor, valor, prof
            if hijo.valor == valor:
                print '%d en prof %d'% (valor, prof)
                return
                #return prof
            hijo.buscar(valor,prof)
            
    def numhijos(self, valor):
        if self.valor == valor:
            return len(self.hijos)
            return

        for hijo in self.hijos:

            if hijo.valor == valor:
                return len(self.hijos)
                return

            hijo.numhijos(valor)
            
            
    def eliminar(self, valor):
        if self.valor == valor:
            hijo1 = self.hijos[0]
            hijo2 = self.hijos[1]

            
            self.padre = hijo1
            hijo1.padre = None
            self.valor = hijo2.valor
            self.hijos = hijo2.hijos
        return
    

#Matriz Agregar y Eliminar
#    A    E    B
# A 0.6  0.3  0.2 
# E 0.4  0.3  0.3
# B 0.3  0.6  0.1

opciones= ['A', 'E', 'B']
Matriz = dict()
Matriz['A']=[0.6, 0.3, 0.2]
Matriz['E']=[0.4, 0.3, 0.3]
Matriz['B']=[0.3, 0.6, 0.1]

MAX = 30
DESDE = 0
HASTA = 1000

padres = list()
r = randint(DESDE,HASTA)
print 'A %d en raiz' % (r)
padres.append(r)
raiz = nodo(r)

hijos = dict()
for i in xrange(0,MAX):
    padre = choice(padres)
    if random() < 0.7:
    
    #print padre, raiz.numhijos(padre)
    #if raiz.numhijos(padre) < 2:
        hijo = randint(DESDE,HASTA)
        padres.append(hijo)
        raiz.agrega(hijo, padre)
        print 'A %d a %d' % (hijo, padre)
    #else: 
    #    padres.remove(padre)
    else:
        print 'B',
        raiz.buscar(padre,0)

print "Arbol"
raiz.recorre(0)


#print 
#print 'Buscar elemento'
#raiz.buscar(choice(padres),0)

#raiz.eliminar(r)
#raiz.recorre(0)
