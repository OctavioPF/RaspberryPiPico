echo = Pin(20, Pin.IN)
trig = Pin(21, Pin.OUT)

while True:
    trig.value(0)
    sleep_us(5)
    trig.value(1)
    Sleep_us(10)
    trig.value(0)

    tiempo = time_pulse_us(echo, 1)
    distancia = tiempo/58

    print(f"Distancia: {distancia} cm")
    sleep(1)
