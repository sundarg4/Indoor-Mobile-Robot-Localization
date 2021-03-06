import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

x=[]
y=[]

img = mpimg.imread('The_grid1.jpg')
imgplot = plt.imshow(img,extent=[-850,850,-254,254])

readFile = open('newdata2.txt','r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	XANDY = plotpair.split(',')
	if len(XANDY) > 1:
		x.append(int(float(XANDY[0])))
		y.append(int(float(XANDY[1])))

plt.plot([x],[y],'o',color='blue')

def quit_figure(event):
	if event.key == 'q':
		plt.close(event.canvas.figure)
cid = plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)
figure = plt.gcf()
figure.set_size_inches(16.80,4.57)
plt.savefig("obs+gyro+encoders.png",dpi=120)
#plt.show()3
