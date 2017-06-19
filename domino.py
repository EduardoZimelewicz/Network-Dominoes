#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import socket
from thread import *
import random

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(('',1234))
s_socket.listen(4)
	
pieces = ["0|0", "1|0", "1|1", "2|0", "2|1", "2|2", "3|0", "3|1", "3|2",
 "3|3", "4|0", "4|1", "4|2", "4|3", "4|4", "5|0", "5|1", "5|2", "5|3", 
 "5|4", "5|5", "6|0", "6|1", "6|2", "6|3", "6|4", "6|5", "6|6"]

player_A1 = []
player_A2 = []
player_B1 = []
player_B2 = []
players = []
clientes = []

jogadores = 0
while (jogadores < 4):
	conn, addr = s_socket.accept()
	clientes.append(conn)
	jogadores = jogadores + 1

players.append(player_A1)
players.append(player_A2)
players.append(player_B1)
players.append(player_B2)

#Distribuição das peças aos jogadores
n = 1
p = 0
while (n < 25):
	for m in range(4):
		while(pieces[p] == ""):
			p = random.randint(0, 27)
		if(pieces[p] != ""):
			players[m].append(pieces[p])
			pieces[p] = ""
			n = n + 1

acks = 0
while(acks < 4):
	data = clientes[acks].recv(3)
	if(data == "ack"):
		acks = acks + 1

p = 0
jo = 0
for jo in range(4):
	for p in range(6):
		MESSAGE = players[jo][p]
		clientes[jo].send(MESSAGE)

		
pieces = ["0|0", "1|0", "1|1", "2|0", "2|1", "2|2", "3|0", "3|1", "3|2",
 "3|3", "4|0", "4|1", "4|2", "4|3", "4|4", "5|0", "5|1", "5|2", "5|3", 
 "5|4", "5|5", "6|0", "6|1", "6|2", "6|3", "6|4", "6|5", "6|6"]
 
pieces_equal = ["0|0", "1|1", "2|2", "3|3", "4|4", "5|5", "6|6"]

#Escolha do primeiro jogador
peca = 0
escolhido = False
qm_comeca = 0
while (peca < 7):
	for i in range(4):
		for j in range(6):
			if(peca == 0):
				if(players[i][j] == pieces[27]):
					escolhido = True
			if(peca == 1):
				if(players[i][j] == pieces[20]):
					escolhido = True
			if(peca == 2):
				if(players[i][j] == pieces[14]):
					escolhido = True
			if(peca == 3):
				if(players[i][j] == pieces[9]):
					escolhido = True
			if(peca == 4):
				if(players[i][j] == pieces[5]):
					escolhido = True
			if(peca == 5):
				if(players[i][j] == pieces[2]):
					escolhido = True
			if(peca == 6):
				if(players[i][j] == pieces[0]):
					escolhido = True
			if(escolhido == True):
				for jo in range(4):
					data = clientes[jo].recv(1)
					if(data == 'p'):
						MESSAGE = "player " + str(i) + " begins"
						clientes[jo].send(MESSAGE)
				qm_comeca = i
				break
		if(escolhido == True):
			break
		
	if(escolhido == False):
		peca = peca + 1
	else:
		peca = 7
	
teamA_score = 0
teamB_score = 0
#time A: jogador 0 e jogador 2
#time B: jogador 1 e jogador 3

#Inicio do jogo
jogo_comecou = True

jogadas = 0
peca_jog = 0
mod_jog = ""
ponta_tab = ""
peca2 = ""
peca3 = ""
pecas_tab = 0
tabuleiro = []
modo_tabuleiro = []

for jo in range(4):
	data = clientes[jo].recv(1)
	if(data == 'c'):
		clientes[jo].send('1')

while(jogo_comecou):
	#print "player " + str(qm_comeca) + " pieces"
	
	j = 0
	p = len(players[qm_comeca])
	
	if(p == 0):
		jo = 0
		if(qm_comeca == 0 or qm_comeca == 2):
			for jo in range(4):
				clientes[jo].send("Team A wins!")
		if(qm_comeca == 1 or qm_comeca == 3):
			for jo in range(4):
				clientes[jo].send("Team B wins!")
		jogo_comecou = False
		
	else:
		j = 0
		for j in range(4):
			data = clientes[j].recv(1)
			if(data == 'j'):
				if(j == qm_comeca):
					clientes[j].send('1')
				else:
					clientes[j].send('0')
		
		data = clientes[qm_comeca].recv(1)
		if(data == 'e'):
			clientes[qm_comeca].send("Voce joga, escolha a peca:")
			peca_jog = int(clientes[qm_comeca].recv(1))
		
		if(peca_jog != 6):
			data = clientes[qm_comeca].recv(1)
			if(data == 'm'):
				clientes[qm_comeca].send("modo da peca:")
				modo_jog = clientes[qm_comeca].recv(1) #Colocar na pos normal ou invertida
			data = clientes[qm_comeca].recv(1)
			if(data == 'p'):
				clientes[qm_comeca].send("ponta:")
				ponta_tab = clientes[qm_comeca].recv(1)#Colocar na ponta esq ou dir
			peca = players[qm_comeca][peca_jog]
			
			if(jogadas > 0):
				peca2 = tabuleiro[pecas_tab - 1]
			
			if(len(tabuleiro) >= 2):
				peca3 = tabuleiro[0]
			
			#Se a peça tiver lados iguais
			if (peca in pieces_equal):
				#Se a peça servir nos dois lados 
				if(peca[:1] in peca2 and peca[:1] in peca3):
					if(qm_comeca == 0 or qm_comeca == 2):
						teamA_score = teamA_score + 4
					if(qm_comeca == 1 or qm_comeca == 3):
						teamB_score = teamB_score + 4
				else:
					if(qm_comeca == 0 or qm_comeca == 2):
						teamA_score = teamA_score + 2
					if(qm_comeca == 1 or qm_comeca == 3):
						teamB_score = teamB_score + 2
			
			#Se a peça tiver um lado igual a ponta da direita
			elif((peca[:1] in peca2 or peca[2:] in peca2) or (peca[:1] in peca3 or peca[2:] in peca3)):
				#Se a peça tiver o lado dir igual a ponta esq e o lado esq igual a ponta dir
				#Ou se a peça tiver o lado esq igual a ponta esq e o lado dir igual a ponta dir 
				if((peca[:1] in peca2 and peca[2:] in peca3) or (peca[:1] in peca3 and peca[2:] in peca2)):
					print peca 
					if(qm_comeca == 0 or qm_comeca == 2):
						teamA_score = teamA_score + 3
					if(qm_comeca == 1 or qm_comeca == 3):
						teamB_score = teamB_score + 3
				else:
					if(qm_comeca == 0 or qm_comeca == 2):
						teamA_score = teamA_score + 1
					if(qm_comeca == 1 or qm_comeca == 3):
						teamB_score = teamB_score + 1
			
			#Colocar na ponta esq ou direita do tabuleiro
			if(ponta_tab == 'd'):
				if(modo_jog == 'n'):
					tabuleiro.append(peca)
				if(modo_jog == 'i'):
					tabuleiro.append(peca[::-1])
				#modo_tabuleiro.append(modo_jog)
			if(ponta_tab == 'e'):
				if(modo_jog == 'n'):
					tabuleiro.insert(0, peca)
				if(modo_jog == 'i'):
					tabuleiro.insert(0, peca[::-1])
				#modo_tabuleiro.insert(0, modo_jog)
			
			pecas_tab = pecas_tab + 1
			
			players[qm_comeca].pop(peca_jog)
		
		pecas_tab1 = str(pecas_tab)
		jo = 0
		for jo in range(4):
			data = clientes[jo].recv(1)
			if(data == 't'):
				clientes[jo].send(pecas_tab1)
		
		if(jogadas == 0):
			jo = 0
			for jo in range(4):
				data = clientes[jo].recv(3)
				if(data == "tab"):
					clientes[jo].send(tabuleiro[0])
		
		elif(jogadas >= 1):
			jo = 0
			for jo in range(4):
				i = 0
				for i in range(pecas_tab):
					data = clientes[jo].recv(3)
					if(data == "tab"):
						clientes[jo].send(tabuleiro[i])
		
		jo = 0
		for jo in range(4):
			data = clientes[jo].recv(1)
			if(data == 'a'):
				clientes[jo].send(str(teamA_score))
		jo = 0
		for jo in range(4):
			data = clientes[jo].recv(1)
			if(data == 'b'):
				clientes[jo].send(str(teamB_score))
		
		print "A:" + str(teamA_score)
		print "B:" + str(teamB_score)
		
		jogadas = jogadas + 1
		qm_comeca = qm_comeca + 1
		
		#Contador atingiu o máx de jog, recomeça o jogo
		if(qm_comeca == 4):
			qm_comeca = 0
		
		if(teamA_score >= 7):
			#for jo in range(4):
				#clientes[jo].send("Team A wins!")
			jogo_comecou = False
		elif(teamB_score >= 7):
			#for jo in range(4):
				#clientes[jo].send("Team B wins!")
			jogo_comecou = False

s_socket.close()
	


