# -*- coding: UTF-8 -*-	
import sys, random, time
import subprocess as sp

resx = 32
resy = 16

mapmatrix = [[0 for x in range(resx)] for y in range(resy)] 

score = 1
livesleft = 4
bombsleft = 2

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

map=[]

def smartmap():
	tofill = (resx-1)*(resy-1)
	while tofill != 0:
		charx = random.randint(1,resx-1)
		chary = random.randint(1,resy-1)

		# choice = blocks[random.randint(1,9)]
		# map.append(choice)
		# tofill -= 1
	x,y = 0
	sauron = mapmatrix[x][y]
	tile = 0
	while y < resy+1:
		if y == 0:
			x1 = 0
			while x1 < resx+1:
				if x1 == 0:
					sys.stdout.write('╔')
				elif x1 == resx:	
					sys.stdout.write('╗')
				else:
					sys.stdout.write('═')
				x1+=1
		elif y == resy:
			x1 = 0
			while x1 < resx+1:
				if x1 == 0:
					sys.stdout.write('╚')
				elif x1 == resx:	
					sys.stdout.write('╝')
				else:
					sys.stdout.write('═')
				x1+=1
		else:
			while x < resx+1:
				if x == 0:
					sys.stdout.write('║')
					x+=1
				elif x == resx:
					sys.stdout.write('║')
					x+=1
				else:
					sys.stdout.write(map[tile])
					tile+=1
					x+=1
		y+=1
		x=0

smartmap()

def draw():
	sp.call('clear',shell=True)
	x = 0
	y = 0
	tile = 0
	while y < resy+1:
		if y == 0:
			x1 = 0
			while x1 < resx+1:
				if x1 == 0:
					sys.stdout.write('╔')
				elif x1 == resx:	
					sys.stdout.write('╗')
				else:
					sys.stdout.write('═')
				x1+=1
		elif y == resy:
			x1 = 0
			while x1 < resx+1:
				if x1 == 0:
					sys.stdout.write('╚')
				elif x1 == resx:	
					sys.stdout.write('╝')
				else:
					sys.stdout.write('═')
				x1+=1
		else:
			while x < resx+1:
				if x == 0:
					sys.stdout.write('║')
					x+=1
				elif x == resx:
					sys.stdout.write('║')
					x+=1
				else:
					sys.stdout.write(map[tile])
					tile+=1
					x+=1
		y+=1
		x=0
		print
	print "Score:",score,"   Lives:",livesleft,"   Bombs:",bombsleft

while True:
	draw()
	time.sleep(0.1)