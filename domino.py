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

players = [player_A1, player_A2, player_B1, player_B2]

n = 1
p = 0
while (n < 25):
	for m in range(0, 4):
		p = random.randint(0, 27)
		if(pieces[p] != ""):
			players[m].append(pieces[p])
			pieces[p] = ""
			n = n + 1
		
for i in range(0, 4):
	print "player pieces:"
	for j in range(0, 6):
		print players[i][j]


