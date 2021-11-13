import requests as req
import time
import datetime
import traceback

modemType = ""

def log(msg, isErrore = False):
    nomeFile = "Errore" if isErrore else getModemType()
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d")
    pathLog = "./log" + nomeFile + now.strftime("%Y%m%d") + ".log"
    fileLog = open(pathLog, "a+")
    t = "[" + time.asctime(time.localtime(time.time())) + "] " + str(msg)
    fileLog.write(t)
    fileLog.write("\n")
    fileLog.close()

def getModemObject():
    global modemType
    try:
        c = req.get("http://vodafonemobile.wifi/html/home.htm")
        if int(c.status_code) == 200:
            modemType = "Vodafone"
            import vodafone as modem
            log("Riconosciuto modem Vodafone")
            return modem
        else:
            raise Exception()
    except:
        try:
            c = req.get("http://mw40.home/index.html")
            if int(c.status_code) == 200:
                modemType = "Tim"
                import tim as modem
                log("Riconosciuto modem Tim")
                return modem
            else:
                raise Exception()
        except:
            log("Impossibile riconoscere il tipo di modem", True)
            time.sleep(60 * 2)
            check()

def getModemType():
    global modemType
    if modemType == "":
        getModemObject()
    return modemType

def check():
    modem = getModemObject() 
    try:
        informazioniModem = modem.getInformazioniModem()
    except:
        log("Impossibile connettersi al modem", True)
        modemType = ""
        time.sleep(60 * 3)
        check()
    batteria = int(informazioniModem["batteria"])

    presa, _ = modem.getPresaTapo()

    log("Batteria " + str(informazioniModem["batteria"]) + ", in carica? " + str(modem.isInCarica(informazioniModem, presa)))

    if batteria < 21 :
        # Se non sta caricando, dovrei caricare
        if not modem.isInCarica(informazioniModem, presa):
            log("Batteria scarica")
            log("Presa accesa") if modem.accendiPresa(presa) else log("Errore nell'accensione della presa")
    elif batteria > 99 :
        if modem.isInCarica(informazioniModem, presa):
            log("Batteria carica")
            log("Presa spenta") if modem.spegniPresa(presa) else log("Errore nello spegnimento della presa")

    time.sleep(60 * 10)
    check()

def main():
    log("Avvio")
    check()

try:
    main()
except Exception:
    log("Errore. Riavvio")
    traceback.print_exc()
    main()
finally:
    log("Riavvio il programma")
    main()