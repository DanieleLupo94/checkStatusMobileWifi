import vodafone as modem
import time
import iftttManager as im
import logManager as lm

canLoop = True

def customLog(testo = ""):
    lm.scriviLog(testo)
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
    customLog("Batteria: " + str(batteria) + ", stato: " + str(stato) + ", isInCarica: " + str(isInCarica))
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
    global canLoop
    canLoop = True
    try:
        while canLoop:
            # Controllo
            check()
            # Attendo 30 minuti
            time.sleep(30 * 60)
    except Exception as e:
        canLoop = False
        customLog("Termino l'esecuzione per via del seguente errore: " + str(e))