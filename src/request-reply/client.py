#!/usr/bin/env python3
import time
import zmq

client_context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
client = client_context.socket(zmq.REQ)
client.connect("tcp://localhost:5555")

#  Do a request about 100 MB of data
print(f"Sending request…")
sendig_time = time.time()
client.send(b"m" * 100_000_000)  # 100 MB of data
print(f"Sending message in {time.time() - sendig_time} seconds")

# Get the reply.
message = client.recv()
print(f"Received reply [ {message} ]")