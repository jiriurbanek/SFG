set datafile separator ','
set terminal epslatex size 14cm, 9cm color colortext
set key bottom right
set xlabel 'time passed in terms of $\frac{1}{20000} t$'
set ylabel 'relative brightness'
set style line 1 lc rgb '#0060ad' lt 1 lw 0.3 pt 2 ps 0.1   # blue
set style line 2 lc rgb '#dd181f' lt 1 lw 0.3 pt 2 ps 0.1   # red
set output 'figures/circles.tex'
plot "circle-i-0.5-pi.txt" w lp ls 1 title "$i = 0.5 \\pi$", "circle-i-0.47-pi.txt" w lp ls 2 title "$i = 0.47 \\pi$"
set output 'figures/circle-and-ellipse-i-0.5pi-var-1.tex'
plot "circle-i-0.5-pi.txt" w lp ls 1 title "circle", "ellipse-i-0.5-a-1.2-b-1-c-0.8333333.txt" w lp ls 2 title "ellipse"
set output 'figures/circles-var-2.tex'
plot "circle-i-0.5-pi.txt" w lp ls 1 title "$i = 0.5 \\pi$", "circle-i-0.45-pi.txt" w lp ls 2 title "$i = 0.45 \\pi$"
set output 'figures/circle-and-ellipse-i-0.47.tex'
plot "circle-i-0.47-pi.txt" w lp ls 1 title "circle", "ellipse-i-0.47-a-1.2-b-1-c-0.8333333.txt" w lp ls 2 title "ellipse"
set output 'figures/ellipses.tex'
plot "ellipse-i-0.5-a-1.2-b-1-c-0.8333333.txt" w lp ls 1 title "$i = 0.5 \\pi$", "ellipse-i-0.45-a-1.2-b-1-c-0.8333333.txt" w lp ls 2 title "$i = 0.45 \\pi$"
set xlabel 'time passed $t^{\prime}$ in terms of $\frac{1}{200000}$ $t$ with 25 $t^{\prime}$ being at $\frac{50001}{200000}\ t$'
set output 'figures/realistic.tex'
plot "realistic-case.txt" w lp ls 1 title "realistic case"
