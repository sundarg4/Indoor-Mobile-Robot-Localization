from encoders import *
from plot_klaus_brenner import *
from matplotlib import *
import threading
import time

def disp():
	pyplot.show()
if __name__ == '__main__':
	# Empirically derived conversion from ticks to mm.
	ticks_to_mm = 1#0.349
	# Measured width of the robot (wheel gauge), in mm.
	robot_width = 217
	'''print "Enter the initial position of the robot:"	
	#Setting initial points
	ix= input('Enter X:')
	iy= input('Enter Y:')'''
	# Start at origin (0,0), looking along x axis (alpha = 0).
	pose = (383.0, 546.0, 0.0)
	
	e=threading.Thread(target=run) #erun thread
	e.daemon=True
	e.start()

	g=threading.Thread(target=disp) #show() matplotlib thread
	g.daemon=True
	g.start()

	while(True):
		ticks=(-ad1.encoder[3].position*3.38,ad1.encoder[1].position*3.38)
		pose = filter_step(pose, ticks, ticks_to_mm, robot_width)
		#print pose
		pyplot.plot([pose[0]], [pose[1]], 'bo')
		#pyplot.draw()
		time.sleep(0.05)

