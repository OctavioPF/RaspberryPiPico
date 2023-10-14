from machine import Pin, PWM
from time import sleep
pwm = PWM(Pin(28))
pwm.freq(50)
duty_min = 65536 / 20000 * 500
duty_max = 65536 / 20000 * 2450

def setServoCycle (grados):
    position = int (duty_min + ((duty_max - duty_min) / 180) * grados)
    pwm.duty_u16(position)

    while True:
        setServoCycle(0)
        sleep(0)
        setServoCycle(90)
        sleep(1)
        setServoCycle(180)
        sleep(1)

