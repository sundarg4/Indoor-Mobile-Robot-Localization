import tty, sys, termios
from bstem.platform import AdCord
from datetime import datetime
from math import *
from accel_gyro_kalman_pure import orientation
#from srivenkat import orientation
import threading

#orientation()
ad=AdCord()

class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

def gyro(gxi,gyi,gzi,t):
	gxzi=(sqrt(pow(gxi,2)+pow(gzi,2)))
        gyzi=(sqrt(pow(gyi,2)+pow(gzi,2)))
	
	gx,gy,gz=ad.gyroscope.value
	gxzf=(sqrt(pow(gx,2)+pow(gz,2)))
	gyzf=(sqrt(pow(gy,2)+pow(gz,2)))

	gxz=gxzf-gxzi
	gyz=gyzf-gyzi

	ortxz=gxz*t
	ortyz=gyz*t
	print("Orientationxz:",ortxz,"Orientationyz:",ortyz)

def test():
    scalar=0.5
    while True:
	gxi,gyi,gzi=ad.gyroscope.value
	t1=datetime.time(datetime.now())
	with ReadChar() as rc:
            char = rc
	print((char))
	#t2=datetime.time(datetime.now())
	#print("ITime:",t1.second,"FTime:",t2.second)
	#t=t2.second-t1.second #only wroks if pressed within one minute
	#gyro(gxi,gyi,gzi,t)
	#print(ad.encoder[0].velocity,ad.encoder[2].velocity)
	#print(ad.encoder[0].position,ad.encoder[2].position)
	#gix,giy,giz=ad.gyroscope.value #initial gyroscope values
	#print("Initial:",gix,giy,giz)
	if (char) =='w' or ord(char)==56:#forward
		#print((char))
		ad.motor[0].speed=scalar
		ad.motor[2].speed=-scalar
	elif (char)=='a' or ord(char)==52:#left
		ad.motor[0].speed=scalar
		ad.motor[2].speed=scalar
	elif (char)=='d' or ord(char)==54:#right
		ad.motor[0].speed=-scalar
		ad.motor[2].speed=-scalar
	elif (char)=='s' or ord(char)==53:#back
		ad.motor[0].speed=-scalar
		ad.motor[2].speed=scalar
	elif ord(char)==32:#stop
		print("Stop")
		ad.motor[0].speed=0
		ad.motor[2].speed=0
	if ord(char)==43:#increase speed
		scalar+=0.10
	elif ord(char)==45:#decrease speed
		scalar-=0.10		
	if char in "x" or ord(char)==27:#exit
            sys.exit()



if __name__ == "__main__":
	
	sensor_thread = threading.Thread(target=orientation)
	sensor_thread.daemon = True
	sensor_thread.start()
	test()
