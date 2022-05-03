import math
import plot_klaus_brenner as pkb

print "Enter the initial position of the robot:"
k= pkb.ix#input('Enter X:')
l= pkb.iy#input('Enter Y:')

p_dist=0
p_ang=0

w=open("newdata2.txt","w")
r=open("gyroscope.txt","r")

w.write(str(k) + "," +str(l) + "\n")
sepFile = r.read().split('\n')
for val in sepFile: 
	ticks_to_cm = (pkb.ticks_to_cm_l + pkb.ticks_to_cm_r)/2
	reading = val.split(',')
	gz=float(reading[0])
	encoder=reading[1].split(' ')
	dist=((float(encoder[0])+float(encoder[1]))/2)
	r=(dist-p_dist)*ticks_to_cm
	print (dist,p_dist,r)
	p_dist=dist
	#print("Left:"+str(-ad1.encoder[2].position*3.38))
	#print("Right:"+str(ad1.encoder[1].position*3.38))
	#print(dist)
	theta=(math.radians(gz))
	#theta=ang-p_ang
	#print (ang,p_ang,theta)
	#p_ang=ang
	k+=(r*(math.cos(theta)))
	l+=(r*(math.sin(theta)))
	print(k,l)
	print("------------------------------")
	w.write(str(k) + "," +str(l) +"\n")
w.close()
