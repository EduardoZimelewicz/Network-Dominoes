import sys
import socket
from thread import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('', 1234))
server_socket.listen(5)

def clientthread(conn):
    conn.send('Bem vindo ao jogo Domino Mania. Estas sao suas pecas')
    
    while True:
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()

while True:
    conn, addr = server_socket.accept()

    print 'Conectado com ' + addr[0] + ':' + str(addr[1]) 
    start_new_thread(clientthread, (conn,))   
    
server_socket.close()

#run telnet localhost "port number" to view 




