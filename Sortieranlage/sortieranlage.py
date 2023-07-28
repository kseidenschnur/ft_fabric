import time
from connectTXT import *

logSPLK('Starting sortieranlage.py' )

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

def detect_color_value():
    #Sammle Farbwerte und nehm den mit den niedrigsten Wert als Farbe
    while True:
        color_list = []
        txt.updateWait()
        while tst_a3.state() != 0:
            color_value = tst_a2.value()
            txt.updateWait()
            color_list.append(color_value)
        color_value = min (color_list)
        return color_value
        break

def determine_color(color_value):
    #Weiße den entsprechenden Werten die Farbe zu
    color = 'None'
    if 620 <= color_value <= 670:
        color = 'white'
    elif 1120 <= color_value <= 1200:
        color = 'red'
    elif 1530 <= color_value <= 1590:
        color = 'blue'
    return color

def sort_color(color):
    if color == 'white':
        #Kompressor ein
        out_a8.setLevel(512)
        #Warten auf richtige Position
        time.sleep(0.7)
        txt.updateWait()
        #Push ein
        out_a5.setLevel(512)
        txt.updateWait()
        time.sleep(0.5)
        #Push aus
        out_a5.setLevel(0)
        txt.updateWait()
        #Kompressor aus
        out_a8.setLevel(0)

    elif color=='red':
        out_a8.setLevel(512)
        time.sleep(2)
        txt.updateWait()
        out_a6.setLevel(512)
        txt.updateWait()
        time.sleep(0.5)
        out_a6.setLevel(0)
        txt.updateWait()
        out_a8.setLevel(0)

    elif color=='blue':
        out_a8.setLevel(512)
        time.sleep(3.5)
        txt.updateWait()
        out_a7.setLevel(512)
        txt.updateWait()
        time.sleep(0.5)
        out_a7.setLevel(0)
        txt.updateWait()
        out_a8.setLevel(0)

######################################################################################################################################

print("Sortieranalage")
while True:
    txt.updateWait()
    if tst_a1.state() == 0:
        mtr_a1.setSpeed(-512)
        color_value = detect_color_value()
        color = determine_color(color_value)
        logSPLK("Status: " + color)
        sort_color(color)
        mtr_a1.stop()