import ftrobopy
import time

txtController_ip = "192.168.0.128"
txtController_port = 65000
txtController_update_interval = "update_interval=0.01"
txtController_use_extension = "use_extension=True"

try:
    txt = ftrobopy.ftrobopy(txtController_ip, txtController_port,use_extension=True)
    txt.updateWait()
except Exception as e:
    print(e)
    quit()

#Motor 5 - Greifarm
motor5 = txt.motor(1, ext=1)
txt.updateWait()

taster1 = txt.input(1, ext=1)
taster2 = txt.input(2, ext=1)
taster3 = txt.input(3, ext=1)
taster4 = txt.input(4, ext=1)
taster5 = txt.input(5, ext=1)
taster6 = txt.input(6, ext=1)
taster7 = txt.input(7, ext=1)
taster8 = txt.input(8, ext=1)

# motor1.setSpeed(-512)
# motor1.setDistance(500)
# while not motor1.finished():
#     txt.updateWait()
#     print ('Motor läuft noch....')
# motor1.stop

# motor2.setSpeed(-512)
# motor2.setDistance(100)
# while not motor2.finished():
#     txt.updateWait()
#     print ('Motor läuft noch....')
# motor1.stop

print ('Starte Motor')
motor5.setSpeed(-512)
motor5.setDistance(1400)
while not motor5.finished():
    txt.updateWait()
    print ('Motor 5 läuft noch....')
motor5.stop()

print ('Starte Motor')
motor5.setSpeed(512)
motor5.setDistance(0)
while taster1.state()!=1:
    txt.updateWait()
    print ('Motor 5 läuft noch....')
motor5.stop()