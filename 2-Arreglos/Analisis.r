#datos.txt

library(plyr)

#%Agregar,%Eliminar,Operaciones,NoEncontrados
d =read.csv('resultados.csv', sep =',', header = FALSE)


boxplot(d$V3 ~ d$V1)

boxplot(d$V4 ~ d$V1)