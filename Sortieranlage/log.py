import requests
import datetime

def logSPLK(message):
    now = str(datetime.datetime.now()) + " CEST | Sortieranlage |"
    message='{} {}'.format(now, message)
    r = requests.post("http://ec2-52-29-244-98.eu-central-1.compute.amazonaws.com:8088/services/collector/raw", verify=False, headers={
    "Authorization": "Splunk 91ade850-752e-4d69-8d9b-6fbc2947347b",
    "X-Splunk-Request-Channel": "FE0ECFAD-13D5-401B-847D-77833BD77131",
    }, data=message)