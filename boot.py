# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import wifiManager as myWifiManager
import logManager as lm
#import webrepl

connesso = myWifiManager.connettiWifiVodafone()
if connesso:
    lm.scriviLog("Connesso al wifi.")
    #webrepl.start()
    import modemManager as mm
    import _thread as t
    import iftttManager as im

    def avviaThreadLoopCheck():
        im.inviaNotifica(testo = "Avviato loopCheck")
        return t.start_new_thread(mm.loopCheck, ())

    avviaThreadLoopCheck()
    im.inviaNotifica(testo = "ESP32 avviato")
else:
    lm.scriviLog("Impossibile connettersi.")


