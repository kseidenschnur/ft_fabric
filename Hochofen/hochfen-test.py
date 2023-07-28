import time
from connectTXT import *

#Connect to TXT
txt = connectTXT()

#Create engine objects on TXT 0
mtr_a1 = txt.motor(1, ext=0) # Engine A1
mtr_a2 = txt.motor(2, ext=0) # Engine A2
#mtr_a3 = txt.motor(3, ext=0) # Engine A2
#mtr_a4 = txt.motor(4, ext=0) # Engine A2

# Create engine objects on TXT 1
mtr_b1 = txt.motor(1, ext=1) # Engine B1
mtr_b2 = txt.motor(2, ext=1) # Engine B2
mtr_b3 = txt.motor(3, ext=1) # Engine B3
#mtr_b4 = txt.motor(4, ext=1) # Engine B4

# Create output object on TXT 0
#out_a1 = txt.output(1, ext=0)
#out_a2 = txt.output(2, ext=0)
#out_a3 = txt.output(3, ext=0)
#out_a4 = txt.output(4, ext=0)
out_a5 = txt.output(5, ext=0)
out_a6 = txt.output(6, ext=0)
out_a7 = txt.output(7, ext=0)
out_a8 = txt.output(8, ext=0)

# Create output object on TXT 1
#out_b3 = txt.output(3, ext=1)
out_b7 = txt.output(7, ext=1)
out_b8 = txt.output(8, ext=1)

# Create objects for sensors on TXT 0
tst_a1 = txt.input(1, ext=0)
tst_a2 = txt.input(2, ext=0)
tst_a3 = txt.input(3, ext=0)
tst_a4 = txt.input(4, ext=0)
tst_a5 = txt.input(5, ext=0)
tst_a6 = txt.input(6, ext=0)
tst_a7 = txt.input(7, ext=0)
tst_a8 = txt.input(8, ext=0)

# Create objects for sensors on TXT 1
tst_b1 = txt.input(1, ext=1)
tst_b2 = txt.input(2, ext=1)
tst_b3 = txt.input(3, ext=1)
tst_b4 = txt.input(4, ext=1)
tst_b5 = txt.input(5, ext=1)
tst_b6 = txt.input(6, ext=1)
tst_b7 = txt.input(7, ext=1)
tst_b8 = txt.input(8, ext=1)

#Kompressor ein
logSPLK('Function: hochofen | Engine: out_b8 | Status: Turn on compressor | Level: 512')
out_b8.setLevel(512)
txt.updateWait()

#Tor auf
logSPLK('Function: hochofen | Engine: out_a7 | Status: Open gate | Level: 512')
out_a7.setLevel(512)
txt.updateWait()

#Schlitten rein
logSPLK('Function: hochofen | Engine: mtr_a1 | Status: Move in | Level: 512')
mtr_a1.setSpeed(-512)
#mtr_a1.setDistance(0)
while tst_a1.state()!=1:
    txt.updateWait()
mtr_a1.stop()