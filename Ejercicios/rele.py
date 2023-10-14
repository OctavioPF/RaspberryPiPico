from machine import Pin
from time import sleep

rele = Pin(28, Pin.OUT)

while True:
    rele.value(1)
    sleep(2)
    rele.value(0)
    sleep(2)