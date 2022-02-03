import time
import urequests2 as req
import utils

conf = utils.loadConfigurations()

response = req.get(conf["urlDate"])
if response.status_code == 200:
    nomeFile = "log" + response.content.decode('utf-8')
else:
    nomeFile = "log00000000"

def sendLog(riga):
    req.post(conf["urlLog"], json = {"riga" : riga})
    
def scriviLog(riga):
    mustWrite = conf["logfile"]
    if mustWrite == "True":
        file = open(nomeFile, "a+")
        file.write(riga)
        file.write("\n")
        file.close()
    sendLog(riga)
