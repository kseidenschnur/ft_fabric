import time
from log import logSPLK
from connectTXT import connectTXT

txt, mtr_a1, mtr_a2, mtr_b1, mtr_b2, mtr_b3, mtr_b4, \
tst_a1, tst_a2, tst_a3, tst_a4, tst_a5, tst_a6, tst_a7, tst_a8, \
tst_b1, tst_b2, tst_b3, tst_b4, tst_b5, tst_b6, tst_b7, tst_b8, \
out_a5, out_a6,out_a7,out_a8,out_b3, out_b8 = connectTXT()

#Kompressor ein
out_b8.setLevel(512)
txt.updateWait()

#Tor auf
out_a7.setLevel(512)
txt.updateWait()

#Schlitten rein
mtr_a1.setSpeed(-512)
mtr_a1.setDistance(0)
while tst_a1.state()!=1:
    txt.updateWait()
mtr_a1.stop()

#Tor zu warten und auf
out_a7.setLevel(0)
time.sleep(5)
out_a7.setLevel(512)

#Schlitten rein
mtr_a1.setSpeed(512)
mtr_a1.setDistance(0)
while tst_a2.state()!=1:
    txt.updateWait()
mtr_a1.stop()

#Greifer in position zur aufnahme
mtr_a2.setSpeed(-512)
mtr_a2.setDistance(0)
while tst_a3.state()!=1:
    txt.updateWait()
mtr_a2.stop()

#Greifer runter
out_a6.setLevel(512)
txt.updateWait()

time.sleep(1)

#Ansaugen
out_a5.setLevel(512)
txt.updateWait()

time.sleep(1)

#Greifer hoch
out_a6.setLevel(0)
txt.updateWait()

time.sleep(5)

#Greifer abgabe
mtr_a2.setSpeed(512)
mtr_a2.setDistance(0)
while tst_b5.state()!=1:
    txt.updateWait()
mtr_a2.stop()

#Greifer runter
out_a6.setLevel(512)
txt.updateWait()

#Block abladen
out_a5.setLevel(0)
txt.updateWait()

#Kompressor aus
out_b8.setLevel(512)