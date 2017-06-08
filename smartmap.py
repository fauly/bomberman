# -*- coding: UTF-8 -*-	
import sys, random, time
import subprocess as sp

resx = 32
resy = 16
x,y = 0,0
mapmatrix = [[0 for x in range(resy)] for y in range(resx)] 

blocks = {}
blocks[1] =	'░'
blocks[2] =	'▒'
blocks[3] =	'▓'
blocks[4] =	u'\U0001F4A3' #Bomb
blocks[5] =	u'\U0001F480' #skull
blocks[6] =	u'\U0001F47F' #devil
blocks[7] =	u'\U0001F46E' #cop
blocks[8] =	u'\U0001F525' #fire - Effect
blocks[9] =	u'\U0001F34B' #lemon - Powerup



def smartdraw():
	tileno = 1
	sp.call('clear',shell=True)
	for xno in xrange(0,resy):
		for yno in xrange(0,resx):
			if xno == 0:
				if 
			mapmatrix[yno][xno] = '▓'
			tileno+=1
			current = str(mapmatrix[yno][xno])
			sys.stdout.write(current)
		print

while True:
	smartdraw()
	time.sleep(0.1)

