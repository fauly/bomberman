import sys
resx,resy = 9,9
x,y = 0,0

mapmatrix = [[0 for x in range(resy)] for y in range(resx)] 

sauron = mapmatrix[x][y]

tileno = 1

for xno in xrange(0,resx):
	for yno in xrange(0,resy):
		mapmatrix[yno][xno] = tileno
		tileno+=1
		current = str(mapmatrix[yno][xno])
		sys.stdout.write(current)
		sys.stdout.write('|')
	print

print mapmatrix[1][1]
print mapmatrix[2][0]