import tty, sys, termios
from bstem.platform import AdCord
import obstacle_avoided as oba

ad1=AdCord()
class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

def erun():
    while True:
        with ReadChar() as rck:
            char = rck
	#print(ord(char))
	if (char) =='w' or ord(char)==56:#forward
		oba.sr.qr.put('w')
	elif (char)=='a' or ord(char)==52:#left
		oba.sr.qr.put('a')
	elif (char)=='d' or ord(char)==54:#right
		oba.sr.qr.put('d')
	elif (char)=='s' or ord(char)==53:#back
		oba.sr.qr.put('s')		
	elif ord(char)==32:#stop
		oba.sr.qr.put(' ')
	if char in "x" or ord(char)==27:#exit
		oba.sr.qr.put('x')
            	sys.exit()

if __name__ == "__main__":
    erun()
