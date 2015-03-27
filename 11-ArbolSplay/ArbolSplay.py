
class nodo:
    def __init__(self, c=None, p=None):

        self.claves = c
        self.padre = p
        self.izq = None
        self.der = None

    def splay(self,l):
        x = self
        p = self.padre
        q = self.padre.padre

        if x == p.izq:
            x.RSI(p)
        elif x == p.der:
            x.RSD(p)
        elif x == p.izq and p == q.izq:
            x.RDD(p,q)
        elif x == p.der and p == q.der:
            x.RDI(p,q)
        elif x == p.izq and p = q.der:
            x.RSDI(p,q)
        elif x == p.der and p = q.izq:
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

print raiz