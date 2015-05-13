set terminal postscript eps

set key off

set out "GraficaDes.eps"
plot "aristas.dat" using 1:2:3:4 with vectors filled nohead lw 1,\
    "nodos.dat" using 2:3 w p pt 7 ps 2, \
    "" using 2:3:1 w labels offset 0.75,0.75