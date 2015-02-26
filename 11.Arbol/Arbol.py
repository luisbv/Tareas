t = 4
class nodo:
    def __init__(self, c=None, h=None, t = 0):
        self.hijos = h
        self.claves = c
        self.maximo = 2 * t -1
        self.minimo = 

    def lleno(self):
        if len(self.hijos) >= 2 * t - 1
            return True

    def vacio(self):
        if len(self.hijos) <= t - 1:
            return True

    def buscar(self, valor):
        for pos in xrange(0, len(self.claves)):
            c = self.claves[pos]
            if c == valor: ##Si se encuentra el valor regresar true
                return True
            elif valor < c and self.hijos is not None: # si es menor continuar busqueda en hijos
                return self.hijos[pos].buscar(valor)
            elif self.hijos is None:
                return False
        return self.hijos[-1].buscar(valor)


    def insertar(self, valor):
        self.buscar(valor)



a = nodo([5, 8, 13])
b = nodo([22, 31, 45])
c = nodo([52, 63, 74])
d = nodo([99, 120])
raiz = nodo([18, 48, 82], [a, b, c, d])


print raiz.buscar(5)
print raiz.buscar(6)
print raiz.buscar(26)
print raiz.buscar(68)
print raiz.buscar(102)
print raiz.buscar(1000)
print raiz.buscar(2)
print raiz.buscar(99)

print raiz.buscar(48)