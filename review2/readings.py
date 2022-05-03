from bstem.platform import AdCord
from gyro_calib import *
from encoders import *
import datetime
import threading
adz=AdCord()

g=threading.Thread(target=gyro) #gyro thread
g.daemon=True
g.start()

e=threading.Thread(target=erun) #erun thread
e.daemon=True
e.start()


r1=open("agereadings.txt","w")
while True:
	gz=q.get()
	r1.write(str(datetime.datetime.now())+", "+str(gz) + "," + str(adz.accelerometer.value[0])+ " "+str(adz.accelerometer.value[1])+" "+str(adz.accelerometer.value[2])+","  + str(-adz.encoder[0].position*3.38)+" " + str(adz.encoder[2].position*3.38) +"\n")
r1.close()
