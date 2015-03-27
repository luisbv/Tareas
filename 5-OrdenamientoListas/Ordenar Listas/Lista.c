#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define AGREGAR 1
#define ELIMINAR 2
#define CONSULTAR 3
#define SALIR 0
#define MAX 101
#define DESDE 0
#define HASTA 9
#define AUSENTE -1
#define DESOCUPADO -1
#define ELIMINADO -1

// Kernighan & Ritchie ANSI C



//#define MANUALTEST 40

#define SIMULATION 41
#define MAXIMO 10

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

void imprimir (int* arreglo, int* l){
    int i;
    int j=0;
    for (i=0; i < l; i++){
        
        if (arreglo[i] == DESOCUPADO){
            break;
        }
        printf("%d ",arreglo[i]);

    }
    printf("\n");
}

void selSort(int* arreglo, int l){
    int menor;
    int k;
    int temp=0;
    int p, i;
    for (i=0; i<l; i++){
        k=-2;
        menor = MAXIMO + 1;
        for (p=i; p<l;p++){
            if (arreglo[p]<menor){
                k = p;
                menor = arreglo[p];
            }
        if (k != -2){
            temp = arreglo[i];
            arreglo[i] = arreglo[k];
            arreglo[k] = temp;
        }
        }
    }
}


int* mergeSort(int* arreglo, int l){
    int mitad;
    int* nueva = NULL;
    int* primero = NULL;
    int* segundo = NULL;
    nueva = (int*)malloc(sizeof(int))
    nu
    if l < 2{
        return arreglo;
    }
    else{
        mitad = l/2;
        primero = mergeSort(arreglo[0])
        while()
        
    }
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
    selSort(arreglo,largo);
    imprimir(arreglo,largo);
    return 0;
}


