import vodafone as modem
import time
import iftttManager as im

def customLog(testo = ""):
    # Aggiungo data e ora
    now = time.localtime()
    testo = str(now[0:5]) + " - " + testo
    print(testo)
    im.inviaNotifica(testo = testo)

def check():
    informazioniModem = modem.getInformazioniModem()
    batteria = int(informazioniModem["batteria"])
    stato = str(informazioniModem["stato"])
    retryPresa = 10
    presa = None
    while retryPresa > 0 and presa is None:
        presa, _ = modem.getPresaTapo()
    if presa is None:
        customLog("Impossibile contattare la presa.")
        return None
    isInCarica = modem.isInCarica(informazioniModem, presa)
    customLog("batteria " + str(batteria) + ", stato " + str(stato) + ", isInCarica " + str(isInCarica))
    if batteria < 21:
        # Se non sta caricando, dovrei caricare
        if not isInCarica:
            customLog("Batteria scarica")
            customLog("Presa accesa") if modem.accendiPresa(presa) else customLog("Errore nell'accensione della presa")
    elif batteria > 99:
        if isInCarica:
            customLog("Batteria carica")
            customLog("Presa spenta") if modem.spegniPresa(presa) else customLog("Errore nello spegnimento della presa")

def loopCheck():
    try:
        # Controllo
        check()
        # Attendo 10 minuti
        time.sleep(10 * 60)
        loopCheck()
    except Exception as e:
        customLog(str(e))