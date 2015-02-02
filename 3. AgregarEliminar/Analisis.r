source("Funciones.r")

#Lectura de datos simulados
#Columnas:
#Iteracion,f,v,Pasos,PorcentajeError,PasosMejor,ErrorPasos
datos = read.csv("results.csv",sep=",", header=TRUE)

plot(range(min(datos$N):max(datos$N)), range(min(datos$Operaciones):max(datos$Operaciones)), type='n', ylab = "Operaciones", xlab = "N")
points(datos$Operaciones~datos$N,col="red", pch=15, cex=.5)
fit = lm(datos$Operaciones~datos$N)
b = coef(fit)[1]
a = coef(fit)[2]
r2 = summary(fit)$r.squared
abline(lm(datos$Operaciones~datos$N))

# add text to plot with legend() for convenient placement
legend('topleft', legend=sprintf("y = %3.2fx %+3.2f, R\UB2 = %3.2f", a, b, r2), bty='n', cex=1)




plot(range(min(datos$N):max(datos$N)), range(0:max(datos$InsercionesBaratas)), type='n', ylab = "Operaciones", xlab = "N")
lines(datos$InsercionesBaratas~datos$N, type="l", col="red")
lines(datos$InsercionesCaras~datos$N, type="l", col="blue")

#plot(range(min(datos$N):max(datos$N)), range(0:max(datos$EliminacionesBaratas)), type='n', ylab = "Operaciones", xlab = "N")
lines(datos$EliminacionesBaratas~datos$N, type="l", col="orange")
lines(datos$EliminacionesCaras~datos$N, type="l", col="green")

legend('topleft',c("I Baratas", "I Caras","E Baratas","E Caras"),lty=1,col=c("red","blue","orange","green"), bty="n", cex=.75) # gives the legend lines the correct color and width