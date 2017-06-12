import sys
import random
# -*- coding: utf-8 -*-

pieces = ["0 | 0", "1 | 0", "1 | 1", "2 | 0", "2 | 1", "2 | 2", "3 | 0", "3 | 1", "3 | 2",
 "3 | 3", "4 | 0", "4 | 1", "4 | 2", "4 | 3", "4 | 4", "5 | 0", "5 | 1", "5 | 2", "5 | 3", 
 "5 | 4", "5 | 5", "6 | 0", "6 | 1", "6 | 2", "6 | 3", "6 | 4", "6 | 5", "6 | 6"]

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
		
for i in range(4):
	print "player " + str(i) + " pieces:"
	for j in range(6):
		print players[i][j]
		
pieces = ["0 | 0", "1 | 0", "1 | 1", "2 | 0", "2 | 1", "2 | 2", "3 | 0", "3 | 1", "3 | 2",
 "3 | 3", "4 | 0", "4 | 1", "4 | 2", "4 | 3", "4 | 4", "5 | 0", "5 | 1", "5 | 2", "5 | 3", 
 "5 | 4", "5 | 5", "6 | 0", "6 | 1", "6 | 2", "6 | 3", "6 | 4", "6 | 5", "6 | 6"]

peca = 0
escolhido = False
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
				break
		if(escolhido == True):
			break
		
	if(escolhido == False):
		peca = peca + 1
	else:
		peca = 7
	
teamA_score = 0
teamB_score = 0





