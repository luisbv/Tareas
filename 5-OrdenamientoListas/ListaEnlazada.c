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


void imprimeTodoReversa(lista* cual){
    elem* actual = cual->inicio;
    elem* temp = NULL;
    lista* reversa = (lista*)malloc(sizeof(lista));
    reversa->inicio = NULL;
    reversa->final = NULL;

    while (actual != NULL){
      temp = (elem*)malloc(sizeof(elem));
      temp->valor = actual->valor;
      temp->sig = NULL;
      
      agregarAlInicio(reversa, temp);
      actual = actual->sig;
    }
    free(temp);

    elem* actualr = reversa->inicio;
    printf("R = [");
    while (actualr != NULL){

        printf(" %d", actualr->valor);
        actualr = actualr->sig;
    }
    printf(" ]\n");
    free(reversa);
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
                printf(" %d en posicion %d\n", queCosa->valor, posicion);
                break;
            }
            actual = actual->sig;
	    posicion ++;
        }
	printf("El elemento %d no esta en la lista\n",queCosa->valor);
    }
}



void eliminarElemento(lista* alCual, elem* queCosa){
    if(alCual->inicio == NULL ){
        printf("No hay elementos en la lista para eliminar\n");
    }else{
	 //printf("ya esta alguien ahi\n");
        
        elem* actual = alCual->inicio;
	int posicion = 0;
        while (actual != NULL){
           
            if (actual->sig == NULL) {
	      printf("%d no esta en la lista\n",queCosa->valor);
	      break;
            }else if (actual->sig->valor == queCosa->valor){
	      printf("%d en pos %d\n", queCosa->valor, posicion+1);
	      actual->sig = actual->sig->sig;
	  
	      break;
	      
	     
	    }
            actual = actual->sig;
	    posicion ++;
        }
	
    }
}

void combinarListas(lista* lista1, lista* lista2, lista* listas){

  elem* actual1 = lista1->inicio;

  while (actual1 != NULL){
    agregarAlInicio(listas, actual1);
    actual1 = actual1->sig;
  }
  /*
  elem* actual2 = lista2->inicio;

  while (actual2 != NULL){
    agregarAlInicio(listas, actual2);
    actual2 = actual2->sig;
  }
  */

  //listas->inicio = lista1->inicio;
  
  //listas->final = lista1->final;
  
  //listas->final->sig = lista2->inicio;
  
  //listas->final = lista2->final;


  
  //free(lista1);
  //free(lista2);
}

void bubbleSort(lista* list){
  int c = -1;
  elem* actual = list->inicio;
  int temp = 0;
  while (c!=0){
    c = 0;
    //printf("Entro primer while\n");
    while (actual != NULL){
      //printf("Entro segundo while\n");
      //printf("%d\n",c);
      if(actual->sig == NULL){
	break;
	}
      if(actual->valor > actual->sig->valor){
	//printf("Entro if\n",c);
	temp = actual->sig->valor;
	actual->sig->valor = actual->valor;
	actual->valor = temp;
	c += 1;
      }
      actual = actual->sig;
    }
    
    //printf("Salio segundo while\n");
    //imprimeTodo(list);
    actual = list->inicio;
  }
}


void selectionSort(lista* list){
    elem* i = list->inicio;
    elem* m = list->inicio;
    elem* actual = list->inicio;
    int pos,k,p, temp=0;
    
  
    int menor;
    pos = 0;
    while (i != NULL){
    //while (i != NULL){
        k = 0;
        p = 0;
	
        //Encontrar el menor
        menor = 1000000;
        while (m != NULL){
            if(m->valor < menor){
                menor = m->valor;
                k = p;
            }
            m = m->sig;
            p++;
        }
        
            
        //Recorrer la lista hasta encontrar la posicion del menor
        pos = 0;
        while (pos < k){
            actual = actual->sig;
            pos++;
        }
    
        //intercambiar los valores entre k e i
        temp = actual->valor;
            
        actual->valor = i->valor;
        i->valor = temp;

	
        m = i->sig;
	actual = i->sig;
        i = i->sig;
        
    }
}


void mergeSort(lista* list){
    elem* i = list->inicio;
    elem* m = list->inicio;
    elem* actual = list->inicio;
    int pos,k,p, temp=0;
    
  
    int menor;
    pos = 0;
    while (i != NULL){
    //while (i != NULL){
        k = 0;
        p = 0;
	
        //Encontrar el menor
        menor = 1000000;
        while (m != NULL){
            if(m->valor < menor){
                menor = m->valor;
                k = p;
            }
            m = m->sig;
            p++;
        }
        
            
        //Recorrer la lista hasta encontrar la posicion del menor
        pos = 0;
        while (pos < k){
            actual = actual->sig;
            pos++;
        }
    
        //intercambiar los valores entre k e i
        temp = actual->valor;
            
        actual->valor = i->valor;
        i->valor = temp;

	
        m = i->sig;
	actual = i->sig;
        i = i->sig;
        
    }
}

int main(int argv, char** args){
    
    lista* l = (lista*)malloc(sizeof(lista));
  
    l->inicio = NULL;
    
    l->final = NULL;
  
    int r, repet = 30;
    
  
    elem* e = NULL;
    elem* t = NULL;
  
    
    srand(time(0));
    
    for (r = 0; r < repet;r++){

        e = (elem*)malloc(sizeof(elem));
    
        e->valor = 1 + rand() % MAXIMO;

        e->sig = NULL;
        if (r % 2 == 0) {
            printf("A %d Inicio. ", e->valor);
            agregarAlInicio(l,e);
            imprimeTodo(l);
        } else if (r % 3 == 0) {
            printf("A %d Final. ", e->valor);
            agregarAlFinal(l,e);
            imprimeTodo(l);
        } else if (r % 5 == 0){
            printf("A %d Orden. ", e->valor);
            //agregarOrden(l, e);
            imprimeTodo(l);
      
        } else if (r % 7 == 0){
            printf("B ", e->valor);
            buscarElemento(l, e);
        } else{
            printf("E ", e->valor);
            eliminarElemento(l,e);
        }
    }
    
    imprimeTodo(l);

    imprimeTodoReversa(l);

    //lista* l1 = (lista*)malloc(sizeof(lista));
    //l1->inicio = l->inicio;
    //l1->final = l->final;
 
  
    lista* juntas = (lista*)malloc(sizeof(lista));
    juntas->inicio = NULL;
    juntas->final = NULL;

    //printf("Combinar listas\n");
    //combinarListas(l,l,juntas);
    //imprimeTodo(juntas);
    printf("Lista ordenada (Selection Sort)\n");
    selectionSort(l);
    imprimeTodo(l);
    
    printf("Lista ordenada (Bubble Sort)\n");
    bubbleSort(l);
    imprimeTodo(l);
  
  
  
    return 0;
}


