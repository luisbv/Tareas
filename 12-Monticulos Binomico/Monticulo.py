class arbol:
    def __init__(self, c=None, g=None,ph = None, h=None, p=None):
        self.clave = c
        self.hijos = list()
        self.k = 0

    def imprime(self, prefix):
        s = '%s%d\n' % (prefix, self.clave)
        for hijo in self.hijos:
            s += '%s\n' % hijo.imprime(prefix + ' ')
        return s[:-1]

    def __str__(self):
        ##Como voy a imprimir
        return self.imprime('')

    def __repr__(self):
        return str(self)


class Monticulo:
    def __init__(self, d=dict()):
        self.d = d

    def __str__(self):
        s = ''
        ##Como voy a imprimir
        for k in self.d:
            s += '\n***\nk=%d\n' % k
            if k in self.d:
              s += '%s' % str(self.d[k])
        return s
             

    def __repr__(self):
        return str(self)

    def agregar(self, valor):
        self.insertar(arbol(valor))

    def insertar(self, a):
        if a.k not in self.d:
            self.d[a.k] = a
        else:
            h = self.d[a.k]
            del self.d[a.k]    
            if h.clave < a.clave:
                h.hijos.append(a)
                h.k += 1
                self.insertar(h)
            else:
                a.hijos.append(h)
                a.k += 1
                self.insertar(a)
            
        
M = Monticulo()

M.agregar(7)
M.agregar(5)
M.agregar(6)
M.agregar(8)
M.agregar(3)
M.agregar(10)
M.agregar(11)
M.agregar(12)


print M