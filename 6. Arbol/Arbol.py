class nodo:
    def __init__(self,valor):
        self.valor = valor;
        self.padre = None
        self.hijos =list()


    def recorre(self, prof):
        prefijo = ' ' * prof
        print ' %s %d ' & (prefijo, self.valor)
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


raiz = nodo(3)

raiz.agrega(5,3)

raiz.recorre(0)
