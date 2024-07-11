#!/usr/bin/env python3
import zmq
import time

pub_context = zmq.Context()
pub_socket = pub_context.socket(zmq.PUB)
pub_socket.connect("tcp://127.0.0.1:5556")

sub_context = zmq.Context()
sub_socket = sub_context.socket(zmq.SUB)
# accept all topics (prefixed) - default is none
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
sub_socket.bind("tcp://*:5555")

# Sleep a bit of time until the connection is properly established,
# otherwise some messages may be lost.
time.sleep(1)

try:
    file = open("time.txt", "a")
except:
    print("Error during file open")

for i in range(10000):
    message_to_send = "Hello Server!"
    print(str(i) + " - Publishing: " + message_to_send)
    start_time = time.time()
    pub_socket.send_string(message_to_send)
    message = sub_socket.recv_string()
    end_time = time.time()
    print("I heard: " + message)

    timer = round(float(end_time - start_time) * 1000000, 3)
    print("[TIME]: " + str(timer) + " microseconds")
    print("-------------------------------------")

    file.write(str(i) + " " + str(timer))
    file.write("\n")

file.close()