
class nodo:
    def __init__(self, c=None, p=None):
        self.clave = c
        self.padre = p
        self.izq = None
        self.der = None
        self.hoja = True

    def agregar(self, c):
        if self.hoja:
            self.hoja = False
            if c < self.clave:
                self.izq = nodo(c, self)
            else:
                self.der = nodo(c, self)
        else:
            if (c < self.clave):
                if self.izq is not None:
                    self.izq.agregar(c)
                else:
                    self.hoja = False
                    self.izq = nodo(c, self)
            else:
                if self.der is not None:
                    self.der.agregar(c)
                else:
                    self.hoja = False
                    self.der = nodo(valor,self)

    def splay(self, c):
        self.agregar(c)
        print "Paso agregar"
        if self.padre is None: return
        print "Paso padre"
        if self.padre.padre is None: return
        print "Paso abuelo"
        x = self
        p = self.padre
        q = self.padre.padre

        if x.clave == p.izq.clave:
            x.RSI(p)
        elif x.clave == p.der.clave:
            x.RSD(p)
        elif x.clave == p.izq.clave and p.clave == q.izq.clave:
            x.RDD(p,q)
        elif x.clave == p.der.clave and p.clave == q.der:
            x.RDI(p,q)
        elif x == p.izq and p == q.der:
            x.RSDI(p,q)
        elif x == p.der and p == q.izq:
            x.RSID(p,q)

    # Rotacion simple derecha
    def RSD(self, p):
        x = self
        A = x.izq
        B = x.der
        C = p.der
        
        x.izq = A
        p.izq = B
        p.der = C
        x.der = p

        return x

    # Rotacion simple izquerda
    def RSI(self, p):
        x = self
        A = p.izq
        B = x.izq
        C = x.der
        
        x.der = C
        p.izq = A
        p.der = B
        x.izq = p
        return x

    # Rotacion doble derecha
    def RDD(self, p, q):
        x = self
        A = x.izq
        B = x.der
        C = p.der
        D = q.der

        q.izq = C
        q.der = D
        p.der = q
        p.izq = B
        x.izq = A
        x.der = p
        return x

    # Rotacion doble izquierda
    def RDI(self, p, q):
        x = self
        A = q.izq
        B = p.izq
        C = x.izq
        D = x.der

        q.izq = A
        q.der = B
        p.der = C
        p.izq = q
        x.izq = p
        x.der = D
        return x

    # Rotacion simple izquierda derecha
    def RSDI(self, p, q):
        x = self
        A = q.izq
        B = p.der
        C = x.izq
        D = x.der

        q.izq = A
        q.der = C
        p.der = B
        p.izq = D
        x.izq = q
        x.der = p
        return x
    
    # Rotacion simple derecha izquierda
    def RSID(self, p, q):
        x = self
        A = p.izq
        B = x.izq
        C = x.der
        D = q.der

        p.izq = A
        p.der = B
        q.izq = C
        q.der = D
        x.izq = p
        x.der = q
        return x

raiz = nodo(10)

raiz.splay(11)
raiz.splay(12)
raiz.splay(13)
raiz.splay(13)
print raiz.der.der.clave