import zmq
import random
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.bind("tcp://*:7783")

# wait all worker connected
time.sleep(1)

for i in range(100):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f'Compute {i}, element {a} + {b} ...')

    # send request to peer
    socket.send_multipart([str(i).encode(), str(a).encode(), str(b).encode()])
    
    # receive response from peer
    rep = socket.recv()
    print(' =', rep)
    time.sleep(0.3)