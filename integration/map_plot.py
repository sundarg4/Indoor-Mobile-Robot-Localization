import sys
import pygame
import pygame as pg
import tty, sys, termios
import pygame.gfxdraw
from PIL import Image
from bstem.platform import AdCord
from gyro_calib import *
from run1 import *
import threading
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

adz=AdCord()
#def map(k,l):
	

if __name__ == "__main__":
	im = mpimg.imread("map_ground_floor.png")
	implot = plt.imshow(im)
		
	'''g=threading.Thread(target=gyro) #gyro thread
	g.daemon=True
	g.start()

	e=threading.Thread(target=test) #erun thread
	e.daemon=True
	e.start()
	
	p_dist=0
	p_ang=0
	#flag=0	
	while True:
		gz=q.get()
		dist=(((-adz.encoder[2].position*3.38)+(adz.encoder[1].position*3.38))/2)-p_dist
		#print("Left:"+str(-ad1.encoder[2].position*3.38))
		#print("Right:"+str(ad1.encoder[1].position*3.38))
		#print(dist)
		ang=(math.radians(gz))-p_ang
		k=((-dist*(math.sin(ang))/10)+x)
		l=(((dist*(math.cos(ang)))/10)+y)
		map(k,l)#send in pixels
		p_dist=dist
		p_ang=ang'''
