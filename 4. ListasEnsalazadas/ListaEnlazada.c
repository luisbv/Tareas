#include <stdio.h> // imprimir
#include <math.h> // inicializar pseudoaleatorio
#include <stdlib.h> // malloc & free

#define MAXIMO 100

struct elemento {
    int valor;
    struct elemento* sig;
};


struct listaEnlazada {
    struct elemento* inicio;
    struct elemento* final;
};

typedef struct elemento elem;
typedef struct listaEnlazada lista;


void imprimeTodo(lista* cual){
    elem* actual = cual->inicio;
    printf("L = [");
    while (actual != NULL){
        printf(" %d", actual->valor);
        actual = actual->sig;
    }
    printf(" ]\n");
}


void agregarAlInicio(lista* alCual, elem* queCosa){
    if(alCual->inicio == NULL ){
        //printf("aun no hay nadie\n");
        alCual->inicio = queCosa;
        alCual->final = queCosa;
    }else{
        //printf("ya esta alguien ahi\n");
        queCosa->sig = alCual->inicio;
        alCual->inicio = queCosa;
    }
}


void agregarAlFinal(lista* alCual, elem* queCosa){
    if(alCual->inicio == NULL ){
        //printf("aun no hay nadie\n");
        alCual->inicio = queCosa;
        alCual->final = queCosa;
    }else{
        //printf("ya esta alguien ahi\n");
        alCual->final->sig = queCosa;
        alCual->final = queCosa;
    }
}




void agregarOrden(lista* alCual, elem* queCosa){
    if(alCual->inicio == NULL ){
        //printf("aun no hay nadie\n");
        alCual->inicio = queCosa;
        alCual->final = queCosa;
    }else{
        //printf("ya esta alguien ahi\n");
        elem* temp = NULL;
        elem* actual = alCual->inicio;
        while (actual != NULL){
            //printf("Actual: %d\n",actual->valor);
            if (actual->sig->valor > queCosa->valor) {
                //Si funciona pero se inserta uno despues
                printf("Agrego %d entre %d y %d\n", queCosa->valor, actual->valor, actual->sig->valor);
                temp = actual->sig;
                
                actual->sig = queCosa;
                actual->sig->sig = temp;
                
                
                break;
            }
            actual = actual->sig;
        }

    }
}



void buscarElemento(lista* alCual, elem* queCosa){
    if(alCual->inicio == NULL ){
        printf("No hay elementos en la lista para buscar\n");
    }else{
	 //printf("ya esta alguien ahi\n");
        elem* temp = NULL;
        elem* actual = alCual->inicio;
	int posicion = 0;
        while (actual != NULL){
            //printf("Actual: %d\n",actual->valor);
            if (actual->valor == queCosa->valor) {
                printf("Elemento %d en posicion %d\n", queCosa->valor, posicion);
                break;
            }
            actual = actual->sig;
	    posicion ++;
        }
    }
}




int main(int argv, char** args){
    
    lista* l = (lista*)malloc(sizeof(lista));;
    
    l->inicio = NULL;
    
    l->final = NULL;
    
    int r, repet = 20;
    
    
    elem* e = NULL;
    elem* t = NULL;
    
    
    srand(time(0));
    
    for (r = 0; r < repet;r++){

        e = (elem*)malloc(sizeof(elem));
    
        //e->valor = 1 + rand() % MAXIMO;
        e->valor = r;
        e->sig = NULL;
        if (r % 2 == 0) {
            //printf("Agrego inicio\n");
            //agregarAlInicio(l,e);
        } else {
            printf("Agrego final\n");
            agregarAlFinal(l,e);
            imprimeTodo(l);
        }
        
        
        
    }
    
    
    e = (elem*)malloc(sizeof(elem));
    
    e->valor = 2;
    e->sig = NULL;
    
    printf("Agregar en orden: %d\n", e->valor);
    agregarOrden(l, e);
    
    imprimeTodo(l);
    
    
    e = (elem*)malloc(sizeof(elem));
    
    e->valor = 10;
    e->sig = NULL;
    
    printf("Agregar en orden: %d\n", e->valor);
    agregarOrden(l, e);

    e = (elem*)malloc(sizeof(elem));
    
    e->valor = 10;
    e->sig = NULL;
     
    
    buscarElemento(l,e);

    imprimeTodo(l);
    
    return 0;
}


