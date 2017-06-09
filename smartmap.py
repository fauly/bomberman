# -*- coding: UTF-8 -*-	
import sys, random, time
import subprocess as sp

resx = 32
resy = 16
x,y = 0,0
mapmatrix = [[0 for x in range(resy)] for y in range(resx)] 

blocks = {}
edge = {}
blocks[0] =	'░'
blocks[1] =	'▒'
blocks[2] =	'▓'
blocks[3] =	u'\U0001F4A3'.encode('utf-8') #Bomb
blocks[4] =	u'\U0001F480'.encode('utf-8') #skull
blocks[5] =	u'\U0001F47F'.encode('utf-8') #devil
blocks[6] =	u'\U0001F46E'.encode('utf-8') #cop
blocks[7] =	u'\U0001F525'.encode('utf-8') #fire - Effect
blocks[8] =	u'\U0001F34B'.encode('utf-8') #lemon - Powerup

edge[0] = '╔'
edge[1] = '╗'
edge[2] = '═'
edge[3] = '╚'
edge[4] = '╝'
edge[5] = '║'

charx,chary = random.randint(1,resx-2),random.randint(1,resy-2)	

def generate():
	tileno = 1
	for yno in xrange(0,resy):
		for xno in xrange(0,resx):
			if yno == chary and xno == charx:
				mapmatrix[xno][yno] = blocks[6]
			else:
				if yno == 0:
					if xno == 0:
						mapmatrix[xno][yno] = edge[0]
					elif xno == resx-1:
						mapmatrix[xno][yno] = edge[1]
					else:
						mapmatrix[xno][yno] = edge[2]
				elif yno == resy-1:
					if xno == 0:
						mapmatrix[xno][yno] = edge[3]
					elif xno == resx-1:
						mapmatrix[xno][yno] = edge[4]
					else:
						mapmatrix[xno][yno] = edge[2]
				elif xno == 0:
					mapmatrix[xno][yno] = edge[5]
				elif xno == resx-1:
					mapmatrix[xno][yno] = edge[5]
				else:
					mapmatrix[xno][yno] = blocks[0]
			tileno+=1

def smartdraw():
	sp.call('clear',shell=True)
	for yno in xrange(0,resy):
		for xno in xrange(0,resx):
			current = str(mapmatrix[xno][yno])
			sys.stdout.write(current)
		print

