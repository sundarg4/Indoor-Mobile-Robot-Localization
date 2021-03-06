import plot_klaus_brenner as pkb
import math
#gyroscope
ang=0
theta = 0
p_dist=0
ticks_to_cm = (pkb.ticks_to_cm_l + pkb.ticks_to_cm_r)/2
#encoders
pose = (pkb.ix,pkb.iy,0)
last_ticks = None
first_motor_ticks = True

def calculate_ticks(l,r):
	ticks = ((l),(r))
	global first_motor_ticks,last_ticks
        if first_motor_ticks:
       		first_motor_ticks = False
       		last_ticks = ticks
        motor_ticks = ( tuple([(int(float(ticks[i])))-(int(float(last_ticks[i]))) for i in range(2)]))
        last_ticks = ticks
	return motor_ticks

w = open("newdata1.txt",'w',0)
r = open("(g+e)readings.txt",'r')
for val in r:
	reading = val.split(",")
	rc = reading[0]
	encoder=reading[1].split(" ")
	l=float(encoder[0])
	r=float(encoder[1])
	if rc =='w':#front
		motor_ticks = calculate_ticks(l,r)
		pose = pkb.filter_step(pose, motor_ticks)
		ang = pose[2]

		#for gyroscope
		p_dist = (l+r)/2
		x = pose[0]
		y = pose[1]
		w.write(str(pose[0])+","+str(pose[1])+","+'w'+","+str(l)+" "+str(r)+","+str(ang*57.2957795)+"\n")

	elif rc=='s':#back
		motor_ticks = calculate_ticks(l,r)
		pose = pkb.filter_step(pose, motor_ticks)
		ang = pose[2]

		#for gyroscope
		p_dist = (l+r)/2
		x = pose[0]
		y = pose[1]	
		w.write(str(pose[0])+","+str(pose[1])+","+'s'+","+str(l)+" "+str(r)+","+str(ang*57.2957795)+"\n")

	elif rc=='a':#left
		ang+= math.radians(float(reading[2]))
		dist=(l+r)/2
		r_dist = (dist-p_dist)*ticks_to_cm
		#print (dist,p_dist,r)
		p_dist=dist
		theta=ang
		x+= (r_dist*(math.cos(theta)))
		y+= (r_dist*(math.sin(theta)))

		#for encoders
		pose = (x,y,ang)
		last_ticks = ((l),(r))
		w.write(str(pose[0])+","+str(pose[1])+","+'a'+","+str(l)+" "+str(r)+","+str(ang*57.2957795)+"\n")

	elif rc=='d':#right
		ang+= math.radians(float(reading[2]))
		dist=(l+r)/2
		r_dist = (dist-p_dist)*ticks_to_cm
		#print (dist,p_dist,r)
		p_dist=dist
		theta=ang
		x+= (r_dist*(math.cos(theta)))
		y+= (r_dist*(math.sin(theta)))

		#for encoders
		pose = (x,y,ang)
		last_ticks = ((l),(r))
		w.write(str(pose[0])+","+str(pose[1])+","+'d'+","+str(l)+" "+str(r)+","+str(ang*57.2957795)+"\n")
