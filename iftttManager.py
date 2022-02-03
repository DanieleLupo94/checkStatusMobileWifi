import urequests2 as req
import logManager as lm
import utils

conf = utils.loadConfigurations()

def inviaNotifica(url = conf["hookIFTTT"], testo = ""):
    mustNotify = bool(conf["logIFTTT"])
    if mustNotify:
        req.post(url, json={'value1': testo})
    
