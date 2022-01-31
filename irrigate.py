from moist import moisture, light_intensity  # 2,4 moisture(2,4). channel 6 is ight_intensity(6)
from gpiozero import DistanceSensor
import sys
import Adafruit_DHT
import rate
import requests
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from lcd import welcome
from photos import photo

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16


lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
welcome()
rate.valve()
soil_moisture = 0.0
light = 0.0
water_level = 0.0
humidity = 0.0
temperature = 0.0
flowrate1 = 0.0
flowrate2 = 0.0
#url to send data to
url = 'https://robinah.pythonanywhere.com/data/'
test_url = "https://robinah.pythonanywhere.com/photo/"


try:
    waterlevel = DistanceSensor(echo=17, trigger=18) #gpio17 and trigger18
except:
    pass

def getValues():
    soil_mosture = moisture(2,4)
    light = light_intensity(6)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) #using gpio4
    flowrate1 = rate.sensorone()
    flowrate2 = rate.sensortwo()
    water_level = waterlevel.distance
    data = {
            'light':light,
            'humidity':humidity,
            'temperature':temperature,
            'distance':water_level,
            'flowrate1':flowrate1,
            'flowrate2':flowrate2,
            'soil_moisture':soil_moisture
        }
    return data
while True:
    try:
        data = getValues()
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("Soil moist="+ str(data['soil_moisture'])+"%")
        lcd.move_to(0,1)
        lcd.putstr("Temp=" + str(data['temperature'])+"C")
        sleep(2)
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("humidity="+str(humidity)+"%")
        lcd.move_to(0,1)
        lcd.putstr("flowrate="+str(data['flowrate1']) + "L/min")
        sleep(2)
        value = requests.post(url,data=data)
        if(value['photo'] == True):
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Taking photo")
            name = photo()
            file = open(name, "rb")
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Taking photo")
            response = requests.post(test_url, files = {"name": file})
            
        rate.valve(soil_mosture,value['cmd'],light)
        
    except:
        pass