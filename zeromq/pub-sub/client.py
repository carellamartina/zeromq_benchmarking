#!/usr/bin/env python3
import zmq
import time

pub_context = zmq.Context()
pub_socket = pub_context.socket(zmq.PUB)
pub_socket.connect("tcp://127.0.0.1:5556")

sub_context = zmq.Context()
sub_socket = sub_context.socket(zmq.SUB)
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
sub_socket.bind("tcp://*:5555")

message_size = 0

# IMPORTANT
# Sleep a bit of time until the connection is properly established,
# otherwise some messages may be lost.
time.sleep(1)

try:
    file = open("time.txt", "a")
except:
    print("Error during file open")

for message_index in range(1500):
    message_to_send = ""
    message_size = message_size + 1000
    for index in range(message_size):
        message_to_send = message_to_send + "*"
    
    print("Publishing message number: " + str(message_index))
    start_time = time.time()
    pub_socket.send_string(message_to_send)
    message = sub_socket.recv_string()
    end_time = time.time()
    print("Response: received!")

    timer = round(float(end_time - start_time) * 1000000000, 3)
    print("[TIME]: " + str(timer) + " nanoseconds")
    print("-------------------------------------")

    file.write(str(message_size) + " " + str(timer))
    file.write("\n")

    # wait 50ms before send new message
    time.sleep(0.01)

file.close()