from tplink_smartplug import SmartPlug
import urequests2 as req

configurazione = {}
fileConfig = open("./configVodafone", "r")
for line in fileConfig.read().splitlines():
        configurazione[line.split(' = ')[0]] = str(line.split(' = ')[1])

def bruteSearchPresa():
    baseIp = configurazione['baseIp']
    for x in range(100, 120):
        try:
            plug = SmartPlug(baseIp + str(x))
            plug.name
            return plug
        except:
            continue
    return None

def getPresaTapo():
    try:
        plug = SmartPlug(configurazione["ipPresa"])
        plug.name
        return plug, None
    except Exception as e:
        print(e)
        plug = bruteSearchPresa()
        return plug, None
    print("Errore nella ricerca della presa.")
    return None, None

def accendiPresa(presa):
    presa.turn_on()
    return presa.is_on

def spegniPresa(presa):
    presa.turn_off()
    return not presa.is_on

def getInformazioniModem():
    r = req.get(configurazione["urlModem"])
    setCookie = r.headers['Set-Cookie'].split(';path')[0]
    r = req.get(configurazione['urlAPI'], headers = {'Cookie': setCookie})
    # Il contenuto della risposta ha bisogno di essere decodificato in UTF-8
    contenuto = r.content.decode('utf-8')
    livelloBatteria = contenuto[contenuto.find("<BatteryLevel>") + 14 : contenuto.find("</BatteryLevel>")]
    inCarica = contenuto[contenuto.find("<BatteryStatus>") + 15 : contenuto.find("</BatteryStatus>")]
    return {
        "batteria" : int(livelloBatteria),
        "stato" : str(inCarica)
    }

''' Casi: 
        - 1 e presa accesa -> sta caricando
        - 1 e presa spenta -> sta caricando con un'altra presa
        - 0 e presa accesa -> non sta caricando e la presa non sta vicino al modem oppure ha finito di caricare
        - 0 e presa spenta -> non sta caricando di sicuro
'''
def isInCarica(informazioniModem, presa):
    return str(informazioniModem["stato"]) == "1" or (str(informazioniModem["stato"]) == "0" and presa.is_on)