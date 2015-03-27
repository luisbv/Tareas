t = 4

class nodo:
    def __init__(self, c=list(), h=None, p=None,prof=0):
        global t
        self.hijos = h
        self.claves = c
        self.padre = p
        self.maximo = 2 * t -1
        self.minimo = t - 1
        self.prof = prof
        self.raiz = False
        self.padre = p

    def __str__(self):
        ##Como voy a imprimir
        s = '%s%s' % ('->' * self.prof, str(self.claves))
        if self.hijos is not None:
            s = '%s\n' % s
            for h in self.hijos:
                s = '%s%s' % (s, str(h))
            s = '%s' % s[:-1]
        return s + '\n'


    def __repr__(self):
        return str(self)

    def lleno(self):
        global t
        return len(self.claves) >= (2 * t - 1)

    def vacio(self):
        global t
        return len(self.claves) <= (t - 1)

    def buscar(self, valor):
        for pos in xrange(0, len(self.claves)):
            c = self.claves[pos]
            if c == valor: ##Si se encuentra el valor regresar true
                return True
            elif valor < c and self.hijos is not None: # si es menor continuar busqueda en hijos
                return self.hijos[pos].buscar(valor)
            elif self.hijos is None: ##Soy hoja
                return False
        return self.hijos[-1].buscar(valor)

    def agregar(self, valor):
        print "A %d" % valor
        if self.padre is None:
            if self.lleno():
                print "Raiz. Esta lleno"
                mediana = self.claves[t-1]
                self.hijos = [nodo(self.claves[0:t], prof=self.prof+1, p=self), nodo(self.claves[t:len(self.claves)], prof=self.prof+1, p=self)]
                self.claves = [mediana]
            else:
                self.claves.append(valor)
                self.claves = sorted(self.claves)
            print self
        else:
            print "valor:", valor
            if self.lleno():
                print "Hijo. Esta lleno"
                mediana = self.claves[t-1]
                self.hijos = [nodo(self.claves[0:t], prof=self.prof+1, p=self), nodo(self.claves[t:len(self.claves)], prof=self.prof+1, p=self)]
                self.claves = [mediana]
            else:
                self.claves.append(valor)
                self.claves = sorted(self.claves)
            print self
                    




a = nodo([5, 8, 13], p=1)
b = nodo([22, 31, 45], p=1)
c = nodo([52, 63, 74], p=1)
d = nodo([99, 120], p=1)
raiz = nodo([18, 48, 82], [a, b, c, d])

print

print "*********PRUEBA BUSQUEDA*********"
print raiz
print raiz.buscar(5)
print raiz.buscar(6)
print raiz.buscar(26)
print raiz.buscar(68)
print raiz.buscar(102)
print raiz.buscar(1000)
print raiz.buscar(2)
print raiz.buscar(99)
print raiz.buscar(48)


print
print
print "*********PRUEBA AGREGAR*********"
print

raiz1 = nodo()
raiz1.agregar(69)
raiz1.agregar(1)
raiz1.agregar(20)
raiz1.agregar(35)
raiz1.agregar(50)

raiz1.agregar(71)
raiz1.agregar(97)

raiz1.agregar(5)


