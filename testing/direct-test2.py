import time
import ftrobopy

txt=ftrobopy.ftrobopy('auto')


temperatur = txt.getTemperature()
print(temperatur)
spannung = txt.getPower()
print(spannung)
time.sleep(2)