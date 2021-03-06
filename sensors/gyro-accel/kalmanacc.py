from bstem.platform import AdCord
import time
from bstem.plot import Plot
from bstem.control import Scheduler

ad=AdCord()
dt=20.0
accelx=[0]
accely=[0]
i=0
def plot_accel():
	def kacc():
		global pnoise
		global snoise
		global error 	
		pnoise=0.1	
		snoise=0.8
		error=0
		vely=0
		global i
		gx=ad.accelerometer.x
		gy=ad.accelerometer.y
		gz=ad.accelerometer.z

		while(True):
			time.sleep(dt/1000)
			x = (ad.accelerometer.x)
			y = (ad.accelerometer.y)
			z = (ad.accelerometer.z)	
			error=error+pnoise
			k=error/(error+snoise)
			gx = gx+k*(x-gx)
			gy = gy+(k*(y-gy))
			gz = gz+k*(z-gz)
			error=(1-k)*error
			#print("Raw: "+str("%.5f" %y) + "  y" + str("%.5f" %gy))# + "Y: 	"+"LA: "+str("%.5f" %gy) + "Z: "+"LA: "+str("%.5f" %gz))
			vely = vely + gy*(dt/1000)
			ystr=str("%.2f" %y)
			gystr=str("%.2f" %gy)
			#accelx.append(Linearaccel[0])
			i+=1
			accely.append(gy)
			print(gy,accely[i]-accely[i-1])
			return(float(gystr),float(accely[i]-accely[i-1]))
			#return(float(ystr),float(gystr))
	# Add lineplot to Scheduler
	Plot.lineplot(kacc, 'Local Line Plot')
    	# Run Scheduler for 5 seconds
	Scheduler.start(100)
    	# Remove lineplot from Scheduler
	Plot.clear()
if __name__ == "__main__":
	#while(True):
		#(a,b,c)=kacc()
		#print ("X:  " + str("%.3f" %a) + " "+"Y: " + str("%.3f" %b)+ " "+ "Z: "+ str("%.3f" %c))
	plot_accel()
