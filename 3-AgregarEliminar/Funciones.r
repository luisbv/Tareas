
combinacionMinima = function(datos){
	library(plyr)
	tablaMedia = aggregate(PasosError~f+v,data=datos,mean)
	minimoValor = min(tablaMedia$PasosError)

	return(tablaMedia[tablaMedia$PasosError == minimoValor,])

	#tablaWhich = aggregate(PasosError ~ f + v,data = datos, which.min)
	#datos$Cual = tablaWhich$PasosError	
}

mapaCalor = function(datos, size=9,inicio=1,step=1/10){
	library(plyr)
	library(lattice)
	#Agregar en la columna PasosError la media de las 25 repeticiones
	tablaMedia = aggregate(PasosError~f+v,data=datos,mean)
	
	matrizMedia = matrix(tablaMedia$PasosError, nrow=size, ncol=size) 
	colnames(matrizMedia) <- seq(inicio*step, size*step, by=step)
	rownames(matrizMedia) <- seq(inicio*step, size*step, by=step)
	
	levelplot(t(matrizMedia),
	col.regions=gray(0:100/100),#heat.colors,
	xlab = "f",
	ylab = "v",
	main = "Pasos / %Error")
	
}

MatrizMediaPasosError = function(datos, size=9,inicio=1,step=1/10){
	library(plyr)
	#Agregar en la columna PasosError la media de las 25 repeticiones
	tablaMedia = aggregate(PasosError~f+v,data=datos,mean)
	
	matrizMedia = matrix(tablaMedia$PasosError, nrow=size, ncol=size) 
	matrizMedia = t(matrizMedia)
	#sink("PasosError.txt")
	write.table(matrizMedia, file = "PasosError.txt", sep = " ", row.names = FALSE, col.names = FALSE)

	#print.matrix(matrizMedia)
	#sink()
	
}

graficaCajas = function(datos){
	#Grafica para f
	boxplot(datos$PasosError~datos$f)
	
	#Grafica para v
	boxplot(datos$PasosError~datos$v)
}

