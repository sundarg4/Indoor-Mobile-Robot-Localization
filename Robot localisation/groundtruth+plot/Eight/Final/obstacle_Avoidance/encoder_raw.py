from bstem.platform import AdCord
import encoders as ec
import threading
ad=AdCord()

e=threading.Thread(target=ec.erun) #run thread
e.daemon=True
e.start()

w = open("raw_encoder.txt","w",0)
while(True):
	w.write(str(ad.encoder[0].position)+" "+str(ad.encoder[2].position)+"\n")

w.close()
