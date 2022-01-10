import network
import time

def connettiWifiVodafone():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        retry = 10
        wifi.connect("Rete", "Password") # Provo a collegarmi al wifi
        wifi.connect("VodafoneMobileWiFi-215297", "0874635237") # Provo a collegarmi al wifi
        while not wifi.isconnected():
            time.sleep(1)
            retry = retry - 1
            print("Non ancora connesso. Retry rimanenti " + str(retry))
            if retry < 1:
                break
            pass
    return wifi.isconnected()
