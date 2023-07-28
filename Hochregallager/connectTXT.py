import ftrobopy
import requests
import datetime

def logSPLK(message):
    now = str(datetime.datetime.now()) + " CEST | Module: HBW+VG |"
    message='{} {}'.format(now, message)
    r = requests.post("http://ec2-54-93-68-230.eu-central-1.compute.amazonaws.com:8088/services/collector/raw", verify=False, headers={
    "Authorization": "Splunk 91ade850-752e-4d69-8d9b-6fbc2947347b",
    "X-Splunk-Request-Channel": "FE0ECFAD-13D5-401B-847D-77833BD77131",
    }, data=message)

def connectTXT():
    txtController_ip = "192.168.0.10"
    txtController_port = 65000
    #txtUpdate_interval = 0.01
    txtUse_extension = True

    logSPLK('Connecting to ' + str(txtController_ip) + ':' + str(txtController_port) + '...')
    try:
        txt = ftrobopy.ftrobopy(txtController_ip, txtController_port, use_extension=txtUse_extension)
        txt.updateWait()
        logSPLK('Connection to ' + str(txtController_ip) + ':' + str(txtController_port) + ' sucessfully established!')
    except Exception as e:
        logSPLK(e)
        quit()
    return txt