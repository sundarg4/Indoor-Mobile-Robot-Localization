from bstem.platform import AdCord
import time
from math import *
import time
import sys
import Queue
import numpy
import gyro_filter as g

ad=AdCord()
offsetX=0
offsetY=0
offsetZ=0
rtd=57.2957795
for i in range(1,500): #500 values mean offset 
	#print(ad.gyroscope.z)
	offsetX+=ad.gyroscope.x
	offsetY+=ad.gyroscope.y
	offsetZ+=ad.gyroscope.z
offsetX=offsetX/500
offsetY=offsetY/500
offsetZ=offsetZ/500
print("Offset:",offsetX,offsetY,offsetZ)

#----------------------------------------------------------------------

dt=20.0 #in milliseconds
noiseX=0
noiseY=0
noiseZ=0
#print("Time:",(dt/1000))
for i in range(1,500):
	
	if((ad.gyroscope.x )-offsetX)>noiseX:
		noiseX=((ad.gyroscope.x )-offsetX)
	elif((ad.gyroscope.z )-offsetX)< -noiseX:
		noiseX=-((ad.gyroscope.x )-offsetX)

	if((ad.gyroscope.y )-offsetY)>noiseY:
		noiseY=((ad.gyroscope.y )-offsetY)
	elif((ad.gyroscope.z )-offsetY)< -noiseY:
		noiseY=-((ad.gyroscope.y )-offsetY)

	if((ad.gyroscope.z )-offsetZ)>noiseZ:
		noiseZ=((ad.gyroscope.z )-offsetZ)
	elif((ad.gyroscope.z )-offsetZ)< -noiseZ:
		noiseZ=-((ad.gyroscope.z )-offsetZ)
print ("noise:",noiseX,noiseY,noiseZ)
def gyro():

	#-----------Angle Calculations------------------------------------------------------------
	ad.gyroscope.dps=250
	gyroRatex,gyroRatey,gyroRatez=g.gyro_filter()
	global noiseX,noiseY,noiseZ
	global offsetX,offsetY,offsetZ
	if (gyroRatex -offsetX >= noiseX or gyroRatex -offsetX<= -noiseX):		
		gyroRatex=((gyroRatex ) - offsetX)*(dt/1000)
	if (gyroRatey -offsetY >= noiseY or gyroRatey -offsetY<= -noiseY):		
		gyroRatey=((gyroRatey ) - offsetY)*(dt/1000)
	if (gyroRatez -offsetZ >= noiseZ or gyroRatez -offsetZ<= -noiseZ):		
		gyroRatez=((gyroRatez ) - offsetZ)*(dt/1000)
	return (gyroRatex,gyroRatey,gyroRatez)
	
	
def kacc():
	global pnoise
	global snoise
	global error 	
	pnoise=0.15	
	snoise=4
	error=0
	ax=ad.accelerometer.x
	ay=ad.accelerometer.y
	az=ad.accelerometer.z
	x = (ad.accelerometer.x)
	y = (ad.accelerometer.y)
	z = (ad.accelerometer.z)	
	error=error+pnoise
	k=error/(error+snoise)
	ax = ax+k*(x-ax)
	ay = ay+(k*(y-ay))
	az = az+k*(z-az)
	error=(1-k)*error
	print(ax,ay,az)
	#print("Raw: "+str("%.5f" %y) + "  y" + str("%.5f" %gy))# + "Y: 	"+"LA: "+str("%.5f" %gy) + "Z: "+"LA: "+str("%.5f" %gz))
	return(ax,ay,az)

if __name__ == "__main__":
	while True:
		kacc()
