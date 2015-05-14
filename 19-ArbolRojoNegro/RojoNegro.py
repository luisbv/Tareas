t = 4

class nodo:
    def __init__(self, p=None):
        self.izq = None
        self.der = None
        self.padre = p
        self.color = "Negro"

    def abuelo(self):
        if self is not None and self.padre is not None:
            return self.padre.padre
        else:
            return
    def tio(self):
        a = abuelo(self)
        if a is None:
            return None
        if self.padre == a.izq:
            return a.der
        else:
            return a.izq

    ##Insertar Caso 1 si no tengo padre soy raiz (negro)
    def insertar_caso1(self):
        if self.padre is None:
            self.color = "Negro"
        else:
            print "Insertar Caso 2"
            self.insertar_caso2()

    def insertar_caso2(self):
        if self.padre.color == "Negro":
            return
        else:
            self.insertar_caso3()

    def insertar_caso3(self):
        t = self.tio()

        if t is not None and t.color == "Rojo":
            self.valor = val
            self.padre.color = "Negro"
            t.color = "Negro"
            a = self.abuelo()
            a.color = "Rojo"
            insertar_caso1(a)
        else:
            self.insertar_caso4()

    def insertar_caso4(self,val):
        a = self.abuelo()
        if self == self.padre.der and self.padre == a.izq:
            rotarI(self.padre)
            self = self.izq
        elif self == self.padre.izq and self.padre == a.der:
            rotarD(self.padre)
            self = self.der
        self.insertar_caso5()


    def insertar_caso5(self):
        a = self.abuelo()
        self.padre.color = "Negro"
        a.color = "Rojo"
        if self == self.padre.izq:
            rotarD(a)
        else:
            rotarI(a)

def rotarD(p):
    global raiz
    aux = raiz
    if p.padre is not None and p.padre.der == p:
        aux = p.padre.der
    elif p.padre is not None and p.padre.izq == p:
        aux = p.padre.izq
    
    aux = p.izq
    aux.padre = p.padre
    p.padre = aux
    p.izq = aux.der
    aux.der = p
    if p.izq is not None:
        p.izq.padre = p

def rotarI(p):
    global raiz
    aux = raiz
    if p.padre is not None and p.padre.der == p:
        aux = p.padre.der
    elif p.padre is not None and p.padre.izq == p:
        aux = p.padre.izq
    
    aux = p.der
    aux.padre = p.padre
    p.padre = aux
    p.der = aux.izq
    aux.izq = p
    if p.der is not None:
        p.der.padre = p


raiz = nodo()


