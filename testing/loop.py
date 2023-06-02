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
    logSPLK('Connection to ' + str(txtController_ip) + ':' + str(txtController_port) + ' failed!')
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

col_a = 775 
col_b = 1390
col_c = 2005
get_cell_1 = 140
get_cell_2 = 500
get_cell_3 = 890
bring_cell_1 = 40
bring_cell_2 = 400
bring_cell_3 = 790


#Creating list of positions for loop
positions = [['a1', col_a, get_cell_1, bring_cell_1], ['a2', col_a, get_cell_2, bring_cell_2], ['a3', col_a, get_cell_3, bring_cell_3],['b1', col_b, get_cell_1, bring_cell_1], ['b2', col_b, get_cell_2, bring_cell_2], ['b3', col_b, get_cell_3, bring_cell_3]]

#Defining counter for loop
#col = positions[4][1]
#get_cell = positions[4][2]
#bring_cell = positions[4][3]

i=1

while i==1:
    col = positions[i][1]
    get_cell = positions[i][2]
    bring_cell = positions[i][3]

    logSPLK('Engine: mtr_a1 | Function: moveGet | Status: Moving to position A | Speed: -512 | Distance:' + str(col))
    mtr_a1.setSpeed(-512)
    mtr_a1.setDistance(775)
    while mtr_a1.getCurrentDistance() < 775:
        txt.updateWait()
        fin = mtr_a1.finished()
        dis = mtr_a1.getCurrentDistance()
        print(fin)
        print(dis)
    logSPLK('Engine: mtr_a1| Function: moveGet| Status: Reached position A')
    mtr_a1.stop()
    txt.updateWait()

    logSPLK('Engine: mtr_a1 | Function: moveGet | Status: Moving to position A | Speed: -512 | Distance:' + str(col))
    mtr_a1.setSpeed(512)
    while tst_a5.state()!=1:
        txt.updateWait()             
    logSPLK('Engine: mtr_a1| Function: moveGet| Status: Reached position A')
    mtr_a1.stop()
    txt.updateWait()
    