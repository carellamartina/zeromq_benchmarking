set title 'Benchmarking ZeroMQ vs ROS2 - 10ms'
set xlabel 'message size'
set ylabel 'RTT (nanoseconds)'
set xrange [0:1500000]
set yrange [0:40000000]
set terminal png size 1920,1080
set output 'result-10ms-ma.png';
plot "ros2_time_10ms.txt" using 1:2 title "ros2-10ms" with lines, \
    "zeromq_time_10ms.txt" using 1:2 title "zeromq-10ms" with lines