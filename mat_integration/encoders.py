import tty, sys, termios
from bstem.platform import AdCord
from mapping import *

ad1=AdCord()
class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

scalar=0.5
f=open("encoders.txt",'w')
def erun():
    	global scalar
        with ReadChar() as rc:
            char = rc
	#print(ord(char))
	print("Leftwheel:",-ad1.encoder[3].position*3.38)#left motor
	print("Rightwheel:",ad1.encoder[1].position*3.38)#right motor
	f.write(str(-ad1.encoder[3].position*3.38)+" "+str(ad1.encoder[1].position*3.38)+"\n")
	if (char) =='w' or ord(char)==56:#forward
		#print((char))
		ad1.motor[1].speed=scalar #right motor 
		ad1.motor[3].speed=-scalar #left motor
	elif (char)=='a' or ord(char)==52:#left
		ad1.motor[1].speed=scalar
		ad1.motor[3].speed=scalar
	elif (char)=='d' or ord(char)==54:#right
		ad1.motor[1].speed=-scalar
		ad1.motor[3].speed=-scalar
	elif (char)=='s' or ord(char)==53:#back
		ad1.motor[1].speed=-scalar
		ad1.motor[3].speed=scalar
	elif ord(char)==32:#stop
		ad1.motor[1].speed=0
		ad1.motor[3].speed=0
	if ord(char)==43:#increase speed
		scalar+=0.10
	elif ord(char)==45:#decrease speed
		scalar-=0.10		
	if char in "x" or ord(char)==27:#exit
		show()
		sys.exit()

if __name__ == "__main__":
	while True:
		erun()
