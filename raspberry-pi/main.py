from machine import Pin, I2C
import utime as time
from dht import *

# /dev/cu.usbmodem1101

#while True:
#    time.sleep(5)
#    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
#   sensor = DHT11(pin)
#    t  = (sensor.temperature)
#    h = (sensor.humidity)
#    print("Temperature: {}".format(sensor.temperature()))
#    print("Humidity: {}".format(sensor.humidity()))

pin = Pin(0, Pin.IN)

while 1:
    time.sleep(2)
    data_dht = DHT11(pin)
    temp = (data_dht.temperature())
    humi = (data_dht.humidity())
    print("temp -> {}".format(temp))
    print("humid -> {}".format(humi))