import time
from log import logSPLK
from connectTXT import connectTXT

txt = connectTXT()

#Create engine objects on TXT 0
mtr_a1 = txt.motor(2, ext=0) # Engine A1
mtr_a2 = txt.motor(4, ext=0) # Engine A2
mtr_a3 = txt.motor(3, ext=0) # Engine A3
mtr_a4 = txt.motor(1, ext=0) # Engine A4

# Create engine objects on TXT 1
mtr_b1 = txt.motor(1, ext=1) # Engine B1
mtr_b2 = txt.motor(2, ext=1) # Engine B2
mtr_b3 = txt.motor(3, ext=1) # Engine B3
#mtr_b4 = txt.motor(4, ext=1) # Engine B4

# Create output object on TXT 1
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

# Reset

mtr_a3.setSpeed(512)
while tst_a6.state()!=1:
    print ('Taster 6')
    print (tst_a6.state())
    txt.updateWait()
mtr_a3.stop()

mtr_a2.setSpeed(512)
while tst_a8.state()!=1:
    print ('Taster 8')
    print (tst_a8.state())
    txt.updateWait()
mtr_a2.stop()

mtr_a1.setSpeed(512)
while tst_a5.state()!=1:
    print ('Taster 5')
    print (tst_a5.state())
    txt.updateWait()
mtr_a1.stop()

#Fahre Greifarm hoch
print ('Starte Motor 6')
mtr_b2.setSpeed(512)
while tst_b2.state()!=1:
    txt.updateWait()
    print ('Motor 6 läuft noch....')
mtr_b2.stop()

#Fahre Arm rein
print ('Starte Motor 7')
mtr_b3.setSpeed(512)
while tst_b3.state()!=1:
    txt.updateWait()
    print ('Motor 7 läuft noch....')
mtr_b3.stop()

# Drehe zurück
print ('Starte Motor 1')
mtr_b1.setSpeed(512)
while tst_b1.state()!=1:
    txt.updateWait()
    print ('Motor 1 läuft noch....')
mtr_b1.stop()
