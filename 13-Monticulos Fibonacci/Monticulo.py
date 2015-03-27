class nodo:
    def __init__(self, c=None,ph = None, h=None, p=None):
        self.clave = c
        self.izq = ph
        self.hermano = h
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

 