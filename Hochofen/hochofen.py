from move import *
import time

######################################################################################################################################

while True:
    if tst_a5.state() == 0:
        time.sleep(1)
        reset()
        txt.updateWait()
        hochofen()
        txt.updateWait()
        station()
        txt.updateWait()