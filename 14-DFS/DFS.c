#include <stdio.h> // imprimir
#include <math.h> // inicializar pseudoaleatorio
#include <stdlib.h> // malloc & free

#define TRUE 1
#define FALSE 0
#define DESOCUPADO -1
typedef struct verticeArbol{
    int etiqueta;
    int* vecinos = NULL;
    int marcado = FALSE;
} vertice;


void dfs(vertice inicio){:
    vertice actual;
    int* pila = NULL;
    int inicial = 1;
    int largo  = inicial;
    pila = (vertice*)malloc(sizeof(inicial*vetice));
    pila[0] = inicio;
    
    while largo > 0{
        actual = pila[0];
        
        actual = pila.pop(0)
        if (actual.marcado == FALSE){
            printf("Visita en %d\n", actual.etiqueta);
            actual.marcado = TRUE;
            for (int i = 0; i < largo; i++){

                if (pila[i] == DESOCUPADO){break;}
                pila[i+1] = pila[i];
                pila[i] = actual.vecino
            }
            for vecino in actual.vecinos:
                pila.insert(0,vecino)
        }
        
    }
    
}
#aristas = ['ad', 'ac','ae','bf','bc','de','be','fc']

int main(int argv, char** args){

}

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