from machine import ADC
from time import sleep 
from math import log 

lm35 = ADC(27)

while True:
  valor = lm35.read_u16()
  print(valor)
  c = 1/(log(1/(65535/valor-1))/3950+1.0/298.15)-273.15
  print(c)
  sleep(2)