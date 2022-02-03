# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import wifiManager as myWifiManager
import network
#import webrepl

connesso = myWifiManager.connettiWifiVodafone()
if connesso:
    import logManager as lm
    lm.scriviLog("Connesso al wifi.")
    #webrepl.start()
    import modemManager as mm
    import _thread as t
    import iftttManager as im

    def avviaThreadLoopCheck():
        im.inviaNotifica(testo = "Avviato loopCheck")
        return t.start_new_thread(mm.loopCheck, ())
    
    def avviaFTP():
        import uftpd as serverFTP
        wifi = network.WLAN(network.STA_IF)
        im.inviaNotifica(testo = "IP {}".format(wifi.ifconfig()[0]))

    im.inviaNotifica(testo = "ESP32 avviato")
    avviaThreadLoopCheck()
    #avviaFTP()
    
else:
    print("Impossibile connettersi.")
