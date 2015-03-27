#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define AGREGAR 1
#define ELIMINAR 2
#define CONSULTAR 3
#define MAX 101
#define DESDE 10
#define HASTA 99

#define DISPONIBLE -1
#define CUPO 8


// Kernighan & Ritchie ANSI C
//claves y producir indices del arreglo
//si tengo 10 posiciones me da de 0 a 9
//capacidad
int hash(int algo){
    return algo % CUPO;
}

typedef struct Alumno {
  int matricula;
} alumno;



int main(int argv, char** args){
    //int H[CUPO];
    alumno H[CUPO]; 
    float agregar = 0.5;
    float eliminar = 0.3;
    
    float pdesocupados = 0.0; //porcentaje desocupados
    int accion = CONSULTAR;
    int h, i, p, s, r, repeticiones;
    // p posicion
    // s seleccion
    

    repeticiones = atoi(args[1]);

    int elemento, posicion, desocupados;
    
    srand(time(0));
    
    int algo;

    for (i = 0; i < CUPO; i++){
        //H[i] = DISPONIBLE;
        H[i].matricula = DISPONIBLE;
    }

    for (r=0; r < repeticiones; r++){
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
        
        //h = hash(s);
        h = hash(s);
        switch (accion) {
            case AGREGAR:
                //if (H[h] == DISPONIBLE){
                if (H[h].matricula == DISPONIBLE){
                    //H[h].matricula = s ;
                    H[h].matricula = s ;
                    printf("%d colocado con hash %d\n", H[h], h);
                } else {
                    printf("hash %d ocupado, %d no entra\n", h, s);
                }
                break;
            case ELIMINAR:
                //H[h] = DISPONIBLE;
                H[h].matricula = DISPONIBLE;
                break;
            default: //consultar
                if (H[h].matricula == DISPONIBLE){
                    printf("%d ausente\n", s);
                } else {
                    printf("presente: %d con hash %d\n", H[h], h);
                }
                break;
            }
    }
    return 0;
}


