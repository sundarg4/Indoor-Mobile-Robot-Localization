from bstem.platform import AdCord
import time
ad=AdCord()
f=open("accel_readings_raw",'w',0)
while True:
	time.sleep(500.0/1000)
	accel=ad.accelerometer
	f.write(str(accel.x)+","+str(accel.y)+","+str(accel.z)+"\n")
	print(accel.value)
