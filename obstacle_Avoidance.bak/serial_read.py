import serial
import Queue
ser = serial.Serial('/dev/ttyACM0',9600)
qr = Queue.Queue()

print "arduino"
def serial_read():
	print "serial_read"
	while True:
		rcr = ser.read()
		#print rcr
		#print rc #read the newest output from the arduino
		qr.put(rcr)

if __name__ == "__main__":
    serial_read()
