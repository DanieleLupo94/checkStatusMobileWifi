import time

def getNomeFile():
    now = time.localtime()
    return "log" + str(now[0]) + str(now[1]) + str(now[2])

def getDataOra():
    now = time.localtime()
    return str(now[0]) + "\\" + str(now[1]) + "\\" + str(now[2]) + " " + str(now[3]) + ":" + str(now[4]) + ":" + str(now[5])
    
def scriviLog(riga):
    nomeFile = getNomeFile()
    file = open(nomeFile, "a+")
    riga = "[" + getDataOra() + "] " + riga
    file.write(riga)
    file.write("\n")
    file.close()