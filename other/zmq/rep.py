import os
import zmq
import random
import time

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:7783")

print('Worker %s is running ...' % os.getpid())

while True:
    # receive request
    i, a, b = socket.recv_multipart()
    i = int(i)
    a = int(a)
    b = int(b)

    time.sleep(random.random())

    print(f'Compute {i}th request, {a} + {b} and send response')
    socket.send(str(a + b).encode())