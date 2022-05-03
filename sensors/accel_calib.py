from bstem.platform import AdCord
from math import *
from run1 import *
import threading
import sys
ad=AdCord()

e=threading.Thread(target=test) #erun thread
e.daemon=True

try:
    e.start()
except (KeyboardInterrupt, SystemExit):
    e.stop()
    sys.exit()

while(True):
	if(ad.accelerometer.x==0 and ad.accelerometer.y==0):
		continue
	s="Accelerometer_angle:"+str(atan2(ad.accelerometer.value[0],ad.accelerometer.value[1]))
	sys.stdout.write(s + '\n') 
	#print("Accelerometer_angle:"+str(atan2(ad.accelerometer.value[0],ad.accelerometer.value[1])))
