# Implement the first move model for the Lego robot.
# 02_a_filter_motor
# Claus Brenner, 31 OCT 2012
from math import * 
from pylab import *
from lego_robot import *
import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import sys

# Measured width of the robot (wheel gauge), in cm.
robot_width = 54
# Empirically derived conversion from ticks to mm.
ticks_to_cm_l = 3.3536
ticks_to_cm_r = 3.2263#3.2070
#5.558772438
#Setting initial points
ix=-265#input('Enter X:')
iy=-285#input('Enter Y:')

i=0
j=0
# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).
def filter_step(old_pose, motor_ticks):
	#img = mpimg.imread('map.png')
	#imgplot = plt.imshow(img)
	global i,j
	stlne =((motor_ticks[0]*ticks_to_cm_l - motor_ticks[1]*ticks_to_cm_r) )
	w.write(str(stlne)+"\n")
   	#l= motor_ticks[0]
	#r= motor_ticks[1]
	#print "--------"
	print stlne
	
	#print (l,r)
    	# Find out if there is a turn at all.
	if  stlne==0:
		#print ((motor_ticks[0]* ticks_to_mm)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_mm)*sin(old_pose[2])+old_pose[1],old_pose[2])
		#print("straight")
		#print ("0",stlne)
		i=i+1
		#print i
		return((motor_ticks[0]* ticks_to_cm_l)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_cm_r)*sin(old_pose[2])+old_pose[1],old_pose[2])
 		
        # --->>> Implement your code to compute x, y, theta here.
        #return (x, y, theta)

    	elif stlne > 0 and stlne < 0.070:#left turn
		#print("strlne :"+str(stlne))
		#print ("0 and 0.050",stlne)
		alpha=-((stlne)/robot_width)
		#print (ang)
		theta=old_pose[2]
		turn_rad = (motor_ticks[0]* ticks_to_cm_l) / (alpha) + robot_width/2
		#con=R+75
		#print (old_pose[2])
		cx=old_pose[0]-((turn_rad) * sin(theta))
		cy=old_pose[1]-(turn_rad * (-cos(theta)))
		#print motor_ticks[1]
	
		x=(cx+(turn_rad * sin(theta + alpha)))
		y=(cy+(turn_rad * -cos(theta + alpha)))
		#print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
		#print "left"
		i=i+1
		print i
		#print (x,y,theta+alpha)
        	return (x, y, theta+alpha)
		
	elif stlne < 0 and stlne > -0.070:#right turn
		#print("strlne :"+str(stlne))
		#print (l-r)
		#print ("-0.050 and 0",stlne)
		alpha=-((stlne)/robot_width)
		#print (ang)
		theta=old_pose[2]
		#con=R+75
		#print (old_pose[2])
		turn_rad = (motor_ticks[1]* ticks_to_cm_r) / (-alpha) + robot_width/2
		cx=old_pose[0]-(turn_rad * (-sin(theta)))
		cy=old_pose[1]-(turn_rad * (cos(theta)))

		x=(cx+(turn_rad * (-sin(theta + alpha))))
		y=(cy+(turn_rad * (cos(theta + alpha))))
		
		#print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
		#print "right"
		i=i+1
		print i
		#print (x,y,theta+alpha)
        	return (x, y, theta+alpha)

	else:	
		#print ("gyroscope",stlne)		
		ticks_to_cm = (ticks_to_cm_l + ticks_to_cm_r)/2
		r=(motor_ticks[0] +motor_ticks[1])/2
		avg = r*ticks_to_cm
		#print darr[i]
		ang=old_pose[2]+ math.radians(float(darr[i]))
		x= old_pose[0] + (avg * math.cos(ang))
		y= old_pose[1] + (avg * math.sin(ang))
		j=j+1
		i=i+1
		print i
		#print (x,y,ang)
		return (x,y,ang)
		
		
	
if __name__ == '__main__':

    '''readFile = open('newencoder.txt','r')
    sepFile = readFile.read().split('\n')
    readFile.close()'''

    # Read data.
    logfile = LegoLogfile()
    logfile.read("encoders.txt")
    #i=0
    print "Enter the initial position of the robot:"	

    f=open("newdata3.txt","w",0)
    f.write(str(ix) + "," +str(iy) + "\n")

    #for kalman_pure
   # w = open("kalman_chumma.txt",'w',0)
    w=open("leftandrightencoderdiff.txt",'w',0)
    # Start at origin (0,0), looking along x axis (alpha = 0).
    pose = (ix,iy, 0)#3.14159 = 180 degrees
    #f=open("newdata.txt","w",0)
    darr = []
    g = open("o_e_g,e.txt",'r')
    for kl in g:
	#reading = kl.split(",")
	#read = reading[2].split(" ")
	darr.append(float(kl))
    #print darr
	

    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks)
	#sys.stdin.read(1)
        f.write(str(pose[0])+","+str(pose[1])+","+str(pose[2]*57.2957795)+"\n")
	#w.write(str(degrees(pose[2]))+"\n")
        filtered.append(pose)
    f.close()
    #print i,j		
    '''# Draw result.
    for pose in filtered:
        print pose
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()'''	
