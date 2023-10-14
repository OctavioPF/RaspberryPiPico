from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
i2c = I2C(0,sda=Pin(8), scl=Pin(9))

oled = SSD1306_I2C(128, 32, i2c)#64

x=0

while True:
    oled.fill(0)
    oled.show()
    oled.text('Hello world', 0, 0)
    oled.text(str(x), 0, 10)
    oled.show()
    x = x + 1
    sleep(2)