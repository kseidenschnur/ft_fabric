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


taster1 = txt.input(1, ext=1)
print ('Taster 1')
print (taster1.state())

taster2 = txt.input(2, ext=1)
print ('Taster 2')
print (taster2.state())

taster3 = txt.input(3, ext=1)
print ('Taster 3')
print (taster3.state())

taster4 = txt.input(4, ext=1)
print ('Taster 4')
print (taster4.state())

taster5 = txt.input(5, ext=1)
print ('Taster 5')
print (taster5.state())

taster6 = txt.input(6, ext=1)
print ('Taster 6')
print (taster6.state())

taster7 = txt.input(7, ext=1)
print ('Taster 7')
print (taster7.state())

taster8 = txt.input(8, ext=1)
print ('Taster 8')
print (taster8.state())