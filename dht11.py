import sys
import Adafruit_DHT
import time
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep, time

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
from lcd import welcome

lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

humidity = 0.0
temperature = 0.0
while True:
    try:
        #dht11 using gpio 4
        #welcome()
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("Soil moist=" + str(86.4) + "%")
        lcd.move_to(0,1)
        lcd.putstr("temp=" + str(temperature) + "C")
        time.sleep(2)
        print("humidity={}, temp={}".format(humidity, temperature))
    except:
        pass