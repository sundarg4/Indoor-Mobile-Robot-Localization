import tty, sys, termios
from bstem.platform import AdCord
ad=AdCord()

class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


def test():
    scalar=0.5
    while True:
        with ReadChar() as rc:
            char = rc
	#print(ord(char))
	print("Speed:",scalar)
	if (char) =='w' or ord(char)==56:#forward
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
		ad.motor[0].speed=0
		ad.motor[2].speed=0
	if ord(char)==43:#increase speed
		scalar+=0.10
		print("Speedincresed:",scalar)
	elif ord(char)==45:#decrease speed
		scalar-=0.10
		print("speeddecresed:",scalar)		
	if char in "x" or ord(char)==27:#exit
            sys.exit()

if __name__ == "__main__":
    test()


