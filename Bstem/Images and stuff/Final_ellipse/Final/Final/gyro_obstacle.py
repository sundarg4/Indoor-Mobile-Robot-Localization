from bstem.platform import AdCord
from math import *
import time
import sys
import Queue
#import sys.exitfunc

qg = Queue.Queue()
#qo=Queue.Queue()
adr=AdCord()
offsetX=0
offsetY=0
offsetZ=0
f=open("gyro_readrings_raw",'w',0)
for i in range(1,250):#junk values
	gyro=adr.gyroscope
	f.write(str(gyro.x)+","+str(gyro.y)+","+str(gyro.z)+"\n")

f.write("-------------------"+"\n")
for i in range(1,500): #500 values mean offset 
	#print(adr.gyroscope.z)
	gyro=adr.gyroscope
	#f.write(str(gyro.x)+","+str(gyro.y)+","+str(gyro.z)+"\n")
	offsetX+=gyro.x*57.2957795
	offsetY+=gyro.y*57.2957795
	offsetZ+=gyro.z*57.2957795
offsetX=offsetX/500
offsetY=offsetY/500
offsetZ=offsetZ/500
print ("Initializing Jarvis...\n")
print("Offset:",offsetX,offsetY,offsetZ)

#----------------------------------------------------------------------

dt=20.0 #in milliseconds
noiseX=0
noiseY=0
noiseZ=0
#print("Time:",(dt/1000))
for i in range(1,500):
	
	if((adr.gyroscope.x*57.2957795)-offsetX)>noiseX:
		noiseX=((adr.gyroscope.x*57.2957795)-offsetX)
	elif((adr.gyroscope.x*57.2957795)-offsetX)< -noiseX:
		noiseX=-((adr.gyroscope.x*57.2957795)-offsetX)

	if((adr.gyroscope.y*57.2957795)-offsetY)>noiseY:
		noiseY=((adr.gyroscope.y*57.2957795)-offsetY)
	elif((adr.gyroscope.y*57.2957795)-offsetY)< -noiseY:
		noiseY=-((adr.gyroscope.y*57.2957795)-offsetY)

	if((adr.gyroscope.z*57.2957795)-offsetZ)>noiseZ:
		noiseZ=((adr.gyroscope.z*57.2957795)-offsetZ)
	elif((adr.gyroscope.z*57.2957795)-offsetZ)< -noiseZ:
		noiseZ=-((adr.gyroscope.z*57.2957795)-offsetZ)

	#print("Noise:",noiseZ)
	#time.sleep(dt/1000)

#noiseZ=noiseZ*(dt/1000)
#print(noiseZ)
'''noiseX=noiseX*(dt/1000)
noiseY=noiseY*(dt/1000)
noiseZ=noiseZ*(dt/1000)'''

#time.sleep(dt/1000)
print("noisu:",noiseX,noiseY,noiseZ)

a=str(raw_input("Continue(y/n):"))
if(a=='n'):
	sys.exit()
#-----------------------------------------------------------------------

angleX=0
angleY=0
angleZ=0
#rotationThreshold=1
adr.gyroscope.dps=250
#print(adr.gyroscope.dps)
p_gyroRateX=0
p_gyroRateY=0
p_gyroRateZ=0

def g_angler(axis,gyroRate):
	#global angle
	global p_gyroRateX,p_gyroRateY,p_gyroRateZ
	global angleX,angleY,angleZ
	global noiseX,noiseY,noiseZ
	global offsetX,offsetY,offsetZ
	x=0
	if axis=='x':
		noise=noiseX
		offset=offsetX
		angle=angleX
		p_gyroRate=p_gyroRateX

	elif axis=='y':
		noise=noiseY
		offset=offsetY
		angle=angleY
		p_gyroRate=p_gyroRateY

	elif axis=='z':
		noise=noiseZ
		offset=offsetZ
		angle=angleZ
		p_gyroRate=p_gyroRateZ

	angle=0
	if (gyroRate*57.2957795-offset >= noise or gyroRate*57.2957795-offset <= -noise):		
		x=1
		gyroRate=((gyroRate*57.2957795) - offset)*(dt/1000)
		#print gyroRate,offset,noise
		angle=gyroRate
		#angle=(p_gyroRate + gyroRate)/2 #((p_gyroRate + gyroRate)*dt*57.2957795)/2000
		#p_gyroRate=gyroRate
		#angle/=8.75
		'''if (angle < 0):
			angle += 360;
		elif (angle >= 360):
			angle -= 360;'''

		if axis=='x':
			angleX=angle
			p_gyroRateX=p_gyroRate
		elif axis=='y':
			angleY=angle
			p_gyroRateY=p_gyroRate
		elif axis=='z':
			angleZ=angle
			p_gyroRateZ=p_gyroRate

		return (x,-angle)#-angle since this needs to correspond with anticlockwise to be +ve
	return(x,angle)#return previous angle....changed recently ;)

angX,angY,angZ=0,0,0
def gyror():
	while(True):
		time.sleep(dt/1000)
		#gyroRate=adr.gyroscope.z
		#print("Grate: ",gyroRate)
		global angX,angY,angZ
		x,gX=g_angler('x',adr.gyroscope.x)
		y,gY=g_angler('y',adr.gyroscope.y)
		z,gZ=g_angler('z',adr.gyroscope.z)
		angX+=gX
		angY+=gY
		angZ+=gZ
		#if(x==1 or y==1 or z==1):
		#print(gX,gY,gZ)
		#print("Angle:"+str(angX),str(angY),str(angZ))
		#q.put(gX)
		#q.put(gY)
		#print(gZ)
		qg.put(gZ)
		#return(gX,gY,gZ)
		
		'''
		z,gZ=g_angle('y',adr.gyroscope.y)
		if z==1:
			print(gZ)
			q.put(gZ)
		'''
if __name__ == "__main__":
	gyror()
