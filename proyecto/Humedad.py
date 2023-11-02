import machine
import time

# Configuración del pin relay
relay_pin = 28
relay = machine.Pin(relay_pin, machine.Pin.OUT)

# Configuración  para la lectura analógica del sensor de humedad
sensor_pin = 27
sensor = machine.ADC(machine.Pin(sensor_pin))

umbral_encendido = 36600  # Umbral de humedad para desactivar el relé

while True:
    sensor_value = sensor.read_u16()
    print("Valor del sensor de humedad del suelo:", sensor_value)
    
    if sensor_value > umbral_encendido:
        print("El suelo está seco. Activando el relé.")
        relay.value(1)  # Enciende el relé
    else:
        print("El suelo está húmedo. Desactivando el relé.")
        relay.value(0)  # Apaga el relé
        
    time.sleep(3)  # Espera 3 segundo antes de la próxima lectura


# 65535 valor sin agua
# 36600 valor con agua humedad max