from bstem.platform import AdCord
from math import *
from gyro_calib	import *
import time
ad=AdCord()

def orientation():        
        #Racc - is the inertial force vector as measured by accelerometer, that consists of following components (projections on X,Y,Z axes):

        Racc=[]
        Rxacc=[]
        Ryacc=[]
        Rzacc=[]
        Racc.append(ad.accelerometer.value)
        Rxacc.append(Racc[0][0])
        Ryacc.append(Racc[0][1])
        Rzacc.append(Racc[0][2]) #not used value

        magRacc=sqrt(pow(Rxacc[0],2)+pow(Ryacc[0],2))

        #|Racc| = SQRT(RxAcc^2 +RyAcc^2 + RzAcc^2),

        lst=list(Racc[0])
        lst[0]=Rxacc[0]/magRacc
        lst[1]=Ryacc[0]/magRacc
        Racc[0]=tuple(lst)


        #Next we'll introduce a new vector and we'll call it

        #Rest = [RxEst,RyEst,RzEst]
        Rest=[]
        Rxest=[]
        Ryest=[]
        #Rzest=[]

        Rest.append(Racc[0])
        Rxest.append(Rest[0][0])
        Ryest.append(Rest[0][1])

        n=0
        Axy=[]
        RateAxy=[]
        RateAxy.append(ad.gyroscope.z)
        Axy.append({Rxest[0],Ryest[0]})
        f=open("reading.txt",'w')
        while(True):
                gz=q.get()
                if(ad.accelerometer.x==0 and ad.accelerometer.y==0):
                        continue
                n+=1
                Racc.append(ad.accelerometer.value)
                Rxacc.append(Racc[n][0])
                Ryacc.append(Racc[n][1])
                magRacc=sqrt(pow(Rxacc[n],2)+pow(Ryacc[n],2))
                
                lst=list(Racc[n])
                lst[0]=Rxacc[0]/magRacc
                lst[1]=Ryacc[0]/magRacc
                Racc[n]=tuple(lst)

                #gyroscope
                #Rgyro=ad.gyroscope.value
                RateAxy.append(ad.gyroscope.z)
                Axy.append((atan2(Rxest[n-1],Ryest[n-1]))+(RateAxy[n]*(.01))) #Axy[n]
                RateAxyAvg=((RateAxy[n]+RateAxy[n-1])/2)
                Axy[n]=((atan2(Rxest[n-1],Ryest[n-1]))+(RateAxyAvg*(.01)))

                Rxgyro=sin(Axy[n])
                Rygyro=cos(Axy[n])

                wGyro=12#5-20
                Rxest.append((Rxacc[n] + Rxgyro * wGyro ) / (1 + wGyro))
                Ryest.append((Ryacc[n] + Rygyro * wGyro ) / (1 + wGyro))
                magRest=sqrt(pow(Rxest[n],2)+pow(Ryest[n],2))
                Rxest[n]=Rxest[n]/magRest
                Ryest[n]=Ryest[n]/magRest
                #finally
                #print("x:",Rxest[n]," y:",Ryest[n])
                #print('.')
                angle=atan2(Rxest[n],Ryest[n])
                f.write("x:")
                f.write(str(Rxest[n]))
                f.write("     ,y:")
                f.write(str(Ryest[n]))
		f.write("     ,angle:")
		f.write(str(angle))
		f.write("     ,degrees:")
		f.write(str(angle*57.294))
                f.write('\n')

        f.close()

