r=open("agereadings.txt","r")
f=open("accelerometerzz.txt",'w')
sepFile = r.read().split('\n')
i=0
for age in sepFile:
	if(i<500):
		reading=age.split(',')
		accel=reading[2].split(" ")
		f.write(str(i*10) + "," + accel[2]+"\n")
		i=i+1
