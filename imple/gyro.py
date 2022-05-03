import math
import tty, sys, termios
from bstem.platform import AdCord
from gyro_calib import *
from run1 import *
import threading

adz=AdCord()

print "Enter the initial position of the robot:"
k= input('Enter X:')
l= input('Enter Y:')

g=threading.Thread(target=gyro) #gyro thread
g.daemon=True
g.start()

e=threading.Thread(target=test) #erun thread
e.daemon=True
e.start()

p_dist=0
p_ang=0

f=open("gyroreadings.txt","w",0)
while True:
	gz=q.get()
	f.write(str(gz))
	dist=(((-adz.encoder[3].position*3.38)+(adz.encoder[1].position*3.38))/2)
	r=dist-p_dist
	p_dist=dist
	#print("Left:"+str(-ad1.encoder[2].position*3.38))
	#print("Right:"+str(ad1.encoder[1].position*3.38))
	#print(dist)
	ang=(math.radians(gz))
	theta=ang-p_ang
	p_ang=ang
	print (dist,p_dist,r)
	print (ang,p_ang,theta)
	k+=(r*(math.sin(theta)))
	l+=(r*(math.cos(theta)))
	#f.write(str(k) + "," +str(l) + "\n")
f.close()
