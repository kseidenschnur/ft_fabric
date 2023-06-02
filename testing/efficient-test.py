from connectTXT import connectTXT
from log import logSPLK

#Connect TXT Controller
txt = connectTXT()

#Create engine objects on TXT 0
mtr_a1 = txt.motor(2, ext=0) # Engine A1
mtr_a2 = txt.motor(4, ext=0) # Engine A2
mtr_a3 = txt.motor(3, ext=0) # Engine A3
mtr_a4 = txt.motor(1, ext=0) # Engine A4

# Create objects for sensors on TXT 0
tst_a1 = txt.input(1, ext=0)
tst_a2 = txt.input(2, ext=0)
tst_a3 = txt.input(3, ext=0)
tst_a4 = txt.input(4, ext=0)
tst_a5 = txt.input(5, ext=0)
tst_a6 = txt.input(6, ext=0)
tst_a7 = txt.input(7, ext=0)
tst_a8 = txt.input(8, ext=0)

#############################################################################################

mtr_a2.setSpeed(512)
    while tst_a8.state()!=1:
        txt.updateWait()
    mtr_a2.stop()
