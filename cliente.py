import socket 
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
server_socket.connect(server_address)

i = 0
pieces = []
tabuleiro = []
piecesA = 6
jogadas = 0

server_socket.send("ack")

while(i < 6):
	data = server_socket.recv(3)
	pieces.append(data)
	i = i + 1

server_socket.send('p')
qm_comeca = server_socket.recv(15)
print qm_comeca

server_socket.send('c')
jogo_comecou = int (server_socket.recv(1))

while (jogo_comecou):
	i = len(pieces)
	j = 0
	peca_escolh = 0
	print "Essas sao suas pecas: "
	for j in range(piecesA):
		print pieces[j] + " ",
	print ""
	
	if(i == 0):
		info = server_socket.recv(11)
		print info,
		jogo_comecou = False
	
	else:
		server_socket.send('j')
		joga = server_socket.recv(1)
		if(joga == '1'):
			server_socket.send('e')
			escolher_peca= server_socket.recv(27)
			peca_escolh = input(escolher_peca)
			peca_escolh = str(peca_escolh)
			server_socket.send(peca_escolh)
			peca_escolh = int(peca_escolh)
			
			if(peca_escolh != 6):
				server_socket.send('m')
				modo_peca = server_socket.recv(13)
				modo_escolh = raw_input(modo_peca)
				server_socket.send(modo_escolh)
				server_socket.send('p')
				ponta_peca = server_socket.recv(6)
				ponta_escolh = raw_input(ponta_peca)
				server_socket.send(ponta_escolh)
				pieces.pop(peca_escolh)
				piecesA = piecesA - 1
		
		server_socket.send('t')
		pecas_tab = server_socket.recv(1)
		pecas_tab = int(pecas_tab)
		
		if(peca_escolh != 6 and jogadas >= 0):
			print ""
			print ""
			tabuleiro[:] = []
			if(pecas_tab == 0):
				server_socket.send("tab")
				tabuleiro.append(server_socket.recv(3))
				print tabuleiro[0] + " ", 
			if(pecas_tab > 0):
				k = 0
				for k in range(pecas_tab):
					server_socket.send("tab")
					tabuleiro.append(server_socket.recv(3))
				j = 0
				for j in range(pecas_tab):
					print tabuleiro[j] + " ",
			print " "
			print " "
		
		server_socket.send('a')
		scoreA = int (server_socket.recv(1))
		server_socket.send('b')
		scoreB = int (server_socket.recv(1))
		
		if(scoreA >= 7):
			print "Team A wins! "
			jogo_comecou = False
		if(scoreB >= 7):
			print "Team B wins! "
			jogo_comecou = False
			
		jogadas = jogadas + 1
			
		print "Pontos Time A: " + str(scoreA)
		print "Pontos Time B: " + str(scoreB)

server_socket.close()