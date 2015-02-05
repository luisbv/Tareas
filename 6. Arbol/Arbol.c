#include <stdio.h> // imprimir
#include <math.h> // inicializar pseudoaleatorio
#include <stdlib.h> // malloc & free


#define MAXIMO 100

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

  e->valor = 0;
  e->padre = NULL;

  e->hijos = (nodo**)malloc(sizeof(2*nodo));
  e->hijos0[] = 3;
  e->hijos0[] = 3;
  e->numeroDeHijos = 2;
  
  
  return 0;
}


