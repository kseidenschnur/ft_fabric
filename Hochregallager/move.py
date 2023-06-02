from connectTXT import connectTXT
from log import logSPLK
import time

#Connect TXT Controller
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

######################################################################################################################################

def moveHBWGet(cell_name, col, get_cell):
    logSPLK('Function: moveHBWGet | Status: Start moving to Cell: ' + str(cell_name))

    logSPLK('Function: moveHBWGet | Engine: mtr_a1 | Status: Moving to position | Speed: -512 | Distance:' + str(col))
    mtr_a1.setSpeed(-512)
    mtr_a1.setDistance(col)
    while mtr_a1.getCurrentDistance() < col:
        txt.updateWait()
    mtr_a1.stop()

    logSPLK('Function: moveHBWGet | Engine: mtr_a2 | Status: Moving to position | Speed: -512 | Distance:' + str(get_cell))
    mtr_a2.setSpeed(-512)
    mtr_a2.setDistance(get_cell)
    while mtr_a2.getCurrentDistance() < get_cell:
        txt.updateWait()
    mtr_a2.stop()
    logSPLK('Function: moveHBWGet | Status: Done moving to Cell: '  + str(cell_name))

def moveHBWGrab():
    logSPLK('Function: moveHBWGrab | Status: Start loading freight')

    logSPLK('Function: moveHBWGrab | Engine: mtr_a3 | Status: Positioning to load freight | Speed: -512')
    mtr_a3.setSpeed(-512)
    while tst_a7.state()!=1:
        txt.updateWait()
    mtr_a3.stop()

    logSPLK('Function: moveHBWGrab | Engine: mtr_a2 | Status: Loading freight | Speed: 512 | Distance: 100')
    mtr_a2.setSpeed(512)
    mtr_a2.setDistance(100)
    while mtr_a2.getCurrentDistance() < 100:
        txt.updateWait()
    mtr_a2.stop()

    logSPLK('Function: moveHBWGrab | Engine: mtr_a3 | Status: Moving back to transport position | Speed: 512')
    mtr_a3.setSpeed(512)
    while tst_a6.state()!=1:
        txt.updateWait()
    mtr_a3.stop()

    logSPLK('Function: moveHBWGrab | Engine: mtr_a2 | Status: Moving up to transport position | Speed: 512')
    mtr_a2.setSpeed(512)
    while tst_a8.state()!=1:
        txt.updateWait()
    mtr_a2.stop()
    logSPLK('Function: moveHBWGrab | Status: Done loading freight')

def moveHBWDeliver():
    logSPLK('Function: moveHBWDeliver | Status: Start')

    logSPLK('Function: moveHBWDeliver | Engine: mtr_a1 | Status: Delivering | Speed: 512')
    mtr_a1.setSpeed(512)
    while tst_a5.state()!=1:
        txt.updateWait()
    mtr_a1.stop()

    txt.SyncDataBegin()
    mtr_a3.setSpeed(-512)
    mtr_a2.setSpeed(-512)
    mtr_a2.setDistance(800)
    txt.SyncDataEnd()

    condition1 = False
    condition2 = False

    while not (condition1 and condition2):
      
        # Check if condition1 is met
        if not condition1:
            # Check if condition1 is now met
            if tst_a7.state()==1:
                condition1 = True
                mtr_a3.stop()

        # Check if condition2 is met
        if not condition2:
            # Check if condition2 is now met
            if mtr_a2.getCurrentDistance() >= 800:
                condition2 = True
                mtr_a2.stop()
    logSPLK('Function: moveHBWDeliver | Status: Done')

def moveHBWBack(cell_name,col,drop_cell):
    logSPLK('Function: moveHBWBack | Status: Start')

    logSPLK('Engine: mtr_a2 | Function: moveHBWBack | Status: Moving to position | Speed: 512')
    mtr_a2.setSpeed(512)
    while tst_a8.state()!=1:
        txt.updateWait()
    mtr_a2.stop()

    logSPLK('Engine: mtr_a3 | Function: moveHBWBack | Status: Moving to position | Speed: 512')
    mtr_a3.setSpeed(512)
    while tst_a6.state()!=1:
        txt.updateWait()
    mtr_a3.stop()

    logSPLK('Engine: mtr_a1 | Function: moveHBWBack | Status: Moving to position ' + cell_name + ' | Speed: -512| Distance:' + str(col))
    mtr_a1.setSpeed(-512)
    mtr_a1.setDistance(col)
    while mtr_a1.getCurrentDistance() < col:
        txt.updateWait()
    mtr_a1.stop()

    logSPLK('Engine: mtr_a2 | Function: moveHBWBack | Status: Moving to position | Speed: -512 | Distance:' + str(drop_cell))
    mtr_a2.setSpeed(-512)
    mtr_a2.setDistance(drop_cell)
    while mtr_a2.getCurrentDistance() < drop_cell:
        txt.updateWait()
    mtr_a2.stop()
    logSPLK('Function: moveDeliver | Status: Done')

def moveHBWDrop():
    logSPLK('Function: moveHBWDrop | Status: Start')

    logSPLK('Engine: mtr_a3 | Function: moveHBWDrop | Status: Positioning to unload freight | Speed: -512')
    mtr_a3.setSpeed(-512)
    while tst_a7.state()!=1:
        txt.updateWait()
    mtr_a3.stop()

    logSPLK('Engine: mtr_a2 | Function: moveHBWDrop | Status: Unloading freight | Speed: -512 | Distance: 100')
    mtr_a2.setSpeed(-512)
    mtr_a2.setDistance(100)
    while mtr_a2.getCurrentDistance() < 100:
        txt.updateWait()
    mtr_a2.stop()

    logSPLK('Engine: mtr_a3 | Function: moveHBWDrop | Status: Moving back | Speed: 512')
    mtr_a3.setSpeed(512)
    while tst_a6.state()!=1:
        txt.updateWait()
    mtr_a3.stop()
    logSPLK('Function: moveHBWDrop | Status: Done')

def moveHBWReset():
    logSPLK('Function: moveHBWReset | Status: Start')

    logSPLK('Engine: mtr_a2 | Function: moveHBWReset | Status: Moving back | Speed: 512')
    mtr_a2.setSpeed(512)
    while tst_a8.state()!=1:
        txt.updateWait()
    mtr_a2.stop()

    logSPLK('Engine: mtr_a1 | Function: moveHBWReset | Status: Moving back | Speed: 512')
    mtr_a1.setSpeed(512)
    while tst_a5.state()!=1:
        txt.updateWait()
    mtr_a1.stop()
    logSPLK('Function: moveHBWReset | Status: Done')

def moveVGGrab(cell_count,tqueue,vg_cb_turn,vg_cb_forth,vg_cb_down,vg_ho_turn,vg_ho_forth,vg_ho_down):
    logSPLK('Function: moveVGGrab | Status: Start')

    #Drehe zum Laufband
    logSPLK('Engine: mtr_b1 | Function: moveVGGrab | Status: Moving to convenur belt | Speed: -512 | Distance: 1400')
    mtr_b1.setSpeed(-512)
    mtr_b1.setDistance(vg_cb_turn)
    while mtr_b1.getCurrentDistance() < vg_cb_turn:
        txt.updateWait()
    mtr_b1.stop()

    #Fahre Arm raus
    logSPLK('Engine: mtr_b3 | Function: moveVGGrab | Status: Positioning to load freight | Speed: -512 | Distance: 170')
    mtr_b3.setSpeed(-512)
    mtr_b3.setDistance(vg_cb_forth)
    while mtr_b3.getCurrentDistance() < vg_cb_forth:
        txt.updateWait()
    mtr_b3.stop()

    # Fahre Greifarm runter
    logSPLK('Engine: mtr_b2 | Function: moveVGGrab | Status: Positioning to load freight | Speed: -512 | Distance: 200')
    mtr_b2.setSpeed(-512)
    mtr_b2.setDistance(vg_cb_down)
    while mtr_b2.getCurrentDistance() < vg_cb_down:
        txt.updateWait()
    mtr_b2.stop()

    #Sauger ein
    logSPLK('Engine: out_b7 | Function: moveVGGrab | Status: Loading freight | Level: 512')
    out_b7.setLevel(512)
    txt.updateWait()
    time.sleep(0.5)
    out_b8.setLevel(512)

    #Fahre Greifarm hoch
    mtr_b2.setSpeed(512)
    while tst_b2.state()!=1:
        txt.updateWait()
    mtr_b2.stop()

    # Write value so that the main script continues
    tqueue.put(cell_count)

    #Fahre Arm rein
    mtr_b3.setSpeed(512)
    while tst_b3.state()!=1:
        txt.updateWait()
    mtr_b3.stop()

    # Drehe zurück
    mtr_b1.setSpeed(512)
    mtr_b1.setDistance(vg_ho_turn)
    while mtr_b1.getCurrentDistance() < vg_ho_turn:
        txt.updateWait()
    mtr_b1.stop()

    #Fahre Arm raus
    mtr_b3.setSpeed(-512)
    mtr_b3.setDistance(vg_ho_forth)
    while mtr_b3.getCurrentDistance() < vg_ho_forth:
        txt.updateWait()
    mtr_b3.stop()

    # Fahre Greifarm runter
    mtr_b2.setSpeed(-512)
    mtr_b2.setDistance(vg_ho_down)
    while mtr_b2.getCurrentDistance() < vg_ho_down:
        txt.updateWait()
    mtr_b2.stop()

    # Sauger aus
    out_b8.setLevel(0)
    txt.updateWait()
    time.sleep(0.5)
    out_b7.setLevel(0)

    #Fahre Greifarm hoch
    mtr_b2.setSpeed(512)
    while tst_b2.state()!=1:
        txt.updateWait()
    mtr_b2.stop()

    #Fahre Arm rein
    mtr_b3.setSpeed(512)
    while tst_b3.state()!=1:
        txt.updateWait()
    mtr_b3.stop()

    # Drehe zurück
    mtr_b1.setSpeed(512)
    while tst_b1.state()!=1:
        txt.updateWait()
    mtr_b1.stop()
    logSPLK('Function: moveVGGrab | Status: Done')