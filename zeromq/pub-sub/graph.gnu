set title 'Time'
set xlabel 'messages'
set ylabel 'microseconds'
set yrange [ * : 5000 ]
set terminal png size 1200,768
set output 'result.png';
plot 'time.txt' with lines