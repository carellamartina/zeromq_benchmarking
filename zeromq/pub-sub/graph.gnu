set title 'ZeroMQ'
set xlabel 'messages'
set ylabel 'RTT (microseconds)'
set terminal png size 1920,1080
set output 'result.png';
plot 'time.txt' with lines