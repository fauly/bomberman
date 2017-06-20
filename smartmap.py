# -*- coding: UTF-8 -*-
import sys, random, time,os
import subprocess as sp

running = True
osrun = os.name
print osrun

if osrun == 'mac':
	resx = 32
	resy = 16
elif osrun == 'nt':
	resx = 14
	resy = 16
else:
	resx = 16
	resy = 16


x,y = 0,0
mapmatrix = [[0 for x in range(resy)] for y in range(resx)]
edge = {}
blocks = {}
blocks[1] =		'░','#'
blocks[2] =		'▒','#'
blocks[3] =		'▓','#'
blocks[4] =	u'\U0001F4A3','B' #Bomb
blocks[5] =	u'\U0001F480','S' #skull
blocks[6] =	u'\U0001F47F','D' #devil
blocks[7] =	u'\U0001F46E','C' #cop
blocks[8] =	u'\U0001F525','@' #fire - Effect
blocks[9] =	u'\U0001F34B','*' #lemon - Powerup

edge[0] = u'\u2554'
edge[1] = u'\u2557'
edge[2] = u'\u2550'
edge[3] = u'\u255A'
edge[4] = u'\u255D'
edge[5] = u'\u2551'

charx,chary = random.randint(1,resx-2),random.randint(1,resy-2)

def generate():
	tileno = 1
	for yno in xrange(0,resy):
		for xno in xrange(0,resx):
			if yno == chary and xno == charx:
				if osrun == 'mac':
					mapmatrix[xno][yno] = blocks[6][0]
				elif osrun == 'nt':
					mapmatrix[xno][yno] = blocks[6][1]
				else:
					print "Shit"
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
					if osrun == 'mac':
						mapmatrix[xno][yno] = blocks[0][0]
					elif osrun == 'nt':
						mapmatrix[xno][yno] = blocks[0][1]
					else:
						print "Shit"
			tileno+=1

def smartdraw():
	sp.call('clear',shell=True)
	for yno in xrange(0,resy):
		for xno in xrange(0,resx):
			current = str(mapmatrix[xno][yno])
			sys.stdout.write(current)
		print
