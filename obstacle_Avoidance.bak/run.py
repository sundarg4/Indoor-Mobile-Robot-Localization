#This is a very big program with great potential, dont judge by the number of lines of this code.
#If you dont believe me, go see the obstacle_avoided file that this file imports
from bstem.platform import AdCord
import threading
from obstacle_avoided import *

f=threading.Thread(target=run) #run thread to control motor in obstacle autonomously
f.daemon=True
f.start()

print "RUN"
