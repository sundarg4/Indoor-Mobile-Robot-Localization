#This is a very big program with great potential, dont judge by the number of lines of this code.
#If you dont believe me, go see the obstacle_avoided file that this file imports
from bstem.platform import AdCord
import threading
import gyro_calib as gc
from obstacle_avoided import *

e=threading.Thread(target=gc.gyro) #gyro thread
e.daemon=True
e.start()

f=threading.Thread(target=run) #run thread to control motor in obstacle autonomouosly
f.daemon=True
f.start()

r1=open("(g,e)readings.txt","w",0)
while True:
	gz=gc.q.get()
	r1.write(str(gz)+","+str(-gc.ad.encoder[2].position)+" "+str(gc.ad.encoder[0].position)+"\n")
r1.close()
