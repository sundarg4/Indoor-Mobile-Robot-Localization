import threading
import math
from gyro_obstacle import *#returns gyro for every 20ms without summation

k=threading.Thread(target=gyror) #calling the gyroscope thread
k.daemon=True
k.start()
print "Gyro_"
def angle_calculate():
	print "angle_calculate"
	while True:
		gz = qg.get()
		'''if obs.rc == 'a':#left
			l = -adr.encoder[2].position
			r = adr.encoder[0].position
			obs.f.write("a"+","+str(l)+" "+str(r)+","+str(gz)+"\n")
			obs.r1.write("a,"+str(obs.gs.gzs)+","+str(l)+" "+str(r)+"\n")

		elif obs.rc == 'd':#right
		        l = -adr.encoder[2].position
			r = adr.encoder[0].position
			obs.f.write("d"+","+str(l)+" "+str(r)+","+str(gz)+"\n")
			obs.r1.write("d,"+str(obs.gs.gzs)+","+str(l)+" "+str(r)+"\n")'''


