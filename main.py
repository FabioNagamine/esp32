"""
    this main script

"""
from machine import Pin, PWM, I2C
from utime import *
import urequests
import oled
import dht
import json
import gc
import api


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('teste', 'realtime')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())



telegram = api.TelegramBot('1098730564:AAE_OW26MY2WkjUu4keqhfGg4Jn1juNFQQE')


def message_handler(messages):
    for message in messages:
        if message[2] == '/start':
            telegram.send(message[0], 'Send me Message')
        else:
            telegram.send(message[0], 'Message printed!')
    gc.collect()

telegram.listen(message_handler)
"""
d = dht.DHT11(Pin(33))
d.measure()
temp = d.temperature()
umi = d.humidity()


teste = urequests.get("https://fabioniot.mybluemix.net/planta2").json()

payload = {"temperatura": temp, "umidade": 60, "umidadeAr": umi, "User": 0, "bomba": 0, "luminosidade": 76}
r = urequests.post('https://fabioniot.mybluemix.net/estufa', data=json.dumps(payload))
print(r.text)


pinI2C = I2C(-1, scl=Pin(4), sda=Pin(5))

oled = SSD1306.SSD1306_I2C(128, 64, pinI2C)
for linha in range(0, 128):
    oled.pixel(linha, 0, 1)
    oled.pixel(linha, 63, 1)
for coluna in range(0, 64):
    oled.pixel(0, coluna, 1)
    oled.pixel(127, coluna, 1)
oled.text('Hello world', 0, 0, 1)
oled.show()




while (1):
    print(teste)


    sleep(10)

"""
