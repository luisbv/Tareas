#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define AGREGAR 1
#define ELIMINAR 2
#define CONSULTAR 3
#define SALIR 0
#define MAX 1001
#define DESDE 1
#define HASTA 9999
#define AUSENTE -1
#define DESOCUPADO -1
#define ELIMINADO -1

// Kernighan & Ritchie ANSI C



//#define MANUALTEST 40

#define SIMULATION 41


// #define IMPRIMIR 42
//#define DEBUG 43

int main(int argv, char** args){

    int* arreglo = NULL;
    int* nuevo = NULL;

    int largo = 0;
    int inicial = 8;
    
    float agregar = 0.0;
    float eliminar = 0.0;
    
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
    
    srand(time(NULL)* getpid());
    
    
    int a;
    a= atoi(args[2]);
    int operaciones = 0;
    int faltas = 0; //indicador de numero de faltas de elemento o no presente en arreglo
    agregar = (float)a/100;
    eliminar = 1 - agregar - 0.1;
    for (r=0; r < repeticiones; r++){
        posicion = AUSENTE;
        #ifdef SIMULATION
        s = rand() % MAX;
    
        if (s < agregar * MAX){
            accion = AGREGAR;
        }
        else if (s < (agregar + eliminar)*MAX){
            accion = ELIMINAR;
        }
        else{
            accion = CONSULTAR;
        }
    
        elemento = DESDE + rand() % (HASTA - DESDE + 1);
        #endif
    
        #ifdef MANUALTEST
        printf("\n\n");
        printf("Opciones: \n");
        printf("1. Agregar \n");
        printf("2. Eliminar \n");
        printf("3. Consultar \n");
        printf("0. Salir \n");
        printf("Elija la opcion deseada: ");
        scanf("%d", &accion);
    
    
        if (accion == SALIR){
            return 0;
        }
        #endif
    
        switch (accion) {
            case AGREGAR:
            
            
                #ifdef MANUALTEST
                printf("\n");
                printf("Elemento a agregar: ");
                scanf("%d", &elemento);
                #endif
            
                if (largo == 0){
                    operaciones++;
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
                    operaciones++;
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
    
                //printf("A %d (%d de %d)\n", elemento, posicion, largo);
                break;
            case ELIMINAR:
                #ifdef MANUALTEST
                printf("\n");
                printf("Elemento a eliminar: ");
                scanf("%d", &elemento);
                #endif
                if (largo != 0) {

                    for (p=0; p < largo; p++){
                        if(arreglo[p] == elemento){
                            posicion = p;
                            break;
                        }
                    }
                
                    if (posicion == AUSENTE) {
                        //printf("E %d ausente\n", elemento);
                        faltas++;
                    } else {
                        arreglo[posicion] = ELIMINADO;
                        //printf("E %d @ %d\n", elemento, posicion);
                    }
                
                    desocupados = 0;
                    for (p=0; p < largo; p++){
                        if(arreglo[p] == DESOCUPADO){
                            desocupados += 1;
                        }
                    }
                
                    // porcentaje de desocupados
                    pdesocupados = (float) desocupados / largo;
                
                    //printf("Porcentaje Desocupados: %.2f\n", pdesocupados);
                    if (pdesocupados > 0.75){
                    
                        //printf("Pocos elementos. Se redujo de (%d a %d)\n", largo, largo / 2);
                        int p1 = 0;
                        //quitarle tamanno
                        operaciones++;
                        nuevo = (int*)malloc(largo / 2 * sizeof(int));
                        for (p = 0; p < largo / 2; p++){
                            nuevo[p] = DESOCUPADO;
                        }
                    
                        p = 0;
                        p1 = 0;
                        while (p1 >= 0) {
                        
                            if (arreglo[p] != DESOCUPADO){
                                //printf("(Nuevo,%d), (Arreglo, %d)\n", p1, p);
                                nuevo[p1] = arreglo[p];
                                p++;
                                p1++;
                            }else{
                                p++;
                            }
                            if (p == largo){
                                break;
                            }
                        }
                    
                        free(arreglo);
                        arreglo = nuevo;
                        largo /= 2;
                    
                    }
                
                }else{
                    //printf("%d NO SE PUEDE ELIMINAR. No hay elementos en el arreglo.\n", elemento);
                    break;
                }
            
                break;
            default: //consultar
                #ifdef MANUALTEST
                printf("\n");
                printf("Elemento a consultar: ");
                scanf("%d", &elemento);
                #endif
                posicion = AUSENTE;
            
                if (largo == 0) {
                    //printf("%d NO SE PUEDE CONSULTAR. No hay elementos en el arreglo.\n", elemento);
                    break;
                }
            
                for (p=0; p < largo; p++){
                    if(arreglo[p] == elemento){
                        posicion = p;
                        break;
                    }
                }
            
    
                if (posicion == AUSENTE) {
                    //printf("C %d ausente\n", elemento);
                    faltas++;
                } else {
                    //printf("C %d @ %d\n", elemento, posicion);
                }
                break;
            }
            #ifdef DEBUG
                printf("D");
                if (largo <= 100){ //
                    for (p = 0; p<largo; p++){
                        printf(" %d ", arreglo[p]);
                    }
                    printf("\n");
                } else{
                    //printf(" Es muy grande para imprimir.\n");
                }
            #endif
    }
    printf("%.2f,%.2f,%d,%d\n",agregar,eliminar, operaciones,faltas);
    
    return 0;
}


