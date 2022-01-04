import urequests2 as req

def inviaNotifica(url = "hook ifttt", testo = ""):
    req.post(url, json={'value1': testo})