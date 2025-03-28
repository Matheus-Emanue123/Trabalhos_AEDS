set datafile separator ","
set title "MinMax1"
set xlabel "Tamanho dos vetores"
set ylabel "Médias de tempo"
set xrange [0:500000]
set yrange [0:5000]
set grid

set term png size 1350, 950

set output "/home/matheus/Documents/CEFET/AEDS/AUXILIAR/AUXILIAR/TrabalhoMaxMin/PorFuncaoEstado/DatasetsMinMax1.png"
plot "Resultados_1.csv" using 1:2 with lp lw 3.0 lc 7 title "Vetor desordenado", \
     "Resultados_1.csv" using 3:4 with lines lw 3.0 title "Vetor ordenado crescente", \
     "Resultados_1.csv" using 5:6 with lines lw 3.0 title "Vetor ordenado decrescente"

set title "MinMax2"
set output "/home/matheus/Documents/CEFET/AEDS/AUXILIAR/AUXILIAR/TrabalhoMaxMin/PorFuncaoEstado/DatasetsMinMax2.png"
plot "Resultados_2.csv" using 1:2 with lp lw 3.0 lc 7 title "Vetor desordenado", \
     "Resultados_2.csv" using 3:4 with lines lw 3.0 title "Vetor ordenado crescente", \
     "Resultados_2.csv" using 5:6 with lines lw 3.0 title "Vetor ordenado decrescente"

set title "MinMax3"
set output "/home/matheus/Documents/CEFET/AEDS/AUXILIAR/AUXILIAR/TrabalhoMaxMin/PorFuncaoEstado/DatasetsMinMax3.png"
plot "Resultados_3.csv" using 1:2 with lp lw 3.0 lc 7 title "Vetor desordenado", \
     "Resultados_3.csv" using 3:4 with lines lw 3.0 title "Vetor ordenado crescente", \
     "Resultados_3.csv" using 5:6 with lines lw 3.0 title "Vetor ordenado decrescente"
