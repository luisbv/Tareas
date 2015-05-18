#include <stdio.h> // imprimir
#include <math.h> // inicializar pseudoaleatorio
#include <stdlib.h> // malloc & free


#define MAXIMO 8

typedef struct nodoDeArbol {
  int valor;
  int numeroDeHijos;
  struct nodoDeArbol* padre;
  struct nodoDeArbol** hijos;
} nodo;


void imprime(nodo* actual, int profundidad){
    int i;
    char* prefijo = (char*)malloc(sizeof(char) * (profundidad + 1));
    for (i = 0; i < profundidad; i++) {
        prefijo[i] = '-';
    }
    prefijo[i] = '\0';
    
    if (actual->numeroDeHijos == 0) {
        printf("%s H %d\n", prefijo, actual->valor);
        return;
    }else{
        printf("%s N %d\n", prefijo, actual->valor);
    }
    free(prefijo);
    for (i = 0; i < actual->numeroDeHijos; i++) {
        imprime(actual->hijos[i], profundidad + 4);
    }
    return;
}


int main(int argv, char** args){
    
    nodo* raiz = (nodo*)malloc(sizeof(nodo));
    raiz = NULL;
    nodo** aux = (nodo**)malloc(sizeof(nodo)*MAXIMO);
    nodo* n = NULL;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 0;
    n->padre = NULL;
    n->numeroDeHijos = 2;
    n->hijos = (nodo**)malloc(sizeof(nodo)*n->numeroDeHijos);
    raiz = n;
    aux[0] = n;
    
    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 1;
    n->numeroDeHijos = 1;
    n->hijos = (nodo**)malloc(sizeof(nodo)*n->numeroDeHijos);
    aux[1] = n;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 2;
    n->numeroDeHijos = 1;
    n->hijos = (nodo**)malloc(sizeof(nodo)*n->numeroDeHijos);
    aux[2] = n;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 3;
    n->numeroDeHijos = 0;
    n->hijos = NULL;
    aux[3] = n;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 4;
    n->numeroDeHijos = 2;
    n->hijos = (nodo**)malloc(sizeof(nodo)*n->numeroDeHijos);
    aux[4] = n;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 5;
    n->numeroDeHijos = 1;
    n->hijos = (nodo**)malloc(sizeof(nodo)*n->numeroDeHijos);
    aux[5] = n;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 6;
    n->numeroDeHijos = 0;
    n->hijos = NULL;
    aux[6] = n;

    n = (nodo*)malloc(sizeof(nodo));
    n->valor = 7;
    n->numeroDeHijos = 0;
    n->hijos = NULL;
    aux[7] = n;

    aux[1]->padre = aux[5];
    aux[2]->padre = aux[4];
    aux[3]->padre = aux[0];
    aux[4]->padre = aux[0];
    aux[5]->padre = aux[2];
    aux[6]->padre = aux[1];
    aux[7]->padre = aux[4];

    aux[0]->hijos[0] = aux[3];
    aux[0]->hijos[1] = aux[4];
    aux[1]->hijos[0] = aux[6];
    aux[2]->hijos[0] = aux[5];
    aux[4]->hijos[0] = aux[7];
    aux[4]->hijos[1] = aux[2];
    aux[5]->hijos[0] = aux[1];
    free(aux);

    imprime(raiz, 1);

    return 0;
}


