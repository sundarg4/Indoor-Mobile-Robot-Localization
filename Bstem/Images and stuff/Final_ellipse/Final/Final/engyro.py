import math
import time
x=0
y=0
s=0
s_ge=0
count=0
p_gyro=0

tstamp=open("tstamp.txt",'w')

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

w = open("e_g,e.txt",'w',0)


for val in k:
	reading = val.split(",")
	rc.append(reading[0])
	encoder = (reading[1].split(" "))
	l.append(float(encoder[0]))
	r.append(float(encoder[1]))
	ts1.append(float(encoder[2]))
	#tstamp.write(encoder[2])
	s = s + 1
#print rc
#print ts1	
		
	
for val1 in ge:
	geread = (val1.split(","))
	gyro.append(float(geread[0]))
	#if(gyro[val1]+gyro[val1] )	
	g_diff.append(gyro[s_ge] - p_gyro)
	p_gyro = gyro[s_ge]
	encoderge=(geread[1].split(" "))
	lge.append(float(encoderge[0]))
	rge.append(float(encoderge[1]))
	tge.append(float(encoderge[2]))
	s_ge = s_ge + 1
print tge
for num in range (s):
		tstamp.write(str(ts1[num])+"\n")

p_ts=ts1[0]
p_tge=tge[0]
j=0
i=0
while(i <> s+1):
	print(i,j)
	if rc[i] =='w':
		print "#########"
		print (tge[j], p_ts,ts1[i+1])
		while(tge[j] >= p_ts and tge[j] <= ts1[i+1]):
			w.write("w" + "," + str(lge[j]) + " " + str(rge[j]) +"," + str(g_diff[j])+"\n")
			j=j+1
		i=i+1
		#p_ts=ts1[i+1]
	elif rc[i]=='s':#back
		while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
			w.write("s" + "," + str(lge[j]) + " " + str(rge[j]) +"," + str(g_diff[j])+ "\n")
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
		
							
				
			

		
			
	
		
		
