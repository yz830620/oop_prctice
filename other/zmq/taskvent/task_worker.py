# Task worker
# Connects PULL socket to tcp://localhost:5557
# Collects workloads from ventilator via that socket
# Connects PUSH socket to tcp://localhost:5558
# Sends results to sink via that socket
#
# Author: Lev Givon <lev(at)columbia(dot)edu>

import sys
import time
import zmq
import random

temperture = random.random()
if temperture > 0.5:
    delay = 0.01
    nature = "good worker"
else:
    delay = 0.5
    nature = "lazy worker"

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

counter = 1
# Process tasks forever
while True:
    message = str(receiver.recv().decode())
    task_nbr, s = (ele.strip() for ele in message.split(','))

    # Simple progress indicator for the viewer
    sys.stdout.write(f"I'm:{nature} task:{task_nbr} now!\nIt is my {counter} task\n->->->\n")
    sys.stdout.flush()

    # Do the work
    time.sleep(int(s)*0.001)
    counter += 1
    time.sleep(delay)

    # Send results to sink
    sender.send(f'{task_nbr}'.encode())