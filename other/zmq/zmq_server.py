import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind('tcp://*:1234')

print(socket.recv())
socket.send_string('baby')