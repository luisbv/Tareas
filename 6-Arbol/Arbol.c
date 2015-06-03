#include <stdio.h> // imprimir
#include <math.h> // inicializar pseudoaleatorio
#include <stdlib.h> // malloc & free


#define MAXIMO 10

typedef struct nodoDeArbol {
  int valor;
  int numeroDeHijos;
  struct nodoDeArbol* padre;
  struct nodoDeArbol** hijos;
} nodo;


typedef struct arbolEnlazado {
    struct nodoDeArbol* raiz;  
}arbol;

int main(int argv, char** args){
    
    arbol* a = (arbol*)malloc(sizeof(arbol));
    a->raiz = NULL;
    nodo** aux = (nodo**)malloc(sizeof(arbol)*8);
    nodo* n = NULL;

    n = (nodo*)malloc(sizeof(nodo));

    n->valor = 0;
    n->padre = NULL;
    n->numeroDeHijos = 2;
    n->hijos = (nodo**)malloc(sizeof(nodo));
    n->hijos[0]->valor = 3;
    n->hijos[1]->valor = 2;

    printf("hola\n");

    return 0;
}


