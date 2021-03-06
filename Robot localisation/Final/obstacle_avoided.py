from bstem.platform import AdCord
import threading
import sys
import gyro_obstacle as gs
import plot_klaus_brenner as pkb
import angle_calculate_obstacle as aco

import serial_read as sr
from motor import *

h=threading.Thread(target=aco.angle_calculate) #to dynamicaly calculate angle during obstacle alone
h.daemon=True
h.start()

g=threading.Thread(target=sr.serial_read) #serial read thread
g.daemon=True
g.start()

j=threading.Thread(target=gs.gyror) #gyro summmated angle thread
j.daemon=True
j.start()

#i=threading.Thread(target=erun) #erun thread to get user input for controlling robot
#i.daemon=True
#i.start()

f=open('(g+e)readings.txt','w',0)
#r1=open("(g,e)readings.txt","w",0)
g=open("serial_data.txt",'w',0)
f1 = open("lrultra.txt",'w',0)
rc='w'
scalar=0.2
tscalar=0.40
newscalar=0.05
scalar1 = 0.275

#print "reached here :)"
def run():
	global rc
	global scalar,tscalar,newscalar
	print "run"
	while True:
		rca = sr.qr.get()
		rc = rca[:1]
		if rc =='w':#forward
			aco.adr.motor[0].speed=scalar #right motor 
			aco.adr.motor[2].speed=-scalar #left motor
			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			f.write('w'+","+str(l)+" "+str(r)+"\n")
			g.write(str(rc)+"\n")
		elif rc=='a':#left
			aco.adr.motor[0].speed=tscalar
			aco.adr.motor[2].speed=-newscalar
			gz = aco.qg.get()
			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			f.write("a"+","+str(l)+" "+str(r)+","+str(gz)+"\n")
			
		elif rc=='d':#right
			aco.adr.motor[0].speed=newscalar
			aco.adr.motor[2].speed=-tscalar
			gz = aco.qg.get()
			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			f.write("a"+","+str(l)+" "+str(r)+","+str(gz)+"\n")
		elif rc=='s':#back
			aco.adr.motor[0].speed=-scalar
			aco.adr.motor[2].speed=scalar
			l = -(aco.adr.encoder[2].position)
			r = (aco.adr.encoder[0].position)
			f.write('s'+","+str(l)+" "+str(r)+"\n")
			g.write(str(rc)+"\n")
		elif rc==' ':#stop
			aco.adr.motor[0].speed=0
			aco.adr.motor[2].speed=0

		elif rc =='x':#quit
			aco.adr.motor[0].speed=0
			aco.adr.motor[2].speed=0
			sys.exit()
		
		else:
			f1.write(rca)
			#print rca
	f.close()
	#r1.close()

if __name__ == "__main__":
    run()
