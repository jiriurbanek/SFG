set datafile separator ','
set terminal epslatex size 14cm, 9cm color colortext
set key bottom right
set xlabel '$\frac{1}{20000} t$'
set ylabel 'brightness'
set style line 1 lc rgb '#0060ad' lt 1 lw 0.3 pt 2 ps 0.1   # blue
set style line 2 lc rgb '#dd181f' lt 1 lw 0.3 pt 2 ps 0.1   # red
set output 'figures/circles.tex'
plot "circle-0.5.txt" w lp ls 1 title "$i = 0.5 \\pi$", "circle-0.47.txt" w lp ls 2 title "$i = 0.47 \\pi$"
set output 'figures/ellipse-circle-0.5.tex'
plot "circle-0.5.txt" w lp ls 1 title "sphere", "ellipse-0.5-1.2-0.8333-1.txt" w lp ls 2 title "ellipsoid"
set output 'figures/ellipse-ellipse-different-phase.tex'
plot "ellipse-0.5-1.2-0.8333-1-phi-0.5pi.txt" w lp ls 1 title "$\\alpha_0 = 0.5\\pi$", "ellipse-0.5-1.2-0.8333-1.txt" w lp ls 2 title "$\\alpha_0 = 0$"
set output 'figures/ellipse-ellipse-0.47-different-phase.tex'
plot "ellipse-0.47-1.2-0.8333-1-phi-0.5pi.txt" w lp ls 1 title "$\\alpha_0 = 0.5 \\pi$", "ellipse-0.47-1.2-0.8333-1.txt" w lp ls 2 title "$\\alpha_0 = 0$"
set output 'figures/ellipse-assymetrical.tex'
plot "ellipse-assymetrical.txt" w lp ls 1 title "asssymetrical view"
set output 'figures/realistic.tex'
plot "realistic.txt" w lp ls 1 title "realistic light curve"
