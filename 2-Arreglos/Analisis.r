#datos.txt

library(plyr)
d =read.csv(“resultados.csv”, sep =“,”)

sink(“miresultado.txt”)
count(d, “facu”)
count(d, c(“facu”, “tipo”))

agregate (valor ~ facu, datos = d, sum)

sink()