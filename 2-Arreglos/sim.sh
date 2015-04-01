#!/bin/bash


rm *.csv
N=10000
R=100
gcc MemoriaDinamica.c

for ((i=10; i <= 90; i += 1))
do
    for ((r=1; r <= R; r += 1))
    do
        ./a.out $N $i >>resultados.csv
    done
done
