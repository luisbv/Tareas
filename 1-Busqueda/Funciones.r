

graficaCajas = function(datos){
	#Grafica para f
	postscript("Operaciones.eps")
	boxplot(datos, main = "Operaciones vs N",  ylab ="Operaciones", xlab ="N")
	dev.off()
	
}

datos = read.csv("Permutaciones.csv",sep=",", header=FALSE)

colnames(datos) = seq(1,ncol(datos),1)
postscript("OperacionesPromedio.eps")
plot(colMeans(datos), main = "Operaciones Promedio vs N",  ylab ="Operaciones Promedio", xlab ="N")
dev.off()

graficaCajas(datos)


datos1 = read.csv("PermutacionesTotales.csv",sep=",", header=FALSE)

colnames(datos1) = seq(1,ncol(datos1),1)
postscript("OperacionesTotalesPromedio.eps")
plot(colMeans(datos1), main = "Operaciones Promedio vs N",  ylab ="Operaciones Promedio", xlab ="N")
dev.off()

postscript("OperacionesTotales.eps")
	boxplot(datos1, main = "Operaciones vs N",  ylab ="Operaciones", xlab ="N")
	dev.off()