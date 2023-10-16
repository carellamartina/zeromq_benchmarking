#!/usr/bin/env python3
import time
import zmq

server_context = zmq.Context()
server = server_context.socket(zmq.REP)
server.bind("tcp://*:5555")

arrival_time = time.time()
#  Wait for next request from client
message = server.recv()
print(f"Received request in {time.time() - arrival_time} seconds")

#  Send reply back to client
server.send(b"World")