from math import *
r=open("accelerometer.txt","r")
f=open("accel_angle.txt","w")
for accel in r:
	a=accel.split(" ")
	theta=atan2(float(a[0]),float(a[1]))
	f.write(str(theta)+"\n")	
	
