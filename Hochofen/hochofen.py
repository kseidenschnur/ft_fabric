from move import *
import time

######################################################################################################################################

print("Hochofen")
reset()
while True:
    txt.updateWait()
    if tst_a5.state() == 0:
        txt.updateWait()
        time.sleep(2)
        txt.updateWait()
        reset()
        txt.updateWait()
        hochofen()
        txt.updateWait()
        station()
        txt.updateWait()