# harini_shree
from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

# I2C configuration
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Initialize display (128x64 OLED)
oled = SSD1306_I2C(128, 64, i2c)

# Clear and write to display
oled.fill(0)
oled.text("harini", 0, 0)
oled.text("yuvashree", 0, 10)
oled.text("exp 11", 0, 20)
oled.show()

# Loop (optional animation/sensor handling)
while True:
    time.sleep(1)
