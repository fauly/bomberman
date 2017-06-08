# -*- coding: UTF-8 -*-	
import sys, random, time
import character,smartmap
import subprocess as sp

running = True

resx = 32
resy = 16

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

#def inputs(x):
#    return {
#        'w': 1,
#        'a': 2,
#        's': 3,
#        'd': 4,
#        ' ': 5
#    }[x]

def generatemap():
	tofill = (resx-1)*(resy-1)
	while tofill != 0:
		choice = blocks[random.randint(1,9)]
		map.append(choice)
		tofill -= 1

# i = 0 

# while i < len(map):
# 	if i == resx-1:
# 		print
# 	elif i == (resx*2)-1: 
# 		print
# 	elif i == (resx*3)-1: 
# 		print
# 	elif i == (resx*4)-1: 
# 		print
# 	elif i == (resx*5)-1: 
# 		print
# 	elif i == (resx*6)-1: 
# 		print
# 	elif i == (resx*7)-1: 
# 		print
# 	elif i == (resx*8)-1: 
# 		print
# 	elif i == (resx*9)-1: 
# 		print
# 	elif i == (resx*10)-1: 
# 		print
# 	elif i == (resx*11)-1: 
# 		print
# 	elif i == (resx*12)-1: 
# 		print
# 	elif i == (resx*13)-1: 
# 		print
# 	elif i == (resx*14)-1: 
# 		print
# 	elif i == (resx*15)-1: 
# 		print
# 	elif i == (resx*16)-1: 
# 		print
# 	else:
# 		sys.stdout.write(map[i])
# 	i+=1

# for k in xrange(1, resy):
# 	for i in xrange(0,len(map)):
# 		send = map[i]
# 		print 'I = ', i,'K = ', k,'VALUE = ',(resx*k)-1
# 		if i == (resx*k)-1:
# 			print 
# 		else:
# 	    	 sys.stdout.write(send)
# 		k+=1


# while i < len(map):
# 	k = 0
# 	while k <= resy:
# 		print k
# 		if i == (resx*k)-1:
# 			print
# 		else:
# 			sys.stdout.write(map[i])
# 		k+=1
# 	i+=1


def setup():
	generatemap()

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

#def input():
#	if 

#def logic():


#def storedata():


#def framerun():
#	draw()
#	input()
#	logic()
#	storedata()


setup();
while running:
	draw()
	time.sleep(0.05)