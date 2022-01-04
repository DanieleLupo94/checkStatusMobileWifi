# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import wifiManager as myWifiManager

connesso = myWifiManager.connettiWifiVodafone()
if connesso:
    print("Connesso al wifi.")
else:
    print("Impossibile connettersi.")

import modemManager as mm
import _thread as t
import iftttManager as im

def avviaThreadLoopCheck():
    im.inviaNotifica(testo = "Avviato loopCheck")
    return t.start_new_thread(mm.loopCheck, ())

avviaThreadLoopCheck()
im.inviaNotifica(testo = "ESP32 avviato")
