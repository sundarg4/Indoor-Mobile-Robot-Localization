from time import sleep
import serial
from bstem.platform import AdCord
from gyro_caib import *

ser = serial.Serial('/dev/ttyACM1',9600)
ad1=AdCord()
scalar=0.2
gyro_angle=0
while True:
	rc = ser.read()
	print rc #read the newest output from the arduino
	#print("Leftwheel:",-ad1.encoder[2].position*3.38)#left motor
	#print("Rightwheel:",ad1.encoder[0].position*3.38)#right motor
	#f.write(str(-ad1.encoder[2].position*3.38)+" "+str(ad1.encoder[0].position*3.38)+"\n")
	if rc =='w':#forward
		#print(rc)
		ad1.motor[0].speed=scalar #right motor 
		ad1.motor[2].speed=-scalar #left motor
	elif rc=='a':#left
		ad1.motor[0].speed=scalar
		ad1.motor[2].speed=scalar
	elif rc=='d':#right
		ad1.motor[0].speed=-scalar
		ad1.motor[2].speed=-scalar
	elif rc=='s':#back
		ad1.motor[0].speed=-scalar
		ad1.motor[2].speed=scalar
