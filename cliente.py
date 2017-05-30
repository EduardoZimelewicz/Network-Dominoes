import socket 
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1234)
server_socket.connect(server_address)

while True:
	data = server_socket.recv(1024)
	print data
	message = raw_input("message:")
	server_socket.sendall(message)

server_socket.close()