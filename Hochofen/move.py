import time
from log import logSPLK
from connectTXT import connectTXT

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

######################################################################################################################################

def hochofen():
    logSPLK('Function: hochofen | Status: Start')

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
    mtr_a1.setDistance(0)
    while tst_a1.state()!=1:
        txt.updateWait()
    mtr_a1.stop()

    #Tor zu
    logSPLK('Function: hochofen | Engine: out_a7 | Status: Close Gate | Level: 0')
    out_a7.setLevel(0)
    txt.updateWait()
    #Turn light on
    out_a8.setLevel(512)
    txt.updateWait()
    
    #Wait
    logSPLK('Function: hochofen | Engine: none | Status: Wait 5 seconds | Level: 512')
    time.sleep(5)
    
    #Turn light of
    out_a8.setLevel(0)
    txt.updateWait()
    #Tor auf
    logSPLK('Function: hochofen | Engine: out_a7 | Status: Open gate | Level: 512')
    out_a7.setLevel(512)
    txt.updateWait()

    #Schlitten raus
    logSPLK('Function: hochofen | Engine: mtr_a1 | Status: Move out | Speed: 512')
    mtr_a1.setSpeed(512)
    mtr_a1.setDistance(0)
    while tst_a2.state()!=1:
        txt.updateWait()
    mtr_a1.stop()

    #Greifer in position zur aufnahme
    logSPLK('Function: hochofen | Engine: mtr_a1 | Status: Moving to position for pick up | Speed: -512')
    mtr_a2.setSpeed(-512)
    mtr_a2.setDistance(0)
    while tst_a3.state()!=1:
        txt.updateWait()
    mtr_a2.stop()

    #Greifer runter
    logSPLK('Function: hochofen | Engine: out_a6 | Status: Moving graber for pick up | Speed: -512')
    out_a6.setLevel(512)
    txt.updateWait()

    time.sleep(0.5)

    #Ansaugen
    logSPLK('Function: hochofen | Engine: out_a5 | Status: Loading freight | Speed: -512')
    out_a5.setLevel(512)
    txt.updateWait()

    time.sleep(0.5)

    #Greifer hoch
    logSPLK('Function: hochofen | Engine: out_a6 | Status: Moving graber for transport | Speed: 0')
    out_a6.setLevel(0)
    txt.updateWait()

    #Greifer zur abgabe
    logSPLK('Function: hochofen | Engine: mtr_a2 | Status: Moving graber to delivery | Speed: 512')
    mtr_a2.setSpeed(512)
    mtr_a2.setDistance(0)
    while tst_b5.state()!=1:
        txt.updateWait()
    mtr_a2.stop()

    #Greifer runter
    logSPLK('Function: hochofen | Engine: out_a6 | Status: Moving graber for delivery | Speed: 512')
    out_a6.setLevel(512)
    txt.updateWait()

    time.sleep(0.5)

    #Sauger aus
    logSPLK('Function: hochofen | Engine: out_a5 | Status: Delivering freigth | Speed: 0')
    out_a5.setLevel(0)
    txt.updateWait()

    time.sleep(0.5)

    #Greifer hoch
    logSPLK('Function: hochofen | Engine: out_a5 | Status: Deliverd freigth | Speed: 0')
    out_a6.setLevel(0)
    txt.updateWait()

    #Kompressor aus
    logSPLK('Function: hochofen | Engine: out_b8 | Status: Turn of compressor | Speed: 0')
    out_b8.setLevel(0)
    txt.updateWait()
    logSPLK('Function: hochofen | Status: Done')

def station():
    logSPLK('Function: station | Status: Start')

    #Drehen bis Taster zur Bearbeitung
    mtr_b1.setSpeed(-412)
    while tst_b2.state()!=1:
        txt.updateWait()
    mtr_b1.stop()

    #Bearbeitung starten
    mtr_b2.setSpeed(512)
    txt.updateWait()
    time.sleep (5)
    mtr_b2.setSpeed(0)
    txt.updateWait()

    #Weiter drehen zur Ausgabe
    mtr_b1.setSpeed(-412)
    while tst_b3.state()!=1:
        txt.updateWait()
    mtr_b1.stop()

    #Kompressor an
    out_b8.setLevel(512)
    txt.updateWait()
    time.sleep (1)
    #Push ein
    out_b7.setLevel(512)
    txt.updateWait()
    time.sleep (1)
    #Push aus
    out_b7.setLevel(0)
    txt.updateWait()
    #Kompressor aus
    out_b8.setLevel(0)
    txt.updateWait()

    #Förderband an
    mtr_b3.setSpeed(-512)
    while tst_b4.state()!=0:
        txt.updateWait()
    time.sleep(2)
    mtr_b3.stop()

    #Zurück drehen
    mtr_b1.setSpeed(412)
    while tst_b1.state()!=1:
        txt.updateWait()
    mtr_b1.stop()
    logSPLK('Function: station | Status: Done')

def reset():
    
    mtr_b1.setSpeed(512)
    while tst_b1.state()!=1:
        txt.updateWait()
    mtr_b1.stop()
