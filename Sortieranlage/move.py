import time
from log import logSPLK
from connectTXT import connectTXT

#Connect to TXT
txt = connectTXT()

#Create engine objects on TXT 0
mtr_a1 = txt.motor(1, ext=0) # Engine A1
#mtr_a2 = txt.motor(2, ext=0) # Engine A2
#mtr_a3 = txt.motor(3, ext=0) # Engine A2
#mtr_a4 = txt.motor(4, ext=0) # Engine A2

# Create output object on TXT 0
#out_a1 = txt.output(1, ext=0)
#out_a2 = txt.output(2, ext=0)
out_a3 = txt.output(3, ext=0)
out_a4 = txt.output(4, ext=0)
out_a5 = txt.output(5, ext=0)
out_a6 = txt.output(6, ext=0)
out_a7 = txt.output(7, ext=0)
out_a8 = txt.output(8, ext=0)

# Create objects for sensors on TXT 0
tst_a1 = txt.input(1, ext=0)
#tst_a2 = txt.input(2, ext=0)
tst_a2 = txt.colorsensor(2, ext=0)
tst_a3 = txt.input(3, ext=0)
tst_a4 = txt.input(4, ext=0)
tst_a5 = txt.input(5, ext=0)
tst_a6 = txt.input(6, ext=0)
tst_a7 = txt.input(7, ext=0)
tst_a8 = txt.input(8, ext=0)

######################################################################################################################################

def sortieranlage():

    #Starte Laufband
    mtr_a1.setSpeed(-412)
    
    while True:
        print('Color: ' + str(tst_a2.color()))
        print('Value: ' + str(tst_a2.value()))
        txt.updateWait()

    # while True:
    #     color = tst_a2.voltage()
    #     if 660 <= color <= 700:
    #         freight = 'white'
    #         out_a8.setLevel(512)
    #         print(color)
    #         print(freight)
    #         while tst_a3.state() != 0:
    #             txt.updateWait()
    #         time.sleep(0.7)
    #         txt.updateWait()
    #         out_a5.setLevel(512)
    #         txt.updateWait()
    #         time.sleep(0.5)
    #         out_a5.setLevel(0)
    #         txt.updateWait()
    #         out_a8.setLevel(0)

    #     elif 1180 <= color <= 1260:
    #         freight = 'blue'
    #         out_a8.setLevel(512)
    #         print(color)
    #         print(freight)
    #         while tst_a3.state() != 0:
    #             txt.updateWait()
    #         time.sleep(2)
    #         txt.updateWait()
    #         out_a6.setLevel(512)
    #         txt.updateWait()
    #         time.sleep(0.5)
    #         out_a6.setLevel(0)
    #         txt.updateWait()
    #         out_a8.setLevel(0)
    