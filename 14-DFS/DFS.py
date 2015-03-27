from random import choice
class vertice:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.vecinos = set()
        self.marcado = False
    def __str__(self):
        return self.etiqueta

    def __repr__(self):
        return str(self)

def dfsrec(pila):
    actual = pila.pop()
    if actual.marcado:
        return
    print "Visita en", actual
    actual.marcado = True
    for vecino in actual.vecinos:
        dfsrec(vecino)
    return

    





def dfs(inicio):
    pila = [inicio]
    while len(pila) > 0:
        actual = pila.pop(0)
        if actual.marcado:
            continue
        print "Visita en", actual
        actual.marcado = True
        for vecino in actual.vecinos:
            pila.insert(0,vecino)
    return
    
#aristas = ['ad', 'ac','ae','bf','bc','de','be','fc']

aristas = ['ac','bf','bc','de','fc']

vertices = dict()

for arista in aristas:
    inicio = arista[0]
    final = arista[1]
    v = None
    w = None
    if inicio not in vertices:
        v = vertice(inicio)
        vertices[inicio] = v
    else:
        v = vertices[inicio]
    if final not in vertices:
        w = vertice(final)
        vertices[final] = w
    else:
        w = vertices[final]
    v.vecinos.add(w)
    w.vecinos.add(v)
start = choice(vertices.values())

print "Iterativo"
dfs(start)

print "Recursivo"
dfsrec([start])