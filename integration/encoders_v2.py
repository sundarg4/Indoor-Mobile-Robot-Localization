import tty, sys, termios
from bstem.platform import AdCord
import threading

ad1=AdCord()
# define a thread which takes input
last_user_input=' '
def user_ip():
	global last_user_input
        while True:
            last_user_input = input('input something: ')
            # do something based on the user input here
            # alternatively, let main do something with
            # self.last_user_input

f=open("encoders.txt",'w')
scalar=0.5
def test():
	global last_user_input
	ip=threading.Thread(target=user_ip) #erun thread
	ip.daemon=True
	ip.start()
	while True:
		# do something  
		# do something with it.last_user_input if you feel like it
		f.write(str(-ad1.encoder[3].position*3.38)+" "+str(ad1.encoder[1].position*3.38)+"\n")	
		#print(ord(char))
		if last_user_input=='w':#forward
			#print((char))
			ad1.motor[1].speed=scalar #right motor 
			ad1.motor[3].speed=-scalar #left motor
		elif last_user_input=='a':#left
			ad1.motor[1].speed=scalar
			ad1.motor[3].speed=scalar
		elif last_user_input=='d':#right
			ad1.motor[1].speed=-scalar
			ad1.motor[3].speed=-scalar
		elif last_user_input=='s':#back
			ad1.motor[1].speed=-scalar
			ad1.motor[3].speed=scalar
		elif last_user_input==' ':#stop
			ad1.motor[1].speed=0
			ad1.motor[3].speed=0
		if last_user_input=='+':#increase speed
			scalar+=0.10
		elif last_user_input=='-':#decrease speed
			scalar-=0.10		
		if last_user_input=='x':#exit
        	    sys.exit()
	
if __name__ == "__main__":
	# main
	test()
