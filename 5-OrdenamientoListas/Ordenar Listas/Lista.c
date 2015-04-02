#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define AGREGAR 1
#define ELIMINAR 2
#define CONSULTAR 3
#define SALIR 0
#define MAX 101
#define DESDE 0
#define HASTA 100
#define AUSENTE -1
#define DESOCUPADO -1
#define ELIMINADO -1

// Kernighan & Ritchie ANSI C

//#define MANUALTEST 40

#define SIMULATION 41
#define MAXIMO 100

// #define IMPRIMIR 42
//#define DEBUG 43


void imprimir (int* arreglo, int l){
    int i;
    for (i=0; i < l; i++){
        
        if (arreglo[i] == DESOCUPADO){
            break;
        }
        printf("%d ",arreglo[i]);

    }
    printf("\n");
}

void imprimirTodo (int* arreglo, int l){
    int i;
    for (i=0; i < l; i++){
        printf("%d ",arreglo[i]);

    }
    printf("\n");
}


int* Juntar(int* lista1, int* lista2, int l1, int l2){
    int* juntas = NULL;
    int len;
    int i;
    len = l1 + l2;
    juntas = (int*)malloc(len*sizeof(int));
    for (i = 0; i < l1; i++){
        juntas[i] = lista1[i];
    }
    
    for (i = l1; i < len; i++){
        juntas[i] = lista2[i-l1];
    }
    return juntas;
}


void eliminar (int* lista, int l){
    int* nueva = NULL;
    int i;
    nueva = (int*)malloc((l-1)*sizeof(int));
    for (i=1; i < l; i++){
        nueva[i-1] = lista[i];
    }
    free(lista);
    lista = (int*)malloc((l-1)*sizeof(int));
    for (i=0; i < (l-1); i++){
        lista[i] = nueva[i];
    }
}

void agregarElemento (int* lista, int l, int elemento){
    lista = (int*)malloc((l+1)*sizeof(int));
    lista[l] = elemento;
}

void selSort(int* lista, int l){
    int menor;
    int k;
    int temp;
    int p, i;
    p = 0;
    temp = 0;
    for (i=0; i < l; i++){
        k=-2;
        menor = MAXIMO + 1;
        for (p = i; p < l; p++){
            if (lista[p] < menor){
                k = p;
                menor = lista[p];
            }
        }
        if (k != -2){
            temp = lista[i];
            lista[i] = lista[k];
            lista[k] = temp;
        }
    }
}


int* mergeSort(int* lista, int l){
    int mitad;
    int i, n, lenP, lenS;
    n = 0;
    int* nueva = NULL;
    int* nuevaP = NULL;
    int* nuevaS = NULL;
    int* primero = NULL;
    int* segundo = NULL;
    if (l < 2){
        return lista;
    }
    else{
        mitad = l/2;
        lenP = mitad;
        lenS = l-mitad;
        nuevaP = (int*)malloc(lenP * sizeof(int));
        for (i=0; i < mitad;i++){
            nuevaP[i] = lista[i];
        }
        primero = (int*)malloc(lenP * sizeof(int));
        primero = mergeSort(nuevaP, lenP);
        
        nuevaS = (int*)malloc(lenS * sizeof(int));
        for (i=mitad; i < l;i++){
            nuevaS[i-mitad] = lista[i];
        }
        segundo = (int*)malloc(lenS * sizeof(int));
        segundo = mergeSort(nuevaS, lenS);
        printf("Primero ");
        imprimir(primero, lenP);
        printf("Segundo ");
        imprimir(segundo, lenS);
        while (lenP > 0 || lenS > 0){
            printf("Entro While \n");
            if (lenP == 0){
                printf("Entro mitad == 0 \n");
                printf("Juntar ");
                imprimir(Juntar(nueva,segundo, n, lenS), n+lenS);
                return Juntar(nueva,segundo, n, lenS);
                
            }
            else if (lenS == 0){
                printf("Entro (l - mitad)== 0\n");
                printf("Juntar ");
                imprimir(Juntar(nueva,primero, n, lenP), n+lenP);
                return Juntar(nueva,primero, n, lenP);
            }
            else if (primero[0]<segundo[0]){
                printf("Entro primero < segundo");
                //agregarElemento(nueva, n, primero[0]);
                if (n == 0){
                    nueva = (int*)malloc((n+1)*sizeof(int));
                    nueva[n] = primero[0];
                }
                else{
                    nueva = (int*)realloc(nueva,(n+1)*sizeof(int));
                    nueva[n] = primero[0];
                }
                printf("nueva %d: %d primero %d\n",n,nueva[n], primero[0]);
                eliminar(primero, lenP);
                lenP--;
                n++;
            }
            else{
                printf("Entro segundo < primero ");
                //agregarElemento(nueva, n, segundo[0]);
                if (n == 0){
                    nueva = (int*)malloc((n+1)*sizeof(int));
                    nueva[n] = segundo[0];
                }
                else{
                    nueva = (int*)realloc(nueva,(n+1)*sizeof(int));
                    nueva[n] = segundo[0];
                }
                
                printf("nueva %d: %d segundo %d\n",n,nueva[n], segundo[0]);
                eliminar(segundo, lenS);
                lenS--;
                n++;
            }
            printf("Nueva ");
            imprimir(nueva, n);
        }
        return nueva;
    }
}



def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivote = lista[0]
        primero = list()
        segundo = list()
        for elemento in lista[1:]:
            if elemento <= pivote:
                primero.append(elemento)
            else:
                segundo.append(elemento)
        if len(primero) == 0:
            primero.append(pivote)
        elif len(segundo) == 0:
            segundo.append(pivote)
        else:
            primero.append(pivote)            
        primero = quicksort(primero)
        segundo = quicksort(segundo)
        return primero + segundo



void IndexQuickSort(int* lista, int desde, int hasta){
    int d, h, pivote, temp;
    if (hasta == desde){
        return;
    }
    d = desde;
    h = hasta;
    pivote = lista[d]; // hay que congelar esto por ahora
    desde += 1;
    while (desde < hasta){
        while (desde < hasta && lista[desde] < pivote){
            desde += 1;
        }
        while (desde < hasta && lista[hasta] >= pivote){
            hasta -= 1;
        }
        if (desde < hasta){
            temp = lista[desde];
            lista[desde] = lista[hasta];
            lista[hasta] = temp; // si pivote es el maximo (caso especial)
        }
    }
    if (lista[h] < pivote){
        temp = lista[d];
        lista[d] = lista[h];
        lista[h] = temp; //si pivote es el maximo (caso especial)
    }
    IndexQuickSort(lista, d, desde - 1);
    IndexQuickSort(lista, hasta, h);
    return;
}

int main(int argv, char** args){

    int* arreglo = NULL;
    int* nuevo = NULL;

    int largo = 0;
    int inicial = 8;
    
    float agregar = 1;
    float pdesocupados = 0.0; //porcentaje desocupados
    int accion = CONSULTAR;
    int p, s, r, repeticiones;
    // p posicion
    // s seleccion
    
    #ifdef SIMULATION
    repeticiones = atoi(args[1]);
    #endif
    
    #ifdef MANUALTEST
    printf("PRUEBA MANUAL\n");
    printf("Pruebas a realizar (muchas pruebas pueden ser tediosas) \n");
    scanf("%d", &repeticiones);
    #endif
    
    int elemento, posicion, desocupados;
    
    srand(time(0));
    
    for (r=0; r < repeticiones; r++){
        posicion = AUSENTE;
        elemento = rand() % (MAXIMO + 1);
        #ifdef MANUALTEST
        printf("\n\n");
        printf("Opciones: \n");
        printf("1. Agregar \n");
        printf("2. BubbleSort \n");
        printf("3. Selection \n");
        printf("0. Salir \n");
        printf("Elija la opcion deseada: ");
        scanf("%d", &accion);
        
        
        if (accion == SALIR){
            return 0;
        }
        #endif
        accion = AGREGAR;
        switch (accion) {
            case AGREGAR:
                #ifdef MANUALTEST
                printf("\n");
                printf("Elemento a agregar: ");
                scanf("%d", &elemento);
                #endif
                
                if (largo == 0){
                    arreglo = (int*)malloc(inicial * sizeof(int));
                    largo = inicial;
                    for (p=0; p < largo; p++){
                        arreglo[p] = DESOCUPADO;
                    }
                }
                for (p=0; p < largo; p++){
                    if (arreglo[p] == DESOCUPADO){
                        arreglo[p] = elemento;
                        posicion = p;
                        break;
                    }
                }
        
                if (largo > 0 && p == largo){ // no hubo desocupados
                    nuevo = (int*)malloc(2 * largo * sizeof(int));
                    for (p = 0; p < 2 * largo; p++){
                        nuevo[p] = arreglo[p];
                    }
                    nuevo[largo] = elemento;
                    posicion = largo;
                    for (p = largo + 1; p < 2 * largo; p++){
                        nuevo[p] = DESOCUPADO;
                    }
                    free(arreglo);
                    arreglo = nuevo;
                    largo *= 2;
                }
        
                break;
        }
}

    imprimir(arreglo,largo);
    IndexQuickSort(arreglo, 0, largo - 1);
    imprimir(arreglo,largo);
    //arreglo = mergeSort(arreglo, largo);
    //imprimir(arreglo,largo);
    //selSort(arreglo,largo);
    
    //imprimir(arreglo,largo);
    return 0;
}


