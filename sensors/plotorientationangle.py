# Implement the first move model for the Lego robot.
# 02_a_filter_motor
# Claus Brenner, 31 OCT 2012
from math import * 
from pylab import *
from lego_robot import *
import numpy as np
from PIL import Image
import matplotlib.image as mpimg

# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).
def filter_step(old_pose, motor_ticks, ticks_to_mm, robot_width):
	#img = mpimg.imread('map.png')
	#imgplot = plt.imshow(img)

	stlne =(motor_ticks[0] -motor_ticks[1])
   	l= motor_ticks[0]
	r= motor_ticks[1] 
	
	#print (l,r)
    # Find out if there is a turn at all.
	if  stlne == 0:
		#print ((motor_ticks[0]* ticks_to_mm)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_mm)*sin(old_pose[2])+old_pose[1],old_pose[2])
	 	return((motor_ticks[0]* ticks_to_mm)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_mm)*sin(old_pose[2])+old_pose[1],old_pose[2])
 
        # --->>> Implement your code to compute x, y, theta here.
        #return (x, y, theta)

    	elif stlne < 0:#left turn
		#print("strlne :"+str(stlne))
		
		alpha=-((stlne* ticks_to_mm)/robot_width)
		#print (ang)
		theta=old_pose[2]
		turn_rad = (motor_ticks[0]* ticks_to_mm) / (alpha) + robot_width/2
		#con=R+75
		#print (old_pose[2])
		cx=old_pose[0]-((turn_rad) * sin(theta))
		cy=old_pose[1]-(turn_rad * (-cos(theta)))
		#print motor_ticks[1]

		x=(cx+(turn_rad * sin(theta + alpha)))
		y=(cy+(turn_rad * -cos(theta + alpha)))
		#print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
        	return (x, y, theta+alpha)
		
	else:#right turn
		#print("strlne :"+str(stlne))
		#print (l-r)
		alpha=-((stlne* ticks_to_mm)/robot_width)
		#print (ang)
		theta=old_pose[2]
		#con=R+75
		#print (old_pose[2])
		turn_rad = (motor_ticks[1]* ticks_to_mm) / (-alpha) + robot_width/2
		cx=old_pose[0]-(turn_rad * (-sin(theta)))
		cy=old_pose[1]-(turn_rad * (cos(theta)))

		x=(cx+(turn_rad * (-sin(theta + alpha))))
		y=(cy+(turn_rad * (cos(theta + alpha))))
		
		#print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
        	return (x, y, theta+alpha)

if __name__ == '__main__':
    # Empirically derived conversion from ticks to mm.
    ticks_to_mm = 0.349

    '''readFile = open('newencoder.txt','r')
    sepFile = readFile.read().split('\n')
    readFile.close()'''

    # Measured width of the robot (wheel gauge), in mm.
    robot_width = 21.7

    # Read data.
    logfile = LegoLogfile()
    logfile.read("encoders.txt")

    print "Enter the initial position of the robot:"	
	#Setting initial points
    ix= input('Enter X:')
    iy= input('Enter Y:')
    f=open("newdata.txt","w",0)
    f.write(str(ix) + "," +str(iy) + "\n")

    # Start at origin (0,0), looking along x axis (alpha = 0).
    pose = (ix,iy, 0)
    #f=open("newdata.txt","w",0)

    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks, ticks_to_mm, robot_width)
        f.write(str(pose[0])+","+str(pose[1])+","+str(pose[2])+"\n")
        filtered.append(pose)
    f.close()
 	
    '''# Draw result.
    for pose in filtered:
        print pose
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()'''
