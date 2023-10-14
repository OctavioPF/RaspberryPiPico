import machine
import time

ldr = machine.ADC(27)
led = machine.Pin(15,machine.Pin.OUT)
while True:
    volt = ldr.read_u16()
    print(volt)
    time.sleep(1)
    if volt < 13500:
        led.value(1)
    else:
        led.value(0)