set title 'ZeroMQ'
set xlabel 'messages'
set ylabel 'RTT (nanoseconds)'
set xrange [0:1500000]
set yrange [0:50000000]
set terminal png size 1920,1080
set output 'result.png';
plot 'time.txt' with lines