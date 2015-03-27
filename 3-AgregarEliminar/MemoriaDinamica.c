#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define AGREGAR 1
#define ELIMINAR 2
#define CONSULTAR 3
#define SALIR 0
#define MAX 101
#define DESDE 10
#define HASTA 99
#define AUSENTE -1
#define DESOCUPADO -1
#define ELIMINADO -1

// Kernighan & Ritchie ANSI C

//#define MANUALTEST 40

//#define SIMULATION 41

#define ANALISIS 42
//#define DEBUG 43

int main(int argv, char** args){

    int* arreglo = NULL;
    int* nuevo = NULL;

    int largo = 0;
    int inicial = 8;
    
    float agregar = 0.5;
    float eliminar = 0.5;
    
    float pdesocupados = 0.0; //porcentaje desocupados
    int accion = CONSULTAR;
    int p, s, r, repeticiones;
    // p posicion
    // s seleccion
    
    int c, e, t1, t2, t3;
    
    #ifdef ANALISIS
    int N = 100;
    // Operaciones
    int operaciones = 0;
    
    // Contados inserciones baratos
    int InsercionesBaratas = 0;
    
    // Contados inserciones caras
    int InsercionesCaras = 0;
    
    // Contados eliminaciones baratos
    int EliminacionesBaratas = 0;
    
    // Contados eliminaciones caras
    int EliminacionesCaras = 0;
    
    
    
    
    FILE *fp;
    /* open the file */
    fp = fopen("results.csv", "w");
    if (fp == NULL) {
        printf("I couldn't open results.dat for writing.\n");
        exit(0);
    }
    /* write to the file */
    fprintf(fp,"N,Operaciones,InsercionesBaratas,InsercionesCaras,EliminacionesBaratas,EliminacionesCaras\n");
    #endif
    
    #ifdef SIMULATION
    repeticiones = atoi(args[1]);
    #endif
    
    #ifdef ANALISIS
    repeticiones = atoi(args[1]);
    #endif
    
    #ifdef MANUALTEST
    printf("PRUEBA MANUAL\n");
    printf("Pruebas a realizar (muchas pruebas pueden ser tediosas) \n");
    scanf("%d", &repeticiones);
    #endif
    
    
    // Presupuesto
    int B = 100000;
    
    // Costo por operacion
    int CO = B/repeticiones;
    
    int CB = 1;
    
    int CC = 2 * CB;
    
    int ahorro = 0;
    
    int prestamo = 0;
    
    int elemento, posicion, desocupados, temp;
    
    srand(time(0));
    
    for (r = 0; r < repeticiones; r++){
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
        
        #ifdef ANALISIS
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
                    #ifdef ANALISIS
                    //printf("Inserciones Caras\n");
                    operaciones += 1;
                    InsercionesCaras += 1;
                    
                    prestamo = CO;
                    
                    #endif
                    arreglo = (int*)malloc(inicial * sizeof(int));
                    largo = inicial;
                    for (p=0; p < largo; p++){
                        arreglo[p] = DESOCUPADO;
                    }
                }
                for (p=0; p < largo; p++){
                    if (arreglo[p] == DESOCUPADO){
                        #ifdef ANALISIS
                        //printf("Inserciones Baratas\n");
                        operaciones += 1;
                        InsercionesBaratas += 1;
                        
                        
                        if (prestamo > 0){
                            if (ahorro > 0){
                                if (prestamo > ahorro){
                                    prestamo -= ahorro;
                                    ahorro = 0;
                                }else{
                                    ahorro -= prestamo;
                                    prestamo = 0;
                                    
                                }
                            }else{
                                prestamo += CB;
                            }
                            
                        }else{
                            if (ahorro > 0) {
                                ahorro -= CB;
                            }else{
                                ahorro += (CO-CB);
                            }
                        }
                        
                        #endif
                        arreglo[p] = elemento;
                        posicion = p;
                        break;
                    }
                }
        
                if (largo > 0 && p == largo){ // no hubo desocupados
                    #ifdef ANALISIS
                    //printf("Inserciones Caras\n");
                    operaciones += 1;
                    InsercionesCaras += 1;
                    
                    if (prestamo > 0){
                        if (ahorro > 0){
                            if (prestamo > ahorro){
                                prestamo -= ahorro;
                                ahorro = 0;
                            }else{
                                ahorro -= prestamo;
                                prestamo = 0;
                                
                            }
                        }else{
                            prestamo += CO;
                        }
                        
                    }else{
                        if (ahorro > 0){
                            if (ahorro > CO) {
                                ahorro -= CO;
                            }else{
                                temp= CO - ahorro;
                                ahorro = 0;
                                prestamo += temp;
                                
                            }
                        }else{
                            prestamo += CO;
                        }
                    }
                    
                    #endif
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
                #ifdef SIMULATION
                printf("A %d (%d de %d)\n", elemento, posicion, largo);
                #endif
                break;
            case ELIMINAR:
                #ifdef ANALISIS
                operaciones += 1;
                #endif
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
                        #ifdef SIMULATION
                        printf("E %d ausente\n", elemento);
                        #endif
                    } else {
                        #ifdef ANALISIS
                        //printf("Eliminaciones Baratas\n");
                        operaciones += 1;
                        EliminacionesBaratas += 1;
                        
                        
                        
                        if (prestamo > 0){
                            if (ahorro > 0){
                                if (prestamo > ahorro){
                                    prestamo -= ahorro;
                                    ahorro = 0;
                                }else{
                                    ahorro -= prestamo;
                                    prestamo = 0;
                                    
                                }
                            }else{
                                prestamo += CB;
                            }
                            
                        }else{
                            if (ahorro > 0) {
                                ahorro -= CB;
                            }else{
                                ahorro += (CO-CB);
                            }
                        }
                        #endif
                        arreglo[posicion] = ELIMINADO;
                        #ifdef SIMULATION
                        printf("E %d @ %d\n", elemento, posicion);
                        #endif
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
                        #ifdef SIMULATION
                        printf("Pocos elementos. Se redujo de (%d a %d)\n", largo, largo / 2);
                        #endif
                        int p1 = 0;
                        //quitarle tamanno
                        #ifdef ANALISIS
                        //printf("Eliminaciones Caras\n");
                        operaciones += 1;
                        EliminacionesCaras += 1;
                        
                        
                        if (prestamo > 0){
                            if (ahorro > 0){
                                if (prestamo > ahorro){
                                    prestamo -= ahorro;
                                    ahorro = 0;
                                }else{
                                    ahorro -= prestamo;
                                    prestamo = 0;
                                    
                                }
                            }else{
                                prestamo += CO;
                            }
                            
                        }else{
                            if (ahorro > 0){
                                if (ahorro > CO) {
                                    ahorro -= CO;
                                }else{
                                    temp= CO - ahorro;
                                    ahorro = 0;
                                    prestamo += temp;
                                    
                                }
                            }else{
                                prestamo += CO;
                            }
                        }
                        #endif
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
                    #ifdef SIMULATION
                    printf("%d NO SE PUEDE ELIMINAR. No hay elementos en el arreglo.\n", elemento);
                    #endif
                    break;
                }
                
                break;
            default: //consultar
                #ifdef ANALISIS
                operaciones += 1;
                #endif
                #ifdef MANUALTEST
                printf("\n");
                printf("Elemento a consultar: ");
                scanf("%d", &elemento);
                #endif
                posicion = AUSENTE;
                
                if (largo == 0) {
                    #ifdef SIMULATION
                    printf("%d NO SE PUEDE CONSULTAR. No hay elementos en el arreglo.\n", elemento);
                    #endif
                    break;
                }
                
                for (p=0; p < largo; p++){
                    if(arreglo[p] == elemento){
                        posicion = p;
                        break;
                    }
                }
                
                if (posicion == AUSENTE) {
                    #ifdef SIMULATION
                    printf("C %d ausente\n", elemento);
                    #endif
                } else {
                    #ifdef SIMULATION
                    printf("C %d @ %d\n", elemento, posicion);
                    #endif
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
                    printf(" Es muy grande para imprimir.\n");
                }
            #endif
        
        #ifdef ANALISIS
        //printf("Agregar en Archivo\n");
        /* write to the file */
        fprintf(fp,"%d,%d,%d,%d,%d,%d\n", r, operaciones, InsercionesBaratas, InsercionesCaras, EliminacionesBaratas, EliminacionesCaras);
        #endif
        
        
    }
    

    #ifdef ANALISIS
    printf("Presupuesto: %d, Ahorro: %d, Prestamo: %d\n", B,ahorro,prestamo);
    /* close the file */
    fclose(fp);
    #endif
    return 0;
}


