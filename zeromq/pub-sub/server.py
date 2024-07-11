#!/usr/bin/env python3
import zmq

sub_context = zmq.Context()
sub_socket = sub_context.socket(zmq.SUB)
# accept all topics (prefixed) - default is none
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
sub_socket.bind("tcp://*:5556")

pub_context = zmq.Context()
pub_socket = pub_context.socket(zmq.PUB)
pub_socket.connect("tcp://127.0.0.1:5555")

while True:
    message = sub_socket.recv_string()
    print("I heard: " + message)
    print("Publishing: " + message)
    pub_socket.send_string(message)