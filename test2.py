from gpiozero import MCP3208, DistanceSensor
import time
import RPi.GPIO as GPIO
import adafruit_dht
import psutil
#GPIO.setmode(GPIO.BCM)

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(21)
#GPIO.setup(12, GPIO.IN)
temp = 0
humidity = 0

while True:
    #sensor = DistanceSensor(echo=4, trigger=18)
    try:
        print("try again")
        adc_value = MCP3208(channel=3).value
        print(adc_value * 3.3)
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        GPIO.cleanup()
        #print(sensor)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)
    
    

