import ftrobopy

txtController_ip = "192.168.0.128"
txtController_port = 65000
txtController_update_interval = 0.01
txtController_use_extension = True

try:
    txt = ftrobopy.ftrobopy(txtController_ip, txtController_port,txtController_update_interval,txtController_use_extension)
    txt.updateWait()
except Exception as e:
    print(e)
    quit()
