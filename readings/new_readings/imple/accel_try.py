from math import * 
#import tty, sys, termios

print "Enter the initial position of the robot:"
k= 1500#input('Enter X:')
l= 1500#input('Enter Y:')

p_dist=0
p_ang=0

f=open("newdata.txt","w",0)
r1=open("accel_angle.txt","r")
#r2=open("encoders.txt","r")
for theta in r1:#zip(r1,r2):
	#dist=((((en.split(','))[1]*3.38)+((en.split(','))[2]*3.38))/2)
	r=5
	theta=float(theta)+p_ang
	p_ang=theta
	print("accel_angle:"+str(theta))
	k+=(r*(sin(theta)))
	l+=(r*(cos(theta)))
	print("x+:"+str(r*(sin(theta))))
	print("y+:"+str(r*(cos(theta))))	
	print("---------------------------")
	f.write(str(k) + "," +str(l) + "\n")
f.close()
