import ftrobopy
from log import logSPLK

def connectTXT():
    txtController_ip = "192.168.0.14"
    txtController_port = 65000
    #txtUpdate_interval = 0.01
    txtUse_extension = False

    logSPLK('Connecting to ' + str(txtController_ip) + ':' + str(txtController_port))
    try:
        txt = ftrobopy.ftrobopy(txtController_ip, txtController_port, use_extension=txtUse_extension)
        txt.updateWait()
        logSPLK('Connection to ' + str(txtController_ip) + ':' + str(txtController_port) + ' sucessfully established!')
    except Exception as e:
        logSPLK(e)
        quit()
    
    return txt
