import math
import time
x=0
y=0
s=0
s_ge=0
count=0
p_gyro=0

#tstamp=open("tstamp.txt",'w')
ac = open("angle_count.txt",'w')
ge = open("(g,e)readings.txt",'r')


gyro=[]
g_diff=[]
lge = []
rge = []
tge = []

k = open("(g+e)readings.txt",'r')

rc=[]
l=[]
r=[]
ts1=[]

san=[]
#w = open("e_g,e.txt",'w',0)


for val in k:
	reading = val.split(",")
	rc.append(reading[0])
	encoder = (reading[1].split(" "))
	l.append(float(encoder[0]))
	r.append(float(encoder[1]))
	ts1.append(float(encoder[2]))
	#tstamp.write(encoder[2])
	s = s + 1
	
		
sa = open("sensor_angle.txt",'r')

for val1 in ge:
	geread = (val1.split(","))
	gyro.append(float(geread[0]))
	#if(gyro[val1]+gyro[val1] )	
	#g_diff.append(gyro[s_ge] - p_gyro)
	#p_gyro = gyro[s_ge]	
	encoderge=(geread[1].split(" "))
	lge.append(float(encoderge[0]))
	rge.append(float(encoderge[1]))
	tge.append(float(geread[3]))
	s_ge = s_ge + 1
#print tge
for sang in sa:
	san.append(float(sang))

ang_count=[]
i=0
j=0
l=0
p_ts=ts1[0]
p_tge=tge[0]

while(i <> s_ge+1):
	if rc[i] =='w':
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			#w.write("w" + "," + str(lge[j]) + " " + str(rge[j]) +"\n")
			j=j+1
			l=l+1
		i=i+1
		ac.write(str(l)+"\n")
		print l
		l=0
		#p_ts=ts1[i+1]
	elif rc[i]=='s':#back
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			#w.write("s" + "," + str(lge[j]) + " " + str(rge[j]) +"\n")
			j=j+1
			l=l+1
		i=i+1
		ac.write(str(l)+"\n")
		l=0
		#p_ts=ts1[i+1]
	
			
	elif rc[i]=='a':#left
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			#w.write("a" + "," + str(lge[j]) + " " + str(rge[j]) + "," + str(g_diff[j])+"\n")
			j=j+1
			l=l+1
		i=i+1
		ac.write(str(l)+"\n")
		l=0
		#p_ts=ts1[i+1]

			
	elif rc[i]=='d':#right
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			#w.write("d" + "," + str(lge[j]) + " " + str(rge[j]) + "," + str(g_diff[j])+"\n")
			j=j+1
			l=l+1
		i=i+1
		ac.write(str(l)+"\n")
		l=0
		#p_ts=ts1[i+1]
print (ang_count)
####################################################
'''
j=0
i=0
p_ts=ts1[0]
p_tge=tge[0]

while(s_ge >= i):
	if rc[i] =='w':
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			w.write("w" + "," + str(lge[j]) + " " + str(rge[j]) +"\n")
			j=j+1
		i=i+1
		#p_ts=ts1[i+1]
	elif rc[i]=='s':#back
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			w.write("s" + "," + str(lge[j]) + " " + str(rge[j]) +"\n")
			j=j+1
		i=i+1
		#p_ts=ts1[i+1]
	
			
	elif rc[i]=='a':#left
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			w.write("a" + "," + str(lge[j]) + " " + str(rge[j]) + "," + str(g_diff[j])+"\n")
			j=j+1
		i=i+1
		#p_ts=ts1[i+1]

			
	elif rc[i]=='d':#right
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			w.write("d" + "," + str(lge[j]) + " " + str(rge[j]) + "," + str(g_diff[j])+"\n")
			j=j+1
		i=i+1
		#p_ts=ts1[i+1]
		
							
				'''
			

		
			
	
		
		
