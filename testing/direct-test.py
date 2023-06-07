import ftrobopy    

txtController_ip = "auto"

txt = ftrobopy.ftrobopy(txtController_ip)
txt.updateWait()

temperatur = txt.getTemperature()
print(temperatur)

spannung = txt.getPower()
print(spannung)