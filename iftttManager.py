import urequests2 as req
import logManager as lm

def inviaNotifica(url = "hook ifttt", testo = ""):
    req.post(url, json={'value1': testo})
    lm.scriviLog("IFTTT >> " + testo)
    