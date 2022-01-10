import urequests2 as req
import logManager as lm

def inviaNotifica(url = "hook ifttt", testo = ""):
def inviaNotifica(url = "http://maker.ifttt.com/trigger/CheckBatteria/with/key/crgmhm7kuG2plVg8e7W1_V", testo = ""):
    req.post(url, json={'value1': testo})
    lm.scriviLog("IFTTT >> " + testo)
    