from bstem.platform import AdCord
import time
import math

global i,count
i=0
count=0.0000000001
ad=AdCord()

def gyro_filter():
	global i,count
	alpha=0.3	 #between 0-1
	#dt=10.0		#in milliseconds
	gx=0.0
	gy=0.0
	gz=0.0
	prevtime= time.time()
	x = (ad.gyroscope.x)
	y = (ad.gyroscope.y)
	z = (ad.gyroscope.z)
	gx = (1-alpha)*x + (alpha)*gx
	gy = (1-alpha)*y + (alpha)*gy
	gz = (1-alpha)*z + (alpha)*gz
	linear_accel_x = x - gx
	linear_accel_y = y - gy
	linear_accel_z = z - gz
	currenttime=time.time()
	dt=1/(count/((currenttime-prevtime)/1000000))
	tc =dt*((1-alpha)/alpha)
	alpha = tc/(tc+dt)
	prevtime=currenttime
	count+=1
	time.sleep(0.02)
	return(gx,gy,gz)
	
	

	
