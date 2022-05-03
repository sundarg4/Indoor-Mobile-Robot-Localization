import tty, sys, termios
from bstem.platform import AdCord

ad1=AdCord()
class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

f=open('raw_encoders.txt','w')
def erun():
    stscalar=0.2
    scalar=0.35
    newscalar=0.05
    while True:
        with ReadChar() as rc:
            char = rc
	print(ord(char))
	#rint("Leftwheel:",-ad1.encoder[2].position)#left motor
	#rint("Rightwheel:",ad1.encoder[0].position)#right motor
	#.write(str(-ad1.encoder[2].position)+" "+str(ad1.encoder[0].position)+"\n")
	if (char) =='w' or ord(char)==56:#forward
		#print((char))
		ad1.motor[0].speed=stscalar #right motor 
		ad1.motor[2].speed=-stscalar #left motor
		ad1.motor[0].speed=0 #right motor 
		ad1.motor[2].speed=0 #left motor
	elif (char)=='a' or ord(char)==52:#left
		ad1.motor[0].speed=scalar
		ad1.motor[2].speed=-newscalar
		ad1.motor[0].speed=0 #right motor 
		ad1.motor[2].speed=0 #left motor
	elif (char)=='d' or ord(char)==54:#right
		ad1.motor[0].speed=newscalar
		ad1.motor[2].speed=-scalar
		ad1.motor[0].speed=0 #right motor 
		ad1.motor[2].speed=0 #left motor
	elif (char)=='s' or ord(char)==53:#back
		ad1.motor[0].speed=-stscalar
		ad1.motor[2].speed=stscalar
		ad1.motor[0].speed=0 #right motor 
		ad1.motor[2].speed=0 #left motor
	elif ord(char)==32:#stop
		ad1.motor[0].speed=0
		ad1.motor[2].speed=0
		ad1.motor[0].speed=0 #right motor 
		ad1.motor[2].speed=0 #left motor
	if ord(char)==43:#increase speed
		scalar+=0.10
	elif ord(char)==45:#decrease speed
		scalar-=0.10		
	if char in "x" or ord(char)==27:#exit
            sys.exit()

if __name__ == "__main__":
    erun()
