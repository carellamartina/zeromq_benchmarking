set title 'ROS2'
set xlabel 'messages'
set ylabel 'RTT (nanoseconds)'
set terminal png size 1920,1080
set output 'result.png';
plot 'time.txt' with lines