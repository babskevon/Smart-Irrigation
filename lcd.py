from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep, time

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16


lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def welcome():
    lcd.clear()
    lcd.move_to(3,0)
    lcd.putstr("Welcome to")
    lcd.move_to(0,1)
    lcd.putstr("Smart Irrigation")
    sleep(7)
#welcome()
def irrig():
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Irrigating now..")
    
welcome()