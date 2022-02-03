import json

fileConfigurazione = "generalConfig.json"

def loadConfigurations():
    file = open(fileConfigurazione, "r")
    configurazioni = json.load(file)
    file.close()
    #print(configurazioni)
    return configurazioni

def setFileConfigurazione(f):
    global fileConfigurazione
    fileConfigurazione = f