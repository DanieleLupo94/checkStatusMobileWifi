import json
import sys
import time
from PyP100 import PyP100
import requests as req

configurazione = {}
fileConfig = open("./configTim", "r")
for line in fileConfig.read().splitlines():
        configurazione[line.split(' = ')[0]] = str(line.split(' = ')[1])

d = {}
d["jsonrpc"] = "2.0"
d["method"] = "GetSystemStatus"
d["id"] = "13.4"
d["params"] = 'null'

def getPresaTapo():
    p100 = PyP100.P100(configurazione["ipPresa"], configurazione["emailAccountTapo"], configurazione["passwordAccountTapo"])
    p100.handshake() 
    p100.login()
    return p100, p100.getDeviceInfo()["result"]

def accendiPresa(presa):
    presa.turnOn()
    presa, info = getPresaTapo()
    return info["device_on"] == True

def spegniPresa(presa):
    presa.turnOff()
    presa, info = getPresaTapo()
    return info["device_on"] == False

def getInformazioniModem():
    headers = {"Host": "mw40.home",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Accept": "text/plain, */*; q=0.01",
            "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "_TclRequestVerificationKey": "KSDHSDFOGQ5WERYTUIQWERTYUISDFG1HJZXCVCXBN2GDSMNDHKVKFsVBNf",
            "_TclRequestVerificationToken": "null",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "70",
            "Origin": "http://mw40.home",
            "Connection": "keep-alive",
            "Referer": "http://mw40.home/index.html",
            "Cookie": "",
            "Sec-GPC": "1"}

    r = req.post(configurazione["urlModem"], data=json.dumps(d), headers=headers)
    informazioni = json.loads(r.content)["result"]
    return {
        "batteria" : int(informazioni["bat_cap"]),
        "stato" : str(informazioni["chg_state"])
    }

'''
    Casi:
        - 
'''
def isInCarica(informazioniModem, presa):
    return informazioniModem["stato"] != '2'