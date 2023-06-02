import ftrobopy
import time
from log import logSPLK

txtController_ip = "192.168.0.10"
txtController_port = 65000
#txtUpdate_interval = 0.01
txtUse_extension = True

logSPLK('Connecting to ' + str(txtController_ip) + ':' + str(txtController_port))
try:
    txt = ftrobopy.ftrobopy(txtController_ip, txtController_port, use_extension=txtUse_extension)
    txt.updateWait()
    logSPLK('Connection to ' + str(txtController_ip) + ':' + str(txtController_port) + ' sucessfully established!')
except Exception as e:
    logSPLK(e)
    quit()


#Create engine objects for high-bay warehouse
mtr_a1 = txt.motor(2) #Engine A1 - Back and forth
mtr_a2 = txt.motor(4) #Engine A2 - Up and Down (Arm)
mtr_a3 = txt.motor(3) #Engine A3 - Back and Forth (Arm) 
mtr_a4 = txt.motor(1) #Engine A4 - Conveyor belt

# Create engine objects for vacuum arm
mtr_b1 = txt.motor(1, ext=1) # Engine 5 - Turning
mtr_b2 = txt.motor(2, ext=1) # Motor 6
mtr_b3 = txt.motor(3, ext=1) # Motor 7
mtr_b4 = txt.motor(4, ext=1) # Motor 8

# Create output object for valve
ausgang8 = txt.output(8, ext=1)

# Create objects for sensors
tst_a1 = txt.input(1)
tst_a2 = txt.input(2)
tst_a3 = txt.input(3)
tst_a4 = txt.input(4)
tst_a5 = txt.input(5)
tst_a6 = txt.input(6)
tst_a7 = txt.input(7)
tst_a8 = txt.input(8)

tst_b1 = txt.input(1, ext=1)
tst_b2 = txt.input(2, ext=1)
tst_b3 = txt.input(3, ext=1)
tst_b4 = txt.input(4, ext=1)
tst_b5 = txt.input(5, ext=1)
tst_b6 = txt.input(6, ext=1)
tst_b7 = txt.input(7, ext=1)
tst_b8 = txt.input(8, ext=1)

###########################################################################################################################

a = 785 
a1 = 140
a2 = 0
a3 = 0
b = 0
b1 = 0
b2 = 0
b3 = 0
c = 0
c1 = 0
c2 = 0
c3 = 0

###########################################################################################################################

def move(row, cell):

    logSPLK('Engine: mtr_a1; Function: move; Status: Moving to position A; Speed: -512; Distance:' + row)
    mtr_a1.setSpeed(-512)
    mtr_a1.setDistance(row)
    while not mtr_a1.finished():
        txt.updateWait()
    logSPLK('Engine: mtr_a1; Function: move; Status: Reached position A')
    mtr_a1.stop()

    logSPLK('Engine: mtr_a2; Function: move; Status: Moving to position A1; Speed: -512; Distance:' + cell)
    mtr_a2.setSpeed(-512)
    mtr_a2.setDistance(cell)
    while not mtr_a2.finished():
        txt.updateWait()
    logSPLK('Engine: mtr_a2; Function: move; Status: Reached position A1')
    mtr_a2.stop()

move(a, a1)