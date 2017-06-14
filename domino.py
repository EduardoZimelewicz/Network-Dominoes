#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import random
import itertools

pieces = ["0|0", "1|0", "1|1", "2|0", "2|1", "2|2", "3|0", "3|1", "3|2",
 "3|3", "4|0", "4|1", "4|2", "4|3", "4|4", "5|0", "5|1", "5|2", "5|3", 
 "5|4", "5|5", "6|0", "6|1", "6|2", "6|3", "6|4", "6|5", "6|6"]

player_A1 = []
player_A2 = []
player_B1 = []
player_B2 = []
players = []

players.append(player_A1)
players.append(player_A2)
players.append(player_B1)
players.append(player_B2)

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

'''			
for i in range(4):
	print "player " + str(i) + " pieces:"
	for j in range(6):
		print players[i][j]
'''
		
pieces = ["0|0", "1|0", "1|1", "2|0", "2|1", "2|2", "3|0", "3|1", "3|2",
 "3|3", "4|0", "4|1", "4|2", "4|3", "4|4", "5|0", "5|1", "5|2", "5|3", 
 "5|4", "5|5", "6|0", "6|1", "6|2", "6|3", "6|4", "6|5", "6|6"]
 
pieces_equal = ["0|0", "1|1", "2|2", "3|3", "4|4", "5|5", "6|6"]

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
				print "player " + str(i) + " begins"
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
teamA = [players[0], players[2]]
teamB = [players[1], players[3]]
	
jogo_comecou = True
jogadas = 0
peca_jog = 0
mod_jog = ""
peca2 = ""
pecas_tab = 0
tabuleiro = []
modo_tabuleiro = []
while(jogo_comecou):
	print "player " + str(qm_comeca) + " pieces"
	
	j = 0
	p = len(players[qm_comeca])
	for j in range(0, p):
		print players[qm_comeca][j] + " ",
	peca_jog = input("piece to play: ")
	
	if(peca_jog != 11):
		modo_jog = raw_input("modo da peca: ")
		peca = players[qm_comeca][peca_jog]
		if(jogadas > 0):
			peca2 = tabuleiro[pecas_tab - 1]
		if (peca in pieces_equal):
			if(qm_comeca == 0 or qm_comeca == 2):
				teamA_score = teamA_score + 2
			if(qm_comeca == 1 or qm_comeca == 3):
				teamB_score = teamB_score + 2
		elif(peca[:1] in peca2 or peca[2:] in peca2):
			if(qm_comeca == 0 or qm_comeca == 2):
				teamA_score = teamA_score + 1
			if(qm_comeca == 1 or qm_comeca == 3):
				teamB_score = teamB_score + 1
		tabuleiro.append(peca)
		modo_tabuleiro.append(modo_jog)
		pecas_tab = pecas_tab + 1
		players[qm_comeca].pop(peca_jog)
		i = 0
	
	print ""
	print ""
	for i in range(pecas_tab):
		if(modo_tabuleiro[i] == 'n'):
			print tabuleiro[i] + " ",
		'''
		if(modo_tabuleiro[i] == 'v'):
			for x in zip_longest(*tabuleiro[i].split(), fillvalue=' '):
				print (' '.join(x)) + " ",
		'''
		if(modo_tabuleiro[i] == 'i'):
			print tabuleiro[i] [::-1] + " ",
	print ""
	print ""
	
	jogadas = jogadas + 1
	qm_comeca = qm_comeca + 1
	if(qm_comeca == 4):
		qm_comeca = 0
	
	print ""
	print ""
	
	print "team A score: " + str(teamA_score)
	print "team B score: " + str(teamB_score)
	
	print ""
	print ""
	
	if(teamA_score == 7):
		print "Team A wins! "
		jogo_comecou = False
	elif(teamB_score == 7):
		print "Team B wins! "
		jogo_comecou = False



