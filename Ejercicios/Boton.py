import machine
import time
led =machine.Pin(15,
machine.Pin.OUT)
boton = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
led_encendido = False

while True:
    if boton.value() == 1:  # Botón presionado
        led_encendido = not led_encendido  # Cambiar el estado del LED
        if led_encendido:
            led.on()  # Encender el LED
        else:
            led.off()  # Apagar el LED
        while boton.value() == 1:  # Esperar a que se suelte el botón
            time.sleep(0.1)  # Pequeña pausa para evitar rebotes del bo
