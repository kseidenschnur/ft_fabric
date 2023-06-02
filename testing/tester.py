import time
from log import logSPLK
from connectTXT import connectTXT

txt, mtr_a1, mtr_a2, mtr_a3, mtr_a4, mtr_b1, mtr_b2, mtr_b3, mtr_b4, \
tst_a1, tst_a2, tst_a3, tst_a4, tst_a5, tst_a6, tst_a7, tst_a8, \
tst_b1, tst_b2, tst_b3, tst_b4, tst_b6, tst_b6, tst_b7, tst_b8, out_b8 = connectTXT()

# Drehe zurück
print ('Starte Motor 1')
mtr_b1.setSpeed(512)
while tst_b1.state()!=1:
    txt.updateWait()
    print ('Motor 1 läuft noch....')
mtr_b1.stop()