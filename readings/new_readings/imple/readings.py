from bstem.platform import AdCord
from gyro_calib import *
from encoders import *
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
	r1.write(str(gz) + "," + str(adz.accelerometer.value) + (-adz.encoder[3].position*3.38) + (adz.encoder[1].position*3.38) +"\n")
r1.close()
