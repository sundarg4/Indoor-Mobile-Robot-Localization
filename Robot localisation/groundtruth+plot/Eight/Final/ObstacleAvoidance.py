ultra = open("lrultra.txt",'r')
sensor = []
for v in ultra:
	sensor = v.split(' ')
	lu = sensor[0]
	ru = sensor[1]
	lir = sensor[2]
	rir = sensor[3]
	
	'''if lu != 'w' or lu != 'a' or lu != 's' or lu != 'd':
		'''
	
