from bstem.platform import AdCord
import time
from bstem.plot import Plot
from bstem.control import Scheduler

ad=AdCord()
def plot_accel():
	def kacc():
		global pnoise
		global snoise
		global error 	
		pnoise=0.1	
		snoise=0.8
		error=0
		gx=ad.accelerometer.x
		gy=ad.accelerometer.y
		gz=ad.accelerometer.z

		while(True):
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
			ystr=str("%.2f" %y)
			gystr=str("%.2f" %gy)
			return(float(ystr),float(gystr))
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
