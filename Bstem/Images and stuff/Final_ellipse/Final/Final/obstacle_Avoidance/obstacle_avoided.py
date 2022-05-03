from bstem.platform import AdCord
import threading
import sys
import plot_klaus_brenner as pkb
import angle_calculate_obstacle as aco
#import gyro_summation as gs
import serial_read as sr
from motor import *

h=threading.Thread(target=aco.angle_calculate) #to dynamicaly calculate angle during obstacle alone
h.daemon=True
h.start()

g=threading.Thread(target=sr.serial_read) #serial read thread
g.daemon=True
g.start()

#j=threading.Thread(target=gs.gyros) #gyro summmated angle thread
#j.daemon=True
#j.start()

#i=threading.Thread(target=erun) #erun thread to get user input for controlling robot
#i.daemon=True
#i.start()

f=open('(g+e)readings.txt','w',0)
r1=open("(g,e)readings.txt","w",0)
g=open("serial_data.txt",'w',0)
f1 = open("lrultra.txt",'w',0)
rc='w'
scalar=0.2
tscalar=0.35
newscalar=0.05

print "reached here :)"
def run():
	global rc
	global scalar,tscalar,newscalar
	print "run"
	while True:
		#print "obstacle_avoided"
		rca = sr.qr.get()
		#a=sr.ser.readline()
		#print (rca)
		
		rc = rca[:1]
		#print rc
		
	#print str(ser.readline())
	
	
	
	
	
		
		#print("Leftwheel:",-adr.encoder[2].position*3.38)#left motor
		#print("Rightwheel:",adr.encoder[0].position*3.38)#right motor
		#f.write(str(-adr.encoder[2].position*3.38)+" "+str(adr.encoder[0].position*3.38)+"\n")
		if rc =='w':#forward
			#print(rc)
			aco.adr.motor[0].speed=scalar #right motor 
			aco.adr.motor[2].speed=-scalar #left motor

			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			print rc
			f.write('w'+","+str(l)+" "+str(r)+"\n")
			g.write(str(rc)+"\n")
			#g.write(str(rc)+"\n")
			#r1.write("w,"+str(gs.gzs)+","+str(l)+" "+str(r)+"\n")

		elif rc=='a':#left
			aco.adr.motor[0].speed=tscalar
			aco.adr.motor[2].speed=-newscalar
			print rc
			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			f.write("a"+","+str(l)+" "+str(r)+","+str(aco.gz)+"\n")
			g.write(str(rc)+"\n")
			#r1.write("a,"+str(gs.gzs)+","+str(l)+" "+str(r)+"\n")

		elif rc=='d':#right
			aco.adr.motor[0].speed=newscalar
			aco.adr.motor[2].speed=-tscalar
			print rc
			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			f.write("d"+","+str(l)+" "+str(r)+","+str(aco.gz)+"\n")
			g.write(str(rc)+"\n")
			#r1.write("d,"+str(gs.gzs)+","+str(l)+" "+str(r)+"\n")
			
		elif rc=='s':#back
			aco.adr.motor[0].speed=-scalar
			aco.adr.motor[2].speed=scalar
			print rc
			l = -(aco.adr.encoder[2].position)
			r = (aco.adr.encoder[0].position)
			f.write('s'+","+str(l)+" "+str(r)+"\n")
			g.write(str(rc)+"\n")
			#r1.write("s,"+str(gs.gzs)+","+str(l)+" "+str(r)+"\n")

		elif rc==' ':#stop
			aco.adr.motor[0].speed=0
			aco.adr.motor[2].speed=0

		elif rc =='x':#quit
			aco.adr.motor[0].speed=0
			aco.adr.motor[2].speed=0
			sys.exit()
		else:
			f1.write(rca)
	f.close()
	r1.close()

if __name__ == "__main__":
    run()
