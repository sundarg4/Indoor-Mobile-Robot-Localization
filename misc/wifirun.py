import tty, sys, termios
from bstem.platform import AdCord
from gi.repository import NetworkManager, NMClient
import threading
import time

nmc = NMClient.Client.new()
devs = nmc.get_devices()
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
	print("run:"+char)
	if (char) =='' or ord(char)==56:#forward
		print((char))
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
	elif ord(char)==45:#decrease speed
		scalar-=0.10		
	if char in "x" or ord(char)==27:#exit
            sys.exit()

def wifiscanner():
	while True:
		with ReadChar() as rc:
			char=rc
		print("wifi:"+char)
		for dev in devs:
			if dev.get_device_type() == NetworkManager.DeviceType.WIFI:
				if (char)=='p':
			        	for ap in dev.get_access_points():
			            		print ap.get_ssid()

if __name__ == "__main__":
	for i in range(1):
	    sa=threading.Thread(target=wifiscanner)
	    da=threading.Thread(target=test)
	    #t.daemon=True
	    sa.start()
	    da.start()
